import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
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


class PaperListTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.papers = json.loads((ROOT / "data" / "papers.json").read_text())
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

    def test_readme_is_reproducible(self):
        expected = MODULE.render_readme(self.papers, self.config)
        self.assertEqual((ROOT / "README.md").read_text(), expected)

    def test_reference_categories_are_represented(self):
        represented = {paper["category"] for paper in self.papers}
        self.assertTrue(set(IMPORT_MODULE.REFERENCE_CATEGORIES) <= represented)

    def test_reference_entries_have_provenance(self):
        imported = [
            paper for paper in self.papers
            if paper.get("source_repo") == IMPORT_MODULE.REFERENCE_REPO
        ]
        self.assertEqual(len(imported), 90)
        self.assertTrue(all(paper.get("source_category") for paper in imported))

    def test_reference_parser(self):
        sample = """## Dynamic
* Example 4D Paper [[CVPR 2026](https://arxiv.org/pdf/2601.12345?)] [[code](https://github.com/example/code)]
"""
        parsed = IMPORT_MODULE.parse_reference(sample)
        self.assertEqual(len(parsed), 1)
        self.assertEqual(parsed[0]["category"], "Dynamic")
        self.assertEqual(parsed[0]["paper_url"], "https://arxiv.org/abs/2601.12345")

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
