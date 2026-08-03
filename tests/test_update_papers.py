import datetime as dt
import importlib.util
import json
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
SPEC = importlib.util.spec_from_file_location(
    "update_papers", ROOT / "scripts" / "update_papers.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

IMPORT_SPEC = importlib.util.spec_from_file_location(
    "import_reference", ROOT / "scripts" / "import_reference.py"
)
IMPORT_MODULE = importlib.util.module_from_spec(IMPORT_SPEC)
assert IMPORT_SPEC.loader
sys.modules[IMPORT_SPEC.name] = IMPORT_MODULE
IMPORT_SPEC.loader.exec_module(IMPORT_MODULE)

TIMELINE_SPEC = importlib.util.spec_from_file_location(
    "generate_timeline", ROOT / "scripts" / "generate_timeline.py"
)
TIMELINE_MODULE = importlib.util.module_from_spec(TIMELINE_SPEC)
assert TIMELINE_SPEC.loader
sys.modules[TIMELINE_SPEC.name] = TIMELINE_MODULE
TIMELINE_SPEC.loader.exec_module(TIMELINE_MODULE)


class PaperListTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.papers = json.loads((ROOT / "data" / "papers.json").read_text())
        cls.honors = json.loads((ROOT / "data" / "honors.json").read_text())
        cls.config = json.loads((ROOT / "config.json").read_text())

    def test_unique_titles(self):
        keys = [MODULE.title_key(paper["title"]) for paper in self.papers]
        self.assertEqual(len(keys), len(set(keys)))

    def test_required_fields_and_urls(self):
        required = {"title", "year", "venue", "category", "paper_url", "code_url"}
        for paper in self.papers:
            self.assertTrue(required <= paper.keys(), paper.get("title"))
            self.assertIn(paper["category"], MODULE.CATEGORY_ORDER)
            self.assertTrue(paper["paper_url"].startswith("https://"))
            if paper["code_url"]:
                self.assertTrue(paper["code_url"].startswith("https://"))

    def test_all_requested_venues_are_represented(self):
        represented = {paper["venue"] for paper in self.papers}
        self.assertTrue(set(self.config["venues"]) <= represented)

    def test_coverage_starts_in_2021(self):
        self.assertEqual(self.config["start_year"], 2021)
        self.assertTrue(all(paper["year"] >= 2021 for paper in self.papers))

    def test_pruning_uses_a_fixed_2021_boundary(self):
        sample = [
            {"title": "Old by year", "year": 2020},
            {"title": "Boundary by year", "year": 2021},
            {
                "title": "Old by date",
                "year": 2021,
                "publication_date": "2020-12-31",
            },
            {
                "title": "Boundary by date",
                "year": 2021,
                "publication_date": "2021-01-01",
            },
        ]
        kept = MODULE.prune_before_start(sample, dt.date(2021, 1, 1))
        self.assertEqual(
            {paper["title"] for paper in kept},
            {"Boundary by year", "Boundary by date"},
        )

    def test_readme_is_reproducible(self):
        expected = MODULE.render_readme(self.papers, self.config)
        self.assertEqual((ROOT / "README.md").read_text(), expected)

    def test_timeline_is_reproducible_and_contains_every_paper(self):
        expected_svg = TIMELINE_MODULE.render_timeline_svg(self.papers, self.honors)
        expected_markdown = TIMELINE_MODULE.render_timeline_markdown(
            self.papers, self.config
        )
        self.assertEqual((ROOT / "assets" / "timeline.svg").read_text(), expected_svg)
        self.assertEqual((ROOT / "TIMELINE.md").read_text(), expected_markdown)

        root = ET.fromstring(expected_svg)
        rendered_titles = {
            node.attrib["data-title"]
            for node in root.findall(".//{http://www.w3.org/2000/svg}g")
            if node.attrib.get("class") == "paper"
        }
        self.assertEqual(rendered_titles, {paper["title"] for paper in self.papers})

    def test_honors_are_valid_and_rendered(self):
        paper_titles = {MODULE.title_key(paper["title"]) for paper in self.papers}
        honor_keys = set()
        readme = (ROOT / "README.md").read_text()
        for honor in self.honors:
            self.assertEqual(set(honor), {"title", "label", "url"})
            self.assertIn(MODULE.title_key(honor["title"]), paper_titles)
            self.assertTrue(honor["url"].startswith("https://"))
            key = (MODULE.title_key(honor["title"]), honor["label"])
            self.assertNotIn(key, honor_keys)
            honor_keys.add(key)
            self.assertIn(f"[{honor['label']}]({honor['url']})", readme)

    def test_all_taxonomy_categories_are_represented(self):
        represented = {paper["category"] for paper in self.papers}
        self.assertEqual(represented, set(MODULE.CATEGORY_ORDER))

    def test_category_counts_cover_every_paper_once(self):
        counts = {
            category: sum(paper["category"] == category for paper in self.papers)
            for category in MODULE.CATEGORY_ORDER
        }
        self.assertEqual(sum(counts.values()), len(self.papers))

    def test_reference_entries_have_provenance(self):
        imported = [
            paper for paper in self.papers
            if paper.get("source_repo") == IMPORT_MODULE.REFERENCE_REPO
        ]
        self.assertEqual(len(imported), 90)
        self.assertTrue(all(paper.get("source_category") for paper in imported))
        source_categories = {paper["source_category"] for paper in imported}
        self.assertEqual(source_categories, set(IMPORT_MODULE.REFERENCE_CATEGORIES))

    def test_reference_parser(self):
        sample = """## Dynamic
* Example 4D Paper [[CVPR 2026](https://arxiv.org/pdf/2601.12345?)] [[code](https://github.com/example/code)]
"""
        parsed = IMPORT_MODULE.parse_reference(sample)
        self.assertEqual(len(parsed), 1)
        self.assertEqual(parsed[0]["category"], "Dynamic & 4D Reconstruction")
        self.assertEqual(parsed[0]["source_category"], "Dynamic")
        self.assertEqual(parsed[0]["paper_url"], "https://arxiv.org/abs/2601.12345")

    def test_taxonomy_resolves_overlapping_signals_by_primary_task(self):
        cases = {
            "Semantic Gaussian Splatting for Panoptic Reconstruction": "Semantic 3D Reconstruction",
            "Dynamic 4D Gaussian Splatting": "Dynamic & 4D Reconstruction",
            "Gaussian-SLAM for Online Mapping": "SLAM, Robotics & Mapping",
            "Gaussian Head Avatars from One Image": "Object, Human & 3D Generation",
            "Static 3D Gaussian Splatting": "Gaussian Splatting",
            "Neural Radiance Fields for Novel View Synthesis": "NeRF & Novel View Synthesis",
            "High-Fidelity Neural Surface Reconstruction": "Dense Depth, Surface & Mesh Reconstruction",
            "Scalable Long-Context Feed-Forward 3D Reconstruction": "Feed-Forward Geometry & Foundation Models",
            "Streaming 4D Visual Geometry Transformer": "Dynamic & 4D Reconstruction",
            "Visual Geometry Grounded Transformer": "Feed-Forward Geometry & Foundation Models",
        }
        for title, expected in cases.items():
            with self.subTest(title=title):
                self.assertEqual(MODULE.classify_paper(title), expected)

    def test_false_positive_filters(self):
        base = {
            "primary_topic": {"subfield": {"display_name": "Computer Vision and Pattern Recognition"}},
            "abstract_inverted_index": {"3D": [0], "reconstruction": [1]},
        }
        for title in (
            "Prompt-Driven Surgical Concept Segmentation",
            "Gaussian Splatting Scene Quality Assessment",
            "Feed-Forward Gaussian Splatting Compression",
        ):
            self.assertFalse(MODULE.is_relevant({**base, "title": title}))

    def test_true_positive_filter(self):
        work = {
            "title": "Multi-Agent Feed-forward 3D Reconstruction from RGB Videos",
            "primary_topic": {"subfield": {"display_name": "Computer Vision and Pattern Recognition"}},
        }
        self.assertTrue(MODULE.is_relevant(work))


if __name__ == "__main__":
    unittest.main()
