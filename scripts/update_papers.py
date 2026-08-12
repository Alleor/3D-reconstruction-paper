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
import xml.etree.ElementTree as ET
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
from generate_timeline import render_timeline_markdown, render_timeline_svg


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "papers.json"
HONORS_FILE = ROOT / "data" / "honors.json"
CONFIG_FILE = ROOT / "config.json"
README_FILE = ROOT / "README.md"
TIMELINE_FILE = ROOT / "TIMELINE.md"
TIMELINE_SVG_FILE = ROOT / "assets" / "timeline.svg"

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
    "medical imaging", "nanomaterial", "crystallographic", "natural discharge",
    "surface temperature", "intraoperative", "multipath", "alloy",
}

PURE_TASK_TERMS = {
    "segmentation", "compression", "quality assessment", "scene quality",
    "action manipulation", "text to 3d generation", "text to 4dgs generation",
    "camera pose estimation", "visual localization", "camera calibration",
    "label transfer", "language gaussian", "mobile manipulation", "reasoning",
    "restoration", "distillation", "primitive merging",
    "exploratory study", "autonomous driving testing", "object selection",
    "beamforming", "rainfall synthesis",
    "world model", "world models", "latent action", "latent actions",
}

RELEVANCE_TERMS = {
    "3d reconstruction", "surface reconstruction", "scene reconstruction",
    "shape reconstruction", "dense mapping", "neural rendering",
    "novel view synthesis", "radiance field", "gaussian splatting",
    "multi-view stereo", "multiview stereo", "view synthesis", "neural implicit surface",
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


def contains_phrase(text: str, terms: Iterable[str]) -> bool:
    padded = f" {normalize(text)} "
    return any(f" {normalize(term)} " in padded for term in terms)


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
    work_title = work.get("display_name") or work.get("title") or ""
    text = normalize(f"{work_title} {abstract}")
    if contains_phrase(text, EXCLUDE_TERMS):
        return False
    title = normalize(work_title)
    if contains_phrase(title, PURE_TASK_TERMS) and "reconstruct" not in title:
        return False
    explicit = contains_phrase(title, RELEVANCE_TERMS)
    topic = work.get("primary_topic") or {}
    subfield = normalize((topic.get("subfield") or {}).get("display_name", ""))
    cv_topic = "computer vision" in subfield
    contextual = contains_phrase(text, RELEVANCE_TERMS)
    title_signal = contains_phrase(
        title,
        (
            "3d", "4d", "gs", "geometry", "geometric", "gaussian", "radiance",
            "novel view", "view synthesis", "surface", "scene", "mesh", "avatar",
            "object", "slam",
        ),
    )
    reconstruction_signal = "reconstruct" in title and title_signal
    return explicit or (cv_topic and title_signal and (contextual or reconstruction_signal))


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


def abstract_index(text: str) -> dict[str, list[int]]:
    index: dict[str, list[int]] = defaultdict(list)
    for position, word in enumerate(text.split()):
        index[word].append(position)
    return dict(index)


def author_link_from_abstract(abstract: str) -> str | None:
    urls = [
        url.rstrip(".,;:!?)\\]}>'\"")
        for url in re.findall(r"https?://[^\s<]+", abstract)
    ]
    external = [url for url in urls if "arxiv.org" not in url.lower()]
    github = next((url for url in external if "github.com" in url.lower()), None)
    return github or (external[0] if external else None)


def parse_arxiv_feed(xml_text: str) -> list[dict[str, Any]]:
    namespace = {"atom": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml_text)
    works: list[dict[str, Any]] = []
    for entry in root.findall("atom:entry", namespace):
        title = " ".join((entry.findtext("atom:title", "", namespace)).split())
        abstract = " ".join((entry.findtext("atom:summary", "", namespace)).split())
        published = entry.findtext("atom:published", "", namespace)[:10]
        raw_id = entry.findtext("atom:id", "", namespace)
        arxiv_match = re.search(r"/abs/([^v]+)(?:v\d+)?$", raw_id)
        if not title or not published or not arxiv_match:
            continue
        arxiv_id = arxiv_match.group(1)
        works.append(
            {
                "id": f"https://arxiv.org/abs/{arxiv_id}",
                "display_name": title,
                "publication_year": int(published[:4]),
                "publication_date": published,
                "type": "preprint",
                "ids": {"arxiv": f"https://arxiv.org/abs/{arxiv_id}"},
                "locations": [{"raw_source_name": "arXiv"}],
                "primary_topic": {
                    "subfield": {"display_name": "Computer Vision and Pattern Recognition"}
                },
                "abstract_inverted_index": abstract_index(abstract),
                "code_url": author_link_from_abstract(abstract),
                "discovery_source": "arXiv API",
            }
        )
    return works


def discover_arxiv(config: dict[str, Any], today: dt.date) -> list[dict[str, Any]]:
    lookback_days = int(config.get("arxiv_lookback_days", 8))
    start = today - dt.timedelta(days=lookback_days)
    terms = (
        'all:"3D reconstruction" OR all:"novel view synthesis" OR '
        'all:"Gaussian splatting" OR all:"surface reconstruction" OR '
        'all:"dense SLAM"'
    )
    query = (
        f"cat:cs.CV AND submittedDate:[{start:%Y%m%d}0000 TO {today:%Y%m%d}2359] "
        f"AND ({terms})"
    )
    params = urllib.parse.urlencode(
        {
            "search_query": query,
            "start": "0",
            "max_results": "100",
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    request = urllib.request.Request(
        f"https://export.arxiv.org/api/query?{params}",
        headers={"User-Agent": "Alleor-3D-reconstruction-paper/1.0"},
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return parse_arxiv_feed(response.read().decode("utf-8"))
        except (urllib.error.URLError, TimeoutError, UnicodeDecodeError, ET.ParseError) as exc:
            if attempt == 2:
                raise RuntimeError(f"arXiv discovery failed: {exc}") from exc
            time.sleep(2**attempt)
    raise AssertionError("unreachable")


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
    record = {
        "title": title.strip(),
        "year": int(work["publication_year"]),
        "publication_date": work.get("publication_date"),
        "venue": venue,
        "category": classify_paper(title),
        "paper_url": best_paper_url(work),
        "code_url": work.get("code_url") or discover_code(title, github_token),
        "added_at": dt.date.today().isoformat(),
        "curated": False,
    }
    work_id = work.get("id", "")
    if "openalex.org" in work_id:
        record["openalex_id"] = work_id
    elif "arxiv.org" in work_id:
        record["arxiv_id"] = work_id
    if work.get("discovery_source"):
        record["discovery_source"] = work["discovery_source"]
    return record


def github_search_url(title: str) -> str:
    query = urllib.parse.quote(f'"{title}"')
    return f"https://github.com/search?q={query}&type=repositories"


def render_readme(
    papers: list[dict[str, Any]],
    config: dict[str, Any],
    honors: list[dict[str, str]] | None = None,
) -> str:
    honors = honors if honors is not None else load_json(HONORS_FILE)
    honors_by_title: dict[str, list[dict[str, str]]] = defaultdict(list)
    for honor in honors:
        honors_by_title[title_key(honor["title"])].append(honor)
    papers = sorted(papers, key=lambda item: (-int(item["year"]), item["title"].lower()))
    by_category: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for paper in papers:
        by_category[paper["category"]].append(paper)
    venues = Counter(paper["venue"] for paper in papers)
    years = sorted({int(paper["year"]) for paper in papers})
    last_added = max(
        (
            max(paper.get("added_at", ""), paper.get("reference_synced_at", ""))
            for paper in papers
        ),
        default="",
    ) or "2026-08-03"
    reference_count = sum(
        paper.get("source_repo") == "chicleee/End-to-End-3D-Reconstruction-Paper-List"
        for paper in papers
    )
    repository = config.get("repository", "Alleor/3D-reconstruction-paper")
    start_year = int(config.get("start_year", 2021))
    workflow_url = f"https://github.com/{repository}/actions/workflows/update-papers.yml"
    lines = [
        "# Awesome 3D Reconstruction Papers",
        "",
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        f"[![Auto Update]({workflow_url}/badge.svg)]({workflow_url})",
        "![Papers](https://img.shields.io/badge/papers-{}-blue)".format(len(papers)),
        "",
        "A curated, automatically updated list of recent papers on 3D reconstruction.",
        f"收录 {start_year} 年至今的三维重建论文，并自动发现新论文及其开源代码。",
        "",
        f"> Coverage: {start_year}–Present · Last content update: {last_added} · Maintainer: [@Alleor](https://github.com/Alleor)",
        "",
        "## About / 项目简介",
        "",
        f"这是一个面向三维视觉研究者和开发者的开源论文库，持续整理 {start_year} 年至今三维重建领域的重要工作。仓库覆盖主流会议、期刊与 arXiv，提供论文、官方代码和荣誉链接，并通过 GitHub Actions 每周自动发现、筛选、去重、分类和更新最新文献。",
        "",
        f"An open-source paper collection for 3D vision researchers and developers, continuously tracking important 3D reconstruction work published since {start_year}. It covers major conferences, journals, and arXiv, provides paper, official-code, and honor links, and uses GitHub Actions to discover, filter, deduplicate, classify, and update the collection every week.",
        "",
        "### Highlights / 项目亮点",
        "",
        "- 📚 Mutually exclusive task categories / 清晰且互不重叠的任务分类",
        "- 📄 Paper and official-code links / 论文与官方代码链接",
        "- 🏆 Verified paper awards and distinctions / 经官方来源核实的论文奖项与荣誉",
        "- 📈 Visual development timeline / 可视化三维重建发展时间线",
        "- 🔄 Automatic weekly updates / 每周自动更新",
        "- 🔍 Automatic discovery, filtering, and deduplication / 自动发现、筛选与去重",
        f"- 📅 Coverage since {start_year} / 持续覆盖 {start_year} 年至今的研究成果",
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
        "Primary discovery venues: " + ", ".join(config["venues"]) + f". Coverage starts on January 1, {start_year} and continues to the present. The complete reference list is also mirrored, so its additional venues are preserved. Papers without a confidently matched official implementation are marked **Code pending**. Honors are manually verified against official conference, journal, or author sources.",
        "",
        "## Development Timeline / 发展时间线",
        "",
        "Follow every paper along a central 2021–Present timeline, with papers alternating on both sides and colors showing the evolution of each research direction.",
        "",
        "沿一条 2021 年至今的主线浏览全部论文；论文交替排列在两侧，并通过分类颜色观察不同研究方向的发展趋势。",
        "",
        "### [Explore the full visual timeline → / 查看完整可视化时间线 →](TIMELINE.md)",
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
    paper_by_title = {title_key(paper["title"]): paper for paper in papers}
    lines.extend([
        "",
        "## Honors / 论文荣誉",
        "",
        "Verified paper awards and official highlight selections. Click an honor to open its source.",
        "",
        "| Paper | Honor |",
        "|:--|:--|",
    ])
    for honor in sorted(
        honors,
        key=lambda item: (
            -int(paper_by_title[title_key(item["title"])]["year"]),
            item["title"].lower(),
            item["label"].lower(),
        ),
    ):
        lines.append(
            f"| {honor['title']} | 🏆 [{honor['label']}]({honor['url']}) |"
        )
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
            details = [f"*{paper['venue']} {paper['year']}*"]
            details.extend(
                f"🏆 [{honor['label']}]({honor['url']})"
                for honor in honors_by_title.get(title_key(paper["title"]), [])
            )
            details.extend((paper_link, code))
            lines.append(f"- **{paper['title']}** — " + " · ".join(details))
    lines.extend([
        "",
        "## Automatic updates",
        "",
        f"A scheduled GitHub Action runs every Monday. It first synchronizes the reference repository, checks the latest arXiv submissions directly, then queries OpenAlex for additional papers published since {start_year}, deduplicates records, searches GitHub for likely official implementations, applies the taxonomy, preserves curated honors, and regenerates this README and the visual timeline. The workflow can also be run manually from the Actions tab.",
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
        f"This repository mirrors {reference_count} entries and their original categories from [End-to-End-3D-Reconstruction-Paper-List](https://github.com/chicleee/End-to-End-3D-Reconstruction-Paper-List). Metadata discovery for additional papers uses the [arXiv API](https://info.arxiv.org/help/api/) and [OpenAlex](https://openalex.org/).",
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
    known_ids = {
        paper[source_id]
        for paper in papers
        for source_id in ("openalex_id", "arxiv_id")
        if paper.get(source_id)
    }
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
    candidates.sort(
        key=lambda item: (
            item.get("publication_date") or f"{int(item['year']):04d}-01-01",
            item["title"].casefold(),
        ),
        reverse=True,
    )
    limit = int(config.get("max_new_papers_per_run", 30))
    selected = candidates[:limit]
    return papers + selected, len(selected)


def enrich_missing_codes(
    papers: list[dict[str, Any]],
    config: dict[str, Any],
    github_token: str | None,
) -> int:
    if not github_token:
        return 0
    candidates = sorted(
        (paper for paper in papers if not paper.get("code_url")),
        key=lambda item: (
            item.get("added_at") or item.get("reference_synced_at") or "",
            item.get("publication_date") or f"{int(item['year']):04d}-01-01",
        ),
        reverse=True,
    )
    updated = 0
    for paper in candidates[: int(config.get("max_code_searches_per_run", 20))]:
        code_url = discover_code(paper["title"], github_token)
        if code_url:
            paper["code_url"] = code_url
            updated += 1
    return updated


def prune_automatic_false_positives(
    papers: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], int]:
    kept: list[dict[str, Any]] = []
    removed = 0
    for paper in papers:
        title = paper.get("title", "")
        excluded_task = (
            contains_phrase(title, PURE_TASK_TERMS)
            and "reconstruct" not in normalize(title)
        )
        if paper.get("curated") is False and excluded_task:
            removed += 1
            continue
        kept.append(paper)
    return kept, removed


def prune_before_start(papers: list[dict[str, Any]], since: dt.date) -> list[dict[str, Any]]:
    # Boundary-year records are retained because curated venue metadata often
    # has only year precision.
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
    since = dt.date(int(config.get("start_year", 2021)), 1, 1)
    papers = prune_before_start(papers, since)
    papers, removed = prune_automatic_false_positives(papers)
    added = 0
    codes_added = 0
    if not args.render_only:
        github_token = os.getenv("GITHUB_TOKEN")
        codes_added = enrich_missing_codes(papers, config, github_token)
        works = [
            *discover_arxiv(config, dt.date.today()),
            *discover_openalex(config, since),
        ]
        papers, added = merge_discovered(
            papers, works, config, github_token
        )
    reclassify_papers(papers)
    papers.sort(key=lambda item: (-int(item["year"]), item["title"].lower()))
    readme = render_readme(papers, config)
    honors = load_json(HONORS_FILE)
    timeline = render_timeline_markdown(papers, config)
    timeline_svg = render_timeline_svg(papers, honors)
    if args.dry_run:
        print(
            f"Would keep {len(papers)} papers, add {added} new papers, "
            f"add {codes_added} code links, and remove {removed} automatic false positives."
        )
        return 0
    DATA_FILE.write_text(json.dumps(papers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    README_FILE.write_text(readme, encoding="utf-8")
    TIMELINE_FILE.write_text(timeline, encoding="utf-8")
    TIMELINE_SVG_FILE.parent.mkdir(parents=True, exist_ok=True)
    TIMELINE_SVG_FILE.write_text(timeline_svg, encoding="utf-8")
    print(
        f"Kept {len(papers)} papers; added {added}; added {codes_added} code links; "
        f"removed {removed} automatic false positives; rendered "
        f"{README_FILE.name}, {TIMELINE_FILE.name}, and {TIMELINE_SVG_FILE.relative_to(ROOT)}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
