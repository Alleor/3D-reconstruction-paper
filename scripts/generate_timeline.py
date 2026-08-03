"""Generate a GitHub-friendly visual timeline from the paper database."""

from __future__ import annotations

import json
import textwrap
from collections import Counter, defaultdict
from html import escape
from pathlib import Path
from typing import Any

from taxonomy import CATEGORY_NAMES_ZH, CATEGORY_ORDER


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "papers.json"
HONORS_FILE = ROOT / "data" / "honors.json"
CONFIG_FILE = ROOT / "config.json"
TIMELINE_FILE = ROOT / "TIMELINE.md"
TIMELINE_SVG_FILE = ROOT / "assets" / "timeline.svg"

CATEGORY_COLORS = {
    "Feed-Forward Geometry & Foundation Models": "#60A5FA",
    "Dense Depth, Surface & Mesh Reconstruction": "#2DD4BF",
    "NeRF & Novel View Synthesis": "#A78BFA",
    "Gaussian Splatting": "#F472B6",
    "Dynamic & 4D Reconstruction": "#FB923C",
    "Object, Human & 3D Generation": "#FACC15",
    "Semantic 3D Reconstruction": "#4ADE80",
    "SLAM, Robotics & Mapping": "#F87171",
}

CATEGORY_SHORT_NAMES = {
    "Feed-Forward Geometry & Foundation Models": "Feed-Forward Geometry",
    "Dense Depth, Surface & Mesh Reconstruction": "Dense Surface & Mesh",
    "NeRF & Novel View Synthesis": "NeRF & NVS",
    "Gaussian Splatting": "Gaussian Splatting",
    "Dynamic & 4D Reconstruction": "Dynamic & 4D",
    "Object, Human & 3D Generation": "Object, Human & Generation",
    "Semantic 3D Reconstruction": "Semantic Reconstruction",
    "SLAM, Robotics & Mapping": "SLAM & Mapping",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def title_key(title: str) -> str:
    return " ".join(title.casefold().split())


def wrap_title(title: str, width: int = 54) -> list[str]:
    return textwrap.wrap(
        title,
        width=width,
        break_long_words=False,
        break_on_hyphens=False,
    ) or [title]


def paper_sort_key(paper: dict[str, Any]) -> tuple[int, str, str]:
    year = int(paper["year"])
    published = paper.get("publication_date") or f"{year:04d}-07-01"
    return year, published, paper["title"].casefold()


def render_timeline_svg(
    papers: list[dict[str, Any]], honors: list[dict[str, str]]
) -> str:
    width = 1800
    center = width // 2
    card_width = 700
    left_x = 70
    right_x = width - left_x - card_width
    honor_by_title: dict[str, list[str]] = defaultdict(list)
    for honor in honors:
        honor_by_title[title_key(honor["title"])].append(honor["label"])

    grouped: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for paper in sorted(papers, key=paper_sort_key):
        grouped[int(paper["year"])].append(paper)

    elements: list[str] = []
    y = 300
    paper_index = 0
    for year in sorted(grouped):
        elements.extend(
            [
                f'<rect x="{center - 64}" y="{y}" width="128" height="52" rx="26" class="year"/>',
                f'<text x="{center}" y="{y + 35}" class="year-text" text-anchor="middle">{year}</text>',
            ]
        )
        y += 82
        for paper in grouped[year]:
            category = paper["category"]
            color = CATEGORY_COLORS[category]
            title_lines = wrap_title(paper["title"])
            paper_honors = honor_by_title.get(title_key(paper["title"]), [])
            card_height = 82 + 22 * len(title_lines) + (22 if paper_honors else 0)
            side = "left" if paper_index % 2 == 0 else "right"
            card_x = left_x if side == "left" else right_x
            card_edge = card_x + card_width if side == "left" else card_x
            node_y = y + card_height / 2
            paper_title = escape(paper["title"], quote=True)
            paper_url = escape(paper["paper_url"], quote=True)
            code_url = escape(paper.get("code_url") or "", quote=True)
            venue = escape(str(paper["venue"]))
            category_label = escape(CATEGORY_SHORT_NAMES[category])

            elements.extend(
                [
                    f'<g class="paper" data-title="{paper_title}">',
                    f'<line x1="{card_edge}" y1="{node_y:.1f}" x2="{center}" y2="{node_y:.1f}" class="connector"/>',
                    f'<circle cx="{center}" cy="{node_y:.1f}" r="9" fill="{color}" class="node"/>',
                    f'<rect x="{card_x}" y="{y}" width="{card_width}" height="{card_height}" rx="18" class="card" stroke="{color}"/>',
                    f'<rect x="{card_x}" y="{y}" width="8" height="{card_height}" rx="4" fill="{color}"/>',
                    f'<text x="{card_x + 28}" y="{y + 27}" class="meta" fill="{color}">{venue} {year}</text>',
                    f'<text x="{card_x + card_width - 24}" y="{y + 27}" class="category" text-anchor="end">{category_label}</text>',
                    f'<a href="{paper_url}" target="_blank">',
                ]
            )
            title_y = y + 56
            for line_index, line in enumerate(title_lines):
                elements.append(
                    f'<text x="{card_x + 28}" y="{title_y + 22 * line_index}" class="title">{escape(line)}</text>'
                )
            elements.append("</a>")
            info_y = title_y + 22 * len(title_lines)
            if paper_honors:
                label = " · ".join(paper_honors)
                elements.append(
                    f'<text x="{card_x + 28}" y="{info_y + 1}" class="honor">★ {escape(label)}</text>'
                )
                info_y += 22
            elements.extend(
                [
                    f'<a href="{paper_url}" target="_blank"><text x="{card_x + 28}" y="{info_y + 1}" class="link">PAPER ↗</text></a>',
                    (
                        f'<a href="{code_url}" target="_blank"><text x="{card_x + 122}" y="{info_y + 1}" class="link">CODE ↗</text></a>'
                        if code_url
                        else f'<text x="{card_x + 122}" y="{info_y + 1}" class="muted">CODE PENDING</text>'
                    ),
                    "</g>",
                ]
            )
            y += card_height + 22
            paper_index += 1
        y += 54

    height = y + 100
    legend = []
    for index, category in enumerate(CATEGORY_ORDER):
        column = index % 4
        row = index // 4
        legend_x = 110 + column * 420
        legend_y = 186 + row * 34
        color = CATEGORY_COLORS[category]
        legend.extend(
            [
                f'<circle cx="{legend_x}" cy="{legend_y - 5}" r="7" fill="{color}"/>',
                f'<text x="{legend_x + 18}" y="{legend_y}" class="legend">{escape(CATEGORY_SHORT_NAMES[category])}</text>',
            ]
        )

    svg = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">',
        '<title id="title">3D Reconstruction Paper Development Timeline</title>',
        f'<desc id="description">{len(papers)} papers from {min(grouped)} to {max(grouped)}, arranged around a central timeline and colored by research category.</desc>',
        "<style>",
        "text { font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }",
        ".background { fill: #0B1020; }",
        ".main-line { stroke: #64748B; stroke-width: 5; }",
        ".connector { stroke: #475569; stroke-width: 2; }",
        ".node { stroke: #E2E8F0; stroke-width: 3; }",
        ".card { fill: #121A2E; stroke-width: 2; }",
        ".title { fill: #F8FAFC; font-size: 20px; font-weight: 650; }",
        ".meta { font-size: 17px; font-weight: 750; }",
        ".category { fill: #CBD5E1; font-size: 15px; }",
        ".link { fill: #93C5FD; font-size: 14px; font-weight: 750; text-decoration: underline; }",
        ".muted { fill: #64748B; font-size: 13px; font-weight: 650; }",
        ".honor { fill: #FDE68A; font-size: 14px; font-weight: 700; }",
        ".year { fill: #E2E8F0; stroke: #0B1020; stroke-width: 6; }",
        ".year-text { fill: #0F172A; font-size: 25px; font-weight: 850; }",
        ".heading { fill: #F8FAFC; font-size: 38px; font-weight: 850; }",
        ".subheading { fill: #94A3B8; font-size: 18px; }",
        ".legend { fill: #CBD5E1; font-size: 15px; }",
        "</style>",
        f'<rect width="{width}" height="{height}" class="background"/>',
        f'<text x="{center}" y="70" class="heading" text-anchor="middle">3D Reconstruction · Development Timeline</text>',
        f'<text x="{center}" y="105" class="subheading" text-anchor="middle">{len(papers)} papers · {min(grouped)}–Present · oldest to newest · click PAPER or CODE</text>',
        *legend,
        f'<line x1="{center}" y1="260" x2="{center}" y2="{height - 55}" class="main-line"/>',
        *elements,
        f'<path d="M {center - 13} {height - 72} L {center} {height - 48} L {center + 13} {height - 72}" fill="#94A3B8"/>',
        "</svg>",
        "",
    ]
    return "\n".join(svg)


