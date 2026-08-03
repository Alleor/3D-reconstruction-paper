#!/usr/bin/env python3
"""Discover recent 3D reconstruction papers and render README.md.

The script intentionally depends only on Python's standard library.  OpenAlex
provides paper metadata; GitHub repository search is used conservatively to
locate likely official implementations.  Curated records are never removed.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

from taxonomy import (
    CATEGORY_DESCRIPTIONS,
    CATEGORY_NAMES_ZH,
    CATEGORY_ORDER,
    classify_paper,
    reclassify_papers,
)


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "papers.json"
CONFIG_FILE = ROOT / "config.json"
README_FILE = ROOT / "README.md"

VENUE_PATTERNS = [
    ("CVPR", r"computer vision and pattern recognition|\bcvpr\b"),
    ("ICCV", r"international conference on computer vision|\biccv\b"),
    ("ECCV", r"european conference on computer vision|\beccv\b"),
    ("TPAMI", r"pattern analysis and machine intelligence|\btpami\b"),
    ("IROS", r"intelligent robots and systems|\biros\b"),
    ("ICRA", r"international conference on robotics and automation|\bicra\b"),
    ("TRO", r"transactions on robotics(?! and)|\btro\b"),
    ("RA-L", r"robotics and automation letters|\bra-l\b|\blra\b"),
    ("ICLR", r"international conference on learning representations|\biclr\b"),
    ("3DV", r"international conference on 3d vision|\b3dv\b"),
]

EXCLUDE_TERMS = {
    "tomography", "magnetic resonance", "mri", "computed tomography",
    "electron microscopy", "microscopy", "cardiac", "dental", "molecule",
    "catalyst", "protein", "chromosome", "ultrasound image reconstruction",
}

PURE_TASK_TERMS = {
    "segmentation", "compression", "quality assessment", "scene quality",
    "action manipulation", "text to 3d generation", "text to 4dgs generation",
}

RELEVANCE_TERMS = {
    "3d reconstruction", "surface reconstruction", "scene reconstruction",
    "shape reconstruction", "dense mapping", "neural rendering",
    "novel view synthesis", "radiance field", "gaussian splatting",
    "multi-view stereo", "multiview stereo", "neural implicit surface",
    "dense slam", "visual geometry", "structure from motion",
}

STOP_WORDS = {
    "a", "an", "and", "as", "at", "by", "for", "from", "in", "into",
    "of", "on", "or", "the", "to", "towards", "using", "via", "with",
    "3d", "neural", "reconstruction",
}


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def title_key(title: str) -> str:
    return normalize(title)


def compact_title_tokens(title: str) -> list[str]:
    return [
        token for token in normalize(title).split()
        if token not in STOP_WORDS and len(token) > 2
    ]


def request_json(url: str, token: str | None = None, retries: int = 3) -> dict[str, Any]:
    headers = {
        "Accept": "application/json",
        "User-Agent": "Alleor-Awesome-3D-Reconstruction-Papers/1.0",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
        headers["X-GitHub-Api-Version"] = "2022-11-28"
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(
                urllib.request.Request(url, headers=headers), timeout=45
            ) as response:
                return json.load(response)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            if attempt == retries - 1:
                raise RuntimeError(f"request failed: {url}: {exc}") from exc
            time.sleep(2 ** attempt)
    raise AssertionError("unreachable")


def reconstruct_abstract(index: dict[str, list[int]] | None) -> str:
    if not index:
        return ""
    words: list[tuple[int, str]] = []
    for word, positions in index.items():
        words.extend((position, word) for position in positions)
    return " ".join(word for _, word in sorted(words))


def source_text(work: dict[str, Any]) -> str:
    names: list[str] = []
    for location in work.get("locations") or []:
        if location.get("raw_source_name"):
            names.append(location["raw_source_name"])
        source = location.get("source") or {}
        if source.get("display_name"):
            names.append(source["display_name"])
    return " | ".join(names)


def detect_venue(work: dict[str, Any]) -> str | None:
    text = source_text(work)
    for venue, pattern in VENUE_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            return venue
    work_type = (work.get("type") or "").lower()
    if "arxiv" in text.lower() or work_type in {"preprint", "posted-content"}:
        return "arXiv"
    return None


def is_relevant(work: dict[str, Any]) -> bool:
    abstract = reconstruct_abstract(work.get("abstract_inverted_index"))
    text = normalize(f"{work.get('title', '')} {abstract}")
    if any(term in text for term in EXCLUDE_TERMS):
        return False
    title = normalize(work.get("title", ""))
    if any(term in title for term in PURE_TASK_TERMS) and "reconstruct" not in title:
        return False
    explicit = any(term in title for term in RELEVANCE_TERMS)
    topic = work.get("primary_topic") or {}
    subfield = normalize((topic.get("subfield") or {}).get("display_name", ""))
    cv_topic = "computer vision" in subfield
    contextual = any(term in text for term in RELEVANCE_TERMS)
    title_signal = any(
        term in title
        for term in ("3d", "4d", "geometry", "splat", "radiance", "novel view", "surface", "scene", "avatar")
    )
    return explicit or (cv_topic and contextual and title_signal)


def best_paper_url(work: dict[str, Any]) -> str:
    ids = work.get("ids") or {}
    if ids.get("arxiv"):
        return ids["arxiv"].replace("http://", "https://")
    doi = work.get("doi") or ""
    arxiv_doi = re.search(r"10\.48550/arxiv\.([0-9.]+)", doi, flags=re.IGNORECASE)
    if arxiv_doi:
        return f"https://arxiv.org/abs/{arxiv_doi.group(1)}"
    oa_url = (work.get("open_access") or {}).get("oa_url")
    if oa_url:
        arxiv_url = re.search(r"arxiv\.org/(?:abs|pdf)/([0-9.]+)", oa_url, flags=re.IGNORECASE)
        if arxiv_url:
            return f"https://arxiv.org/abs/{arxiv_url.group(1)}"
        return oa_url.replace("http://", "https://")
    if doi:
        return doi.replace("http://", "https://")
    primary = work.get("primary_location") or {}
    if primary.get("landing_page_url"):
        return primary["landing_page_url"].replace("http://", "https://")
    return work.get("id", "https://openalex.org")


def discover_openalex(config: dict[str, Any], since: dt.date) -> Iterable[dict[str, Any]]:
    endpoint = "https://api.openalex.org/works"
    email = os.getenv("OPENALEX_EMAIL", "")
    for query in config["queries"]:
        params = {
            "search": query,
            "filter": f"from_publication_date:{since.isoformat()},to_publication_date:{dt.date.today().isoformat()}",
            "per-page": "100",
            "sort": "publication_date:desc",
            "select": "id,doi,display_name,publication_year,publication_date,type,ids,open_access,primary_location,locations,primary_topic,abstract_inverted_index",
        }
        if email:
            params["mailto"] = email
        url = f"{endpoint}?{urllib.parse.urlencode(params)}"
        payload = request_json(url)
        yield from payload.get("results", [])
        time.sleep(0.15)


def score_code_repo(title: str, repo: dict[str, Any]) -> float:
    name = normalize(repo.get("name", ""))
    description = normalize(repo.get("description") or "")
    full = f"{name} {description}"
    if any(word in full for word in ("awesome list", "paper list", "reading list")):
        return 0.0
    tokens = set(compact_title_tokens(title))
    if not tokens:
        return 0.0
    overlap = len(tokens & set(full.split())) / len(tokens)
    acronym = "".join(word[0] for word in normalize(title.split(":", 1)[0]).split())
    name_bonus = 0.35 if len(acronym) >= 3 and acronym in name.replace(" ", "") else 0.0
    return overlap + name_bonus


def discover_code(title: str, github_token: str | None) -> str | None:
    if not github_token:
        return None
    tokens = compact_title_tokens(title)[:7]
    if not tokens:
        return None
    query = " ".join(tokens) + " in:name,description,readme"
    params = urllib.parse.urlencode({"q": query, "sort": "stars", "per_page": 10})
    try:
        payload = request_json(
            f"https://api.github.com/search/repositories?{params}", github_token
        )
    except RuntimeError as exc:
        print(f"warning: code search skipped for {title!r}: {exc}", file=sys.stderr)
        return None
    ranked = sorted(
        ((score_code_repo(title, repo), repo) for repo in payload.get("items", [])),
        reverse=True,
        key=lambda item: item[0],
    )
    if ranked and ranked[0][0] >= 0.58:
        return ranked[0][1].get("html_url")
    return None


def make_record(work: dict[str, Any], venue: str, github_token: str | None) -> dict[str, Any]:
    title = work.get("display_name") or work.get("title") or "Untitled"
    return {
        "title": title.strip(),
        "year": int(work["publication_year"]),
        "publication_date": work.get("publication_date"),
        "venue": venue,
        "category": classify_paper(title),
        "paper_url": best_paper_url(work),
        "code_url": discover_code(title, github_token),
        "openalex_id": work.get("id"),
        "added_at": dt.date.today().isoformat(),
        "curated": False,
    }


def github_search_url(title: str) -> str:
    query = urllib.parse.quote(f'"{title}"')
    return f"https://github.com/search?q={query}&type=repositories"


def render_readme(papers: list[dict[str, Any]], config: dict[str, Any]) -> str:
    papers = sorted(papers, key=lambda item: (-int(item["year"]), item["title"].lower()))
    by_category: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for paper in papers:
        by_category[paper["category"]].append(paper)
    venues = Counter(paper["venue"] for paper in papers)
    years = sorted({int(paper["year"]) for paper in papers})
    last_added = max((paper.get("added_at", "") for paper in papers), default="") or "2026-08-03"
    reference_count = sum(
        paper.get("source_repo") == "chicleee/End-to-End-3D-Reconstruction-Paper-List"
        for paper in papers
    )
    repository = config.get("repository", "Alleor/3D-reconstruction-paper")
    workflow_url = f"https://github.com/{repository}/actions/workflows/update-papers.yml"
    lines = [
        "# Awesome 3D Reconstruction Papers",
        "",
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        f"[![Auto Update]({workflow_url}/badge.svg)]({workflow_url})",
        "![Papers](https://img.shields.io/badge/papers-{}-blue)".format(len(papers)),
        "",
        "A curated, automatically updated list of recent papers on 3D reconstruction.",
        "收录近五年三维重建论文，并自动发现新论文及其开源代码。",
        "",
        f"> Coverage: {min(years) if years else '—'}–{max(years) if years else '—'} · Last content update: {last_added} · Maintainer: [@Alleor](https://github.com/Alleor)",
        "",
        "## About / 项目简介",
        "",
        "这是一个面向三维视觉研究者和开发者的开源论文库，持续整理近五年来三维重建领域的重要工作。仓库覆盖主流会议、期刊与 arXiv，提供论文和官方代码链接，并通过 GitHub Actions 每周自动发现、筛选、去重、分类和更新最新文献。",
        "",
        "An open-source paper collection for 3D vision researchers and developers, continuously tracking important 3D reconstruction work from the most recent five years. It covers major conferences, journals, and arXiv, provides paper and official-code links, and uses GitHub Actions to discover, filter, deduplicate, classify, and update the collection every week.",
        "",
        "### Highlights / 项目亮点",
        "",
        "- 📚 Mutually exclusive task categories / 清晰且互不重叠的任务分类",
        "- 📄 Paper and official-code links / 论文与官方代码链接",
        "- 🔄 Automatic weekly updates / 每周自动更新",
        "- 🔍 Automatic discovery, filtering, and deduplication / 自动发现、筛选与去重",
        "- 📅 Rolling five-year coverage / 持续覆盖近五年研究成果",
        "",
        "### Research Areas / 研究分类",
        "",
        "| # | 中文分类 | English Category |",
        "|--:|:--|:--|",
    ]
    for index, category in enumerate(CATEGORY_ORDER, start=1):
        lines.append(f"| {index} | {CATEGORY_NAMES_ZH[category]} | {category} |")
    lines.extend([
        "",
        "If this repository helps your research, literature review, or project development, please consider giving it a ⭐ **Star**. Issues and pull requests are always welcome!",
        "",
        "如果这个仓库对你的科研、文献调研或项目开发有所帮助，欢迎点一个 ⭐ **Star**，也欢迎通过 Issue 或 Pull Request 推荐论文、补充代码和修正信息！",
        "",
        "## Scope",
        "",
        "Primary discovery venues: " + ", ".join(config["venues"]) + ". The rolling five-year window is based on publication date. The complete reference list is also mirrored, so its additional venues are preserved. Papers without a confidently matched official implementation are marked **Code pending**.",
        "",
        "## Contents",
        "",
    ])
    for category in CATEGORY_ORDER:
        if by_category.get(category):
            anchor = re.sub(r"[^a-z0-9 -]", "", category.lower()).replace(" ", "-")
            lines.append(f"- [{category}](#{anchor})")
    lines.extend([
        "",
        "## Taxonomy",
        "",
        "Categories are mutually exclusive and follow each paper's primary task. Method properties such as self-supervision, efficiency, or scalability do not create duplicate categories.",
        "",
        "| Category | Scope | Papers |",
        "|:--|:--|--:|",
    ])
    for category in CATEGORY_ORDER:
        anchor = re.sub(r"[^a-z0-9 -]", "", category.lower()).replace(" ", "-")
        lines.append(
            f"| [{category}](#{anchor}) | {CATEGORY_DESCRIPTIONS[category]} | "
            f"{len(by_category.get(category, []))} |"
        )
    lines.extend(["", "## Venue coverage", "", "| Venue | Papers |", "|:--|--:|"])
    venue_order = config["venues"] + sorted(set(venues) - set(config["venues"]))
    for venue in venue_order:
        if venues.get(venue):
            lines.append(f"| {venue} | {venues[venue]} |")
    for category in CATEGORY_ORDER:
        entries = by_category.get(category, [])
        if not entries:
            continue
        lines.extend(["", f"## {category}", ""])
        for paper in entries:
            paper_link = f"[Paper]({paper['paper_url']})"
            if paper.get("code_url"):
                code = f"[Code]({paper['code_url']})"
            else:
                code = f"**Code pending** ([search]({github_search_url(paper['title'])}))"
            lines.append(
                f"- **{paper['title']}** — *{paper['venue']} {paper['year']}* "
                f"{paper_link} · {code}"
            )
    lines.extend([
        "",
        "## Automatic updates",
        "",
        "A scheduled GitHub Action runs every Monday. It first synchronizes the reference repository, then queries OpenAlex for additional papers, applies the rolling five-year filter, deduplicates records, searches GitHub for likely official implementations, and regenerates this README. The workflow can also be run manually from the Actions tab.",
        "",
        "To run locally:",
        "",
        "```bash",
        "python scripts/update_papers.py --render-only",
        "python scripts/update_papers.py --dry-run",
        "python scripts/update_papers.py",
        "```",
        "",
        "Set `GITHUB_TOKEN` to enable code-repository discovery and optionally set `OPENALEX_EMAIL` for the OpenAlex polite pool.",
        "",
        "## Contributing",
        "",
        "Corrections and missing papers are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and open a pull request or issue.",
        "",
        "## Acknowledgements",
        "",
        f"This repository mirrors {reference_count} entries and their original categories from [End-to-End-3D-Reconstruction-Paper-List](https://github.com/chicleee/End-to-End-3D-Reconstruction-Paper-List). Metadata discovery for additional papers uses [OpenAlex](https://openalex.org/).",
        "",
        "## License",
        "",
        "MIT",
        "",
    ])
    return "\n".join(lines)


def merge_discovered(
    papers: list[dict[str, Any]],
    works: Iterable[dict[str, Any]],
    config: dict[str, Any],
    github_token: str | None,
) -> tuple[list[dict[str, Any]], int]:
    known_titles = {title_key(paper["title"]) for paper in papers}
    known_ids = {paper.get("openalex_id") for paper in papers if paper.get("openalex_id")}
    allowed_venues = set(config["venues"])
    candidates: list[dict[str, Any]] = []
    seen_work_ids: set[str] = set()
    for work in works:
        work_id = work.get("id", "")
        if work_id in seen_work_ids or work_id in known_ids:
            continue
        seen_work_ids.add(work_id)
        venue = detect_venue(work)
        title = work.get("display_name") or work.get("title") or ""
        if venue not in allowed_venues or title_key(title) in known_titles or not is_relevant(work):
            continue
        candidates.append(make_record(work, venue, github_token))
        known_titles.add(title_key(title))
    candidates.sort(key=lambda item: (-item["year"], item["title"].lower()))
    limit = int(config.get("max_new_papers_per_run", 30))
    selected = candidates[:limit]
    return papers + selected, len(selected)


def prune_rolling_window(papers: list[dict[str, Any]], since: dt.date) -> list[dict[str, Any]]:
    # Curated boundary-year records are retained because venue metadata often has
    # only year precision; discovered records use their publication year.
    kept = []
    for paper in papers:
        published = paper.get("publication_date")
        if published:
            try:
                if dt.date.fromisoformat(published) >= since:
                    kept.append(paper)
                continue
            except ValueError:
                pass
        if int(paper["year"]) >= since.year:
            kept.append(paper)
    return kept


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--render-only", action="store_true", help="do not access the network")
    parser.add_argument("--dry-run", action="store_true", help="print changes without writing")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = load_json(CONFIG_FILE)
    papers = load_json(DATA_FILE)
    today = dt.date.today()
    since = today - dt.timedelta(days=365 * int(config.get("rolling_years", 5)))
    papers = prune_rolling_window(papers, since)
    added = 0
    if not args.render_only:
        works = discover_openalex(config, since)
        papers, added = merge_discovered(
            papers, works, config, os.getenv("GITHUB_TOKEN")
        )
    reclassify_papers(papers)
    papers.sort(key=lambda item: (-int(item["year"]), item["title"].lower()))
    readme = render_readme(papers, config)
    if args.dry_run:
        print(f"Would keep {len(papers)} papers and add {added} new papers.")
        return 0
    DATA_FILE.write_text(json.dumps(papers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    README_FILE.write_text(readme, encoding="utf-8")
    print(f"Kept {len(papers)} papers; added {added}; rendered {README_FILE.name}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
