import hashlib
import importlib.util
import os
import tempfile
import unittest
from pathlib import Path

from PIL import Image


WORKTREE_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = Path(os.environ.get("PIECEMARKET_ASSET_SOURCE_ROOT", "/Users/keyipeng/Dev/piecemarket"))
MODULE_PATH = WORKTREE_ROOT / "scripts" / "render_v113_store_assets.py"


def load_renderer():
    spec = importlib.util.spec_from_file_location("render_v113_store_assets", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


class V113StoreAssetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.renderer = load_renderer()
        cls.tempdir = tempfile.TemporaryDirectory()
        cls.output_root = Path(cls.tempdir.name)
        cls.renderer.render_all(cls.output_root)

    @classmethod
    def tearDownClass(cls):
        cls.tempdir.cleanup()

    def test_contract_has_ten_images_per_device(self):
        self.assertEqual(len(self.renderer.IPHONE_OUTPUT_FILES), 10)
        self.assertEqual(len(self.renderer.IPAD_OUTPUT_FILES), 10)
        self.assertEqual(len(set(self.renderer.IPHONE_OUTPUT_FILES)), 10)
        self.assertEqual(len(set(self.renderer.IPAD_OUTPUT_FILES)), 10)

    def test_all_outputs_have_app_store_dimensions(self):
        iphone_dir = self.output_root / self.renderer.IPHONE_RELATIVE_OUTPUT
        ipad_dir = self.output_root / self.renderer.IPAD_RELATIVE_OUTPUT
        for filename in self.renderer.IPHONE_OUTPUT_FILES:
            with Image.open(iphone_dir / filename) as image:
                self.assertEqual(image.size, (1320, 2868), filename)
        for filename in self.renderer.IPAD_OUTPUT_FILES:
            with Image.open(ipad_dir / filename) as image:
                self.assertEqual(image.size, (2064, 2752), filename)

    def test_locked_treatment_a_trio_is_byte_identical(self):
        self.assertEqual(self.renderer.LOCKED_DIR.name, "pieceful-independent-6.9")
        self.assertEqual(
            self.renderer.LOCKED_IPHONE_SOURCES[2].name,
            "03-move-pieces-together-dune-source.png",
        )
        iphone_dir = self.output_root / self.renderer.IPHONE_RELATIVE_OUTPUT
        for index, source in enumerate(self.renderer.LOCKED_IPHONE_SOURCES, start=1):
            self.assertEqual(
                sha256(source),
                sha256(iphone_dir / self.renderer.IPHONE_OUTPUT_FILES[index - 1]),
            )

    def test_iphone_positions_five_through_ten_are_byte_identical(self):
        iphone_dir = self.output_root / self.renderer.IPHONE_RELATIVE_OUTPUT
        for filename, source in zip(
            self.renderer.IPHONE_OUTPUT_FILES[4:],
            self.renderer.UNCHANGED_IPHONE_SOURCES,
        ):
            self.assertEqual(sha256(source), sha256(iphone_dir / filename))

    def test_only_ipad_position_six_changes(self):
        ipad_dir = self.output_root / self.renderer.IPAD_RELATIVE_OUTPUT
        source_dir = SOURCE_ROOT / "marketing-assets/next-version-prep/reorder/ipad-13-appstore"
        for index, filename in enumerate(self.renderer.IPAD_OUTPUT_FILES, start=1):
            if index == 6:
                self.assertNotEqual(sha256(source_dir / filename), sha256(ipad_dir / filename))
            else:
                self.assertEqual(sha256(source_dir / filename), sha256(ipad_dir / filename))

    def test_ipad_delivery_uses_the_ipad_completion_source(self):
        self.assertEqual(self.renderer.IPAD_COMPLETION_SOURCE.name, "3037.JPG")
        self.assertTrue(all(title.isascii() for title in self.renderer.TREATMENT_TITLES["en"]))
        self.assertTrue(self.renderer.IPAD_TITLE.isascii())

    def test_ipad_completion_source_is_localized_to_english(self):
        localize = getattr(self.renderer, "localize_ipad_completion", None)
        self.assertTrue(callable(localize), "renderer must localize the iPad completion source")
        if not callable(localize):
            return
        with Image.open(self.renderer.IPAD_COMPLETION_SOURCE) as opened:
            source = opened.convert("RGB")
        localized = localize()
        self.assertEqual(localized.size, source.size)
        self.assertNotEqual(
            localized.crop((350, 70, 1000, 155)).tobytes(),
            source.crop((350, 70, 1000, 155)).tobytes(),
        )
        self.assertNotEqual(
            localized.crop((320, 1230, 610, 1370)).tobytes(),
            source.crop((320, 1230, 610, 1370)).tobytes(),
        )
        localized.close()
        source.close()

    def test_treatment_a_trio_is_ready_for_four_languages(self):
        self.assertEqual(set(self.renderer.TREATMENT_TITLES), {"en", "zh", "zht", "ja"})
        self.assertTrue(all(len(titles) == 3 for titles in self.renderer.TREATMENT_TITLES.values()))

    def test_iphone_completion_uses_original_v8_style(self):
        self.assertEqual(
            getattr(self.renderer, "IPHONE_COMPLETION_STYLE", None),
            "original-v8",
        )

    def test_localized_update_contract_renders_four_languages(self):
        self.assertEqual(
            getattr(self.renderer, "LOCALES", None),
            ("en", "zh", "zht", "ja"),
        )
        render = getattr(self.renderer, "render_localized_updates", None)
        self.assertTrue(callable(render), "renderer must generate localized update images")
        if not callable(render):
            return
        render(self.output_root)
        for locale in self.renderer.LOCALES:
            iphone_dir = self.output_root / self.renderer.iphone_output_dir(locale)
            ipad_dir = self.output_root / self.renderer.ipad_output_dir(locale)
            for filename in self.renderer.IPHONE_OUTPUT_FILES[:4]:
                with Image.open(iphone_dir / filename) as image:
                    self.assertEqual(image.size, (1320, 2868), (locale, filename))
            with Image.open(ipad_dir / "06-finish-continue.png") as image:
                self.assertEqual(image.size, (2064, 2752), locale)

class RendererHelperTests(unittest.TestCase):
    def test_chinese_page_one_uses_approved_piece_wording(self):
        renderer = load_renderer()
        self.assertEqual(renderer.TREATMENT_COPY["zh"][0]["title"], ("全部碎片", "一目了然"))
        self.assertEqual(renderer.TREATMENT_COPY["zht"][0]["title"], ("全部碎片", "一目瞭然"))

    def test_localized_page_one_preserves_original_classic_play_badge(self):
        renderer = load_renderer()
        with tempfile.TemporaryDirectory() as tempdir:
            output = Path(tempdir) / "01.png"
            renderer.render_localized_treatment_poster(
                renderer.LOCKED_IPHONE_SOURCES[0],
                output,
                "zh",
                1,
            )
            badge_box = (35, 650, 760, 900)
            with Image.open(renderer.LOCKED_IPHONE_SOURCES[0]) as source:
                expected = source.convert("RGB").crop(badge_box)
            with Image.open(output) as localized:
                actual = localized.convert("RGB").crop(badge_box)
            self.assertEqual(actual.tobytes(), expected.tobytes())
            actual.close()
            expected.close()

    def test_dark_copy_removal_preserves_the_surrounding_gradient(self):
        renderer = load_renderer()
        erase = getattr(renderer, "erase_flattened_dark_copy", None)
        self.assertTrue(callable(erase), "renderer must remove dark copy without a flat patch")
        if not callable(erase):
            return
        source = Image.new("RGB", (120, 60))
        pixels = source.load()
        for y in range(source.height):
            for x in range(source.width):
                pixels[x, y] = (180 + x // 4, 205 + x // 8, 210 + y // 6)
        for x in range(40, 80):
            for y in range(20, 38):
                if (x + y) % 3:
                    pixels[x, y] = (45, 60, 65)
        outside_before = source.crop((0, 0, 30, 60)).tobytes()
        result = erase(source, ((35, 15, 85, 43),))
        self.assertEqual(result.crop((0, 0, 30, 60)).tobytes(), outside_before)
        center = result.crop((40, 20, 80, 38))
        self.assertGreater(center.getextrema()[0][0], 120)
        center.close()
        result.close()
        source.close()

    def test_box_gradient_repair_removes_copy_without_horizontal_streaks(self):
        renderer = load_renderer()
        erase = getattr(renderer, "erase_box_to_gradient", None)
        self.assertTrue(callable(erase), "renderer must rebuild smooth completion-card copy regions")
        if not callable(erase):
            return
        source = Image.new("RGB", (120, 60))
        pixels = source.load()
        for y in range(source.height):
            for x in range(source.width):
                pixels[x, y] = (180 + x // 4, 200 + x // 8, 210 + y // 6)
        for x in range(38, 82):
            for y in range(20, 38):
                if (x + y) % 3:
                    pixels[x, y] = (45, 60, 65)
        outside_before = source.crop((0, 0, 25, 60)).tobytes()
        result = erase(source, (30, 15, 90, 43), sample_left=10, sample_right=110)
        self.assertEqual(result.crop((0, 0, 25, 60)).tobytes(), outside_before)
        repaired = result.crop((38, 20, 82, 38))
        self.assertGreater(repaired.getextrema()[0][0], 120)
        repaired.close()
        result.close()
        source.close()


if __name__ == "__main__":
    unittest.main()