def render_timeline_markdown(
    papers: list[dict[str, Any]], config: dict[str, Any]
) -> str:
    years = list(range(int(config.get("start_year", 2021)), max(int(p["year"]) for p in papers) + 1))
    counts = Counter((paper["category"], int(paper["year"])) for paper in papers)
    repository = config.get("repository", "Alleor/3D-reconstruction-paper")
    raw_svg = f"https://raw.githubusercontent.com/{repository}/main/assets/timeline.svg"
    lines = [
        "# 3D Reconstruction Development Timeline / 三维重建发展时间线",
        "",
        "[← Back to the paper list / 返回论文列表](README.md)",
        "",
        f"> {len(papers)} papers from {years[0]} to the present. The central line runs from the earliest work at the top to the newest work at the bottom; cards alternate on both sides and colors represent the primary research direction.",
        "",
        f"> 共收录 {len(papers)} 篇论文。时间从上到下推进，论文交替分布在主线两侧，不同颜色对应不同研究方向。点击卡片中的 PAPER 或 CODE 可访问相关链接。",
        "",
        f"[Open full-size interactive SVG / 打开可点击的完整大图]({raw_svg})",
        "",
        "![3D Reconstruction Development Timeline](assets/timeline.svg)",
        "",
        "## Trend matrix / 趋势矩阵",
        "",
        "The counts below make changes in research activity easier to compare across years.",
        "",
        "| Research direction | " + " | ".join(map(str, years)) + " | Total |",
        "|:--|" + "--:|" * (len(years) + 1),
    ]
    for category in CATEGORY_ORDER:
        yearly = [counts[(category, year)] for year in years]
        lines.append(
            f"| {CATEGORY_NAMES_ZH[category]}<br>{category} | "
            + " | ".join(map(str, yearly))
            + f" | {sum(yearly)} |"
        )
    lines.extend(
        [
            "",
            "---",
            "",
            "This page and its SVG are regenerated automatically from `data/papers.json` during the weekly update.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    papers = load_json(DATA_FILE)
    honors = load_json(HONORS_FILE)
    config = load_json(CONFIG_FILE)
    TIMELINE_SVG_FILE.parent.mkdir(parents=True, exist_ok=True)
    TIMELINE_SVG_FILE.write_text(render_timeline_svg(papers, honors), encoding="utf-8")
    TIMELINE_FILE.write_text(render_timeline_markdown(papers, config), encoding="utf-8")
    print(f"Rendered {TIMELINE_FILE.name} and {TIMELINE_SVG_FILE.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
