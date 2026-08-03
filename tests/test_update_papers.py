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
                self.assertTrue(paper["code_url"].startswith("https://github.com/"))

    def test_all_requested_venues_are_represented(self):
        represented = {paper["venue"] for paper in self.papers}
        self.assertTrue(set(self.config["venues"]) <= represented)

    def test_readme_is_reproducible(self):
        expected = MODULE.render_readme(self.papers, self.config)
        self.assertEqual((ROOT / "README.md").read_text(), expected)

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
