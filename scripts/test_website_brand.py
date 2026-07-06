import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WEBSITE_TEXT_FILES = [
    ROOT / "index.html",
    ROOT / "privacy.html",
    ROOT / "zh.html",
    ROOT / "zht.html",
    ROOT / "ja.html",
    ROOT / "assets" / "app.js",
]


class WebsiteBrandTests(unittest.TestCase):
    def test_old_brand_is_absent_from_website_copy(self):
        for path in WEBSITE_TEXT_FILES:
            with self.subTest(path=path.name):
                self.assertNotIn("Piece Moment", path.read_text())

    def test_new_brand_is_present_on_home_and_privacy_pages(self):
        for name in ("index.html", "privacy.html"):
            with self.subTest(path=name):
                self.assertIn("Pieceful Moment", (ROOT / name).read_text())

    def test_social_pages_use_new_share_image(self):
        for name in ("index.html", "zh.html", "zht.html", "ja.html"):
            with self.subTest(path=name):
                self.assertIn("share-pieceful.jpg", (ROOT / name).read_text())


if __name__ == "__main__":
    unittest.main()
