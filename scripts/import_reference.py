#!/usr/bin/env python3
"""Synchronize paper entries from the reference end-to-end paper list."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "papers.json"
REFERENCE_REPO = "chicleee/End-to-End-3D-Reconstruction-Paper-List"
REFERENCE_URL = (
    "https://raw.githubusercontent.com/"
    "chicleee/End-to-End-3D-Reconstruction-Paper-List/main/README.md"
)
REFERENCE_CATEGORIES = [
    "3D Reconstruction",
    "Scalable",
    "Self-Supervised",
    "Semantic",
    "Dynamic",
    "Generation",
    "Novel View Synthesis",
]

ENTRY_RE = re.compile(
    r"^\*\s+(.*?)\s+\[\[([^\]]+)\]\(([^)]*)\)\]\s+"
    r"\[\[([^\]]*)\]\(([^)]*)\)\]\s*$"
)
VENUE_RE = re.compile(r"^(.*?)\s+((?:19|20)\d{2})$")


def normalize_title(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def canonical_url(url: str) -> str | None:
    url = url.strip().rstrip("?")
    if not url:
        return None
    url = url.replace("http://", "https://")
    arxiv = re.search(r"arxiv\.org/(?:pdf|abs)/([0-9.]+)(?:v\d+)?", url, re.I)
    if arxiv:
        return f"https://arxiv.org/abs/{arxiv.group(1).rstrip('.')}"
    return url


def parse_reference(markdown: str) -> list[dict[str, Any]]:
    category: str | None = None
    papers: list[dict[str, Any]] = []
    for line_number, raw_line in enumerate(markdown.splitlines(), start=1):
        line = raw_line.strip()
        if line.startswith("## "):
            heading = line[3:].strip()
            category = heading if heading in REFERENCE_CATEGORIES else None
            continue
        if not line.startswith("*") or category is None:
            continue
        match = ENTRY_RE.match(line)
        if not match:
            raise ValueError(f"cannot parse reference line {line_number}: {line}")
        title, publication, paper_url, _code_label, code_url = match.groups()
        title = title.replace(":globe_with_meridians:", "🌐").strip()
        venue_match = VENUE_RE.match(publication.strip())
        if not venue_match:
            raise ValueError(
                f"cannot parse venue/year on reference line {line_number}: {publication}"
            )
        venue, year = venue_match.groups()
        papers.append(
            {
                "title": title,
                "year": int(year),
                "venue": venue.strip(),
                "category": category,
                "paper_url": canonical_url(paper_url),
                "code_url": canonical_url(code_url),
                "curated": True,
                "source_repo": REFERENCE_REPO,
                "source_category": category,
            }
        )
    return papers


def fetch_reference(retries: int = 3) -> str:
    request = urllib.request.Request(
        REFERENCE_URL,
        headers={"User-Agent": "Alleor-3D-reconstruction-paper/1.0"},
    )
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                return response.read().decode("utf-8")
        except (urllib.error.URLError, TimeoutError, UnicodeDecodeError) as exc:
            if attempt == retries - 1:
                raise RuntimeError(f"failed to fetch {REFERENCE_URL}: {exc}") from exc
            time.sleep(2**attempt)
    raise AssertionError("unreachable")


def merge_papers(
    existing: list[dict[str, Any]], imported: list[dict[str, Any]]
) -> tuple[list[dict[str, Any]], int, int]:
    by_title = {normalize_title(paper["title"]): paper for paper in existing}
    added = 0
    updated = 0
    sync_date = dt.date.today().isoformat()
    for source_paper in imported:
        key = normalize_title(source_paper["title"])
        current = by_title.get(key)
        if current is None:
            current = dict(source_paper)
            current["reference_synced_at"] = sync_date
            existing.append(current)
            by_title[key] = current
            added += 1
            continue
        changed = False
        for field in (
            "year",
            "venue",
            "category",
            "paper_url",
            "source_repo",
            "source_category",
        ):
            value = source_paper[field]
            if current.get(field) != value:
                current[field] = value
                changed = True
        if source_paper.get("code_url") and current.get("code_url") != source_paper["code_url"]:
            current["code_url"] = source_paper["code_url"]
            changed = True
        if changed:
            current["reference_synced_at"] = sync_date
            updated += 1
    existing.sort(key=lambda item: (-int(item["year"]), item["title"].lower()))
    return existing, added, updated


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, help="read a local reference README")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    markdown = args.input.read_text(encoding="utf-8") if args.input else fetch_reference()
    imported = parse_reference(markdown)
    if not imported:
        raise RuntimeError("reference parser returned no papers")
    existing = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    merged, added, updated = merge_papers(existing, imported)
    if not args.dry_run:
        DATA_FILE.write_text(
            json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    print(
        f"Reference contains {len(imported)} papers; added {added}; "
        f"updated {updated}; total {len(merged)}."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
