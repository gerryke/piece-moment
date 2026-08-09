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

    def test_updated_store_images_are_localized_and_cache_busted(self):
        index = (ROOT / "index.html").read_text()
        app_js = (ROOT / "assets" / "app.js").read_text()
        self.assertIn('data-localized-ipad-shot="06"', index)
        self.assertIn('assets/app.js?v=13', index)
        self.assertIn("assets/img/shots/v113-ipad/", app_js)
        self.assertIn('lang !== "en" && shotNumber <= 3 ? 6 : 5', app_js)
        self.assertIn('01.jpg?v=5', index)
        self.assertNotIn('01.jpg?v=6', index)
        for locale in ("en", "zh", "zht", "ja"):
            for number in ("01", "02", "03", "04", "05", "06"):
                self.assertTrue((ROOT / f"assets/img/shots/v8/{locale}/{number}.jpg").is_file())
            self.assertTrue((ROOT / f"assets/img/shots/v113-ipad/{locale}/06.jpg").is_file())


if __name__ == "__main__":
    unittest.main()
