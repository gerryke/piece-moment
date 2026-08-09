import math
import os
import shutil
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = Path(os.environ.get("PIECEMARKET_ASSET_SOURCE_ROOT", ROOT))
DOWNLOADS_ROOT = Path(os.environ.get("PIECEMARKET_DOWNLOADS_ROOT", "/Users/keyipeng/Downloads"))
FONTS = ROOT / "marketing-assets/next-version-prep/fonts"

IPHONE_RELATIVE_OUTPUT = Path(
    "marketing-assets/next-version-prep/drafts/iphone-6.9-en/v1.1.3-treatment-a"
)
IPAD_RELATIVE_OUTPUT = Path("marketing-assets/next-version-prep/drafts/ipad-13-en/v1.1.3")

IPHONE_W, IPHONE_H = 1320, 2868
IPAD_W, IPAD_H = 2064, 2752

GREEN = (15, 70, 58)
MUTED = (102, 138, 128)
TREATMENT_BG = (239, 244, 239)
IPAD_PAPER = (250, 250, 246)
IPAD_MIST = (233, 240, 245)
IPAD_INK = (44, 49, 56)
IPAD_SOFT = (86, 93, 102)

TITLE_FONT = FONTS / "Fraunces-400.ttf"
TITLE_LIGHT = FONTS / "Fraunces-300.ttf"
TITLE_ITALIC = FONTS / "Fraunces-Italic-300.ttf"
BODY_FONT = FONTS / "HankenGrotesk-400.ttf"
CJK_SERIF = Path("/System/Library/Fonts/Supplemental/Songti.ttc")
JA_SERIF = Path("/System/Library/Fonts/ヒラギノ明朝 ProN.ttc")
JA_SANS = Path("/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc")

LOCALES = ("en", "zh", "zht", "ja")

LOCKED_DIR = SOURCE_ROOT / "marketing-assets/app-store-candidates/pieceful-independent-6.9"
LOCKED_IPHONE_SOURCES = [
    LOCKED_DIR / "01-every-piece-in-view-1320x2868.png",
    LOCKED_DIR / "02-build-outside-the-board-1320x2868.png",
    LOCKED_DIR / "03-move-pieces-together-dune-source.png",
]

V8_DIR = SOURCE_ROOT / "marketing-assets/next-version-prep/drafts/iphone-6.9-en/v8"
UNCHANGED_IPHONE_SOURCES = [
    V8_DIR / "05-for-every-mood.png",
    V8_DIR / "06-made-for-little-pauses.png",
    V8_DIR / "07-photos-become-puzzles.png",
    V8_DIR / "08-hide-a-note-inside.png",
    V8_DIR / "09-piece-together-a-memory.png",
    V8_DIR / "10-no-rush-to-finish.png",
]

COMPLETION_SOURCE = DOWNLOADS_ROOT / "100091.JPG"
IPAD_COMPLETION_SOURCE = DOWNLOADS_ROOT / "3037.JPG"
IPAD_SOURCE_DIR = SOURCE_ROOT / "marketing-assets/next-version-prep/reorder/ipad-13-appstore"

IPHONE_OUTPUT_FILES = [
    "01-every-piece-in-view.png",
    "02-build-outside-the-board.png",
    "03-move-pieces-together.png",
    "04-a-finish-worth-sharing.png",
    "05-for-every-mood.png",
    "06-made-for-little-pauses.png",
    "07-photos-become-puzzles.png",
    "08-hide-a-note-inside.png",
    "09-piece-together-a-memory.png",
    "10-no-rush-to-finish.png",
]

IPAD_OUTPUT_FILES = [
    "01-spacious-browsing.png",
    "02-birds-seasons.png",
    "03-pick-your-pace.png",
    "04-wide-calm-play.png",
    "05-more-room.png",
    "06-finish-continue.png",
    "07-personal-photos.png",
    "08-name-moment.png",
    "09-big-pieces.png",
    "10-gentle-finish.png",
]

TREATMENT_TITLES = {
    "en": (
        "Every Piece In View",
        "Build Outside the Board",
        "Move Pieces Together",
    ),
    "zh": (
        "全部碎片，一目了然",
        "在拼图框外自由拼搭",
        "一次移动多块拼图",
    ),
    "zht": (
        "全部碎片，一目瞭然",
        "在拼圖框外自由拼搭",
        "一次移動多塊拼圖",
    ),
    "ja": (
        "すべてのピースをひと目で",
        "ボードの外でも組み立てられる",
        "複数のピースをまとめて移動",
    ),
}

TREATMENT_COPY = {
    "en": (
        {"title": ("Every", "Piece In View"), "badge": "Classic Play"},
        {"title": ("Build Outside", "the Board"), "group": "Group pieces", "move": "Move together"},
        {"title": ("Move Pieces", "Together"), "badge": "Place as one"},
    ),
    "zh": (
        {"title": ("全部碎片", "一目了然"), "badge": "经典玩法"},
        {"title": ("在拼图框外", "自由拼搭"), "group": "组合拼图片", "move": "整组移动"},
        {"title": ("成组移动", "拼图片"), "badge": "整组放下"},
    ),
    "zht": (
        {"title": ("全部碎片", "一目瞭然"), "badge": "經典玩法"},
        {"title": ("在拼圖框外", "自由拼搭"), "group": "組合拼圖片", "move": "整組移動"},
        {"title": ("成組移動", "拼圖片"), "badge": "整組放下"},
    ),
    "ja": (
        {"title": ("すべてのピースが", "ひと目で見える"), "badge": "クラシック"},
        {"title": ("ボードの外でも", "組み立てられる"), "group": "ピースをまとめる", "move": "まとめて移動"},
        {"title": ("ピースを", "まとめて移動"), "badge": "まとめて配置"},
    ),
}

COMPLETION_COPY = {
    "en": {
        "title": ("A finish worth", "sharing."),
        "header": "I completed “Moonflight” · 5-star puzzle",
        "brand": "Pieceful",
        "cta": "Scan to download Pieceful",
    },
    "zh": {
        "title": ("完成这一刻，", "值得分享。"),
        "header": "我完成了「Moonflight」· 5 星难度",
        "brand": "片刻",
        "cta": "扫码下载片刻",
    },
    "zht": {
        "title": ("完成這一刻，", "值得分享。"),
        "header": "我完成了「Moonflight」· 5 星難度",
        "brand": "片刻",
        "cta": "掃碼下載片刻",
    },
    "ja": {
        "title": ("完成の瞬間を", "シェアしよう。"),
        "header": "「Moonflight」を完成 · 難易度5",
        "brand": "Pieceful",
        "cta": "QRコードでダウンロード",
    },
}

IPAD_COPY = {
    "en": {
        "title": ("Finish,", "then continue."),
        "subtitle": "Keep the moment. Share it when you like.",
        "header": "I completed “Snowy Red-crowned Cranes” · 2-star puzzle",
        "brand": "Pieceful Moment",
        "cta": "Scan to download",
    },
    "zh": {
        "title": ("拼完，", "再继续。"),
        "subtitle": "留住这一刻，想分享时就分享。",
        "header": "我完成了「雪地丹顶鹤」· 2 星难度",
        "brand": "片刻",
        "cta": "扫码下载片刻",
    },
    "zht": {
        "title": ("拼完，", "再繼續。"),
        "subtitle": "留住這一刻，想分享時就分享。",
        "header": "我完成了「雪地丹頂鶴」· 2 星難度",
        "brand": "片刻",
        "cta": "掃碼下載片刻",
    },
    "ja": {
        "title": ("完成したら、", "次の一枚へ。"),
        "subtitle": "この瞬間を残して、いつでもシェア。",
        "header": "「雪原のタンチョウ」を完成 · 難易度2",
        "brand": "Pieceful Moment",
        "cta": "QRコードでダウンロード",
    },
}

IPAD_TITLE = "Finish, then continue."
IPHONE_COMPLETION_STYLE = "original-v8"


def font(path, size):
    return ImageFont.truetype(str(path), size)


def locale_serif(locale, size):
    if locale == "ja":
        return ImageFont.truetype(str(JA_SERIF), size, index=1)
    if locale == "zht":
        return ImageFont.truetype(str(CJK_SERIF), size, index=5)
    if locale == "zh":
        return ImageFont.truetype(str(CJK_SERIF), size, index=3)
    return font(TITLE_LIGHT, size)


def locale_sans(locale, size):
    if locale == "ja":
        return ImageFont.truetype(str(JA_SANS), size)
    if locale in {"zh", "zht"}:
        return locale_serif(locale, size)
    return font(BODY_FONT, size)


def iphone_output_dir(locale):
    return Path(
        f"marketing-assets/next-version-prep/drafts/iphone-6.9-{locale}/v1.1.3-treatment-a"
    )


def ipad_output_dir(locale):
    return Path(f"marketing-assets/next-version-prep/drafts/ipad-13-{locale}/v1.1.3")


def lerp(a, b, t):
    return int(round(a + (b - a) * t))


def treatment_background():
    strip = Image.new("RGB", (1, IPHONE_H))
    pixels = strip.load()
    for y in range(IPHONE_H):
        t = y / IPHONE_H
        pixels[0, y] = (
            lerp(249, 222, t),
            lerp(250, 235, t),
            lerp(246, 228, t),
        )
    canvas = strip.resize((IPHONE_W, IPHONE_H), Image.Resampling.BICUBIC).convert("RGBA")
    overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    for x in range(-420, IPHONE_W + 420, 230):
        draw.line((x, -80, x + 540, IPHONE_H + 80), fill=(35, 60, 50, 23), width=42)
        draw.line((x + 76, -80, x + 616, IPHONE_H + 80), fill=(255, 255, 255, 34), width=84)
    overlay = overlay.filter(ImageFilter.GaussianBlur(36))
    canvas = Image.alpha_composite(canvas, overlay)
    strip.close()
    overlay.close()
    return canvas


TREATMENT_ERASE_BOXES = {
    1: ((35, 85, 1140, 610),),
    2: ((35, 85, 1250, 620), (1030, 1960, 1315, 2215)),
    3: ((35, 85, 1140, 650), (35, 630, 780, 980)),
}


def expand_mask(mask, radius=7):
    expanded = mask.copy()
    for _ in range(radius):
        grown = expanded.copy()
        grown[1:, :] |= expanded[:-1, :]
        grown[:-1, :] |= expanded[1:, :]
        grown[:, 1:] |= expanded[:, :-1]
        grown[:, :-1] |= expanded[:, 1:]
        expanded = grown
    return expanded


def erase_flattened_green_copy(image, boxes):
    original = np.asarray(image.convert("RGB"), dtype=np.uint8)
    mask = np.zeros(original.shape[:2], dtype=bool)
    red = original[:, :, 0].astype(np.int16)
    green = original[:, :, 1].astype(np.int16)
    blue = original[:, :, 2].astype(np.int16)
    green_copy = (
        (red < 175)
        & (green < 195)
        & (blue < 185)
        & (green - red > 5)
        & (blue - red > -8)
    )
    for left, top, right, bottom in boxes:
        mask[top:bottom, left:right] |= green_copy[top:bottom, left:right]
    mask = expand_mask(mask)
    filled = original.copy()
    for y in np.flatnonzero(mask.any(axis=1)):
        row_mask = mask[y]
        known = np.flatnonzero(~row_mask)
        missing = np.flatnonzero(row_mask)
        if known.size < 2:
            continue
        for channel in range(3):
            filled[y, missing, channel] = np.interp(
                missing,
                known,
                original[y, known, channel],
            ).astype(np.uint8)
    repaired = Image.fromarray(filled, "RGB")
    feather = Image.fromarray((mask.astype(np.uint8) * 255), "L").filter(
        ImageFilter.GaussianBlur(2.2)
    )
    result = Image.composite(repaired, image.convert("RGB"), feather)
    repaired.close()
    feather.close()
    return result


def erase_flattened_dark_copy(image, boxes):
    original = np.asarray(image.convert("RGB"), dtype=np.uint8)
    mask = np.zeros(original.shape[:2], dtype=bool)
    red = original[:, :, 0]
    green = original[:, :, 1]
    blue = original[:, :, 2]
    dark_copy = (red < 135) & (green < 155) & (blue < 160)
    for left, top, right, bottom in boxes:
        mask[top:bottom, left:right] |= dark_copy[top:bottom, left:right]
    mask = expand_mask(mask, radius=3)
    filled = original.copy()
    for y in np.flatnonzero(mask.any(axis=1)):
        row_mask = mask[y]
        known = np.flatnonzero(~row_mask)
        missing = np.flatnonzero(row_mask)
        if known.size < 2:
            continue
        for channel in range(3):
            filled[y, missing, channel] = np.interp(
                missing,
                known,
                original[y, known, channel],
            ).astype(np.uint8)
    repaired = Image.fromarray(filled, "RGB")
    feather = Image.fromarray((mask.astype(np.uint8) * 255), "L").filter(
        ImageFilter.GaussianBlur(1.4)
    )
    result = Image.composite(repaired, image.convert("RGB"), feather)
    repaired.close()
    feather.close()
    return result


def erase_box_to_gradient(image, box, sample_left=None, sample_right=None):
    source = image.convert("RGB")
    left, top, right, bottom = box
    width = right - left
    height = bottom - top
    patch = Image.new("RGB", (width, height))
    patch_pixels = patch.load()
    left_x = max(0, left - 3 if sample_left is None else sample_left)
    right_x = min(source.width - 1, right + 3 if sample_right is None else sample_right)
    for local_y, y in enumerate(range(top, bottom)):
        start = source.getpixel((left_x, y))
        end = source.getpixel((right_x, y))
        for local_x in range(width):
            t = local_x / max(1, width - 1)
            patch_pixels[local_x, local_y] = tuple(
                lerp(start[channel], end[channel], t) for channel in range(3)
            )
    mask = Image.new("L", (width, height), 255).filter(ImageFilter.GaussianBlur(3.0))
    source.paste(patch, (left, top), mask)
    patch.close()
    mask.close()
    return source


def draw_laurel(draw, center_x, center_y, half_width=125, height=120):
    color = MUTED
    for side in (-1, 1):
        base_x = center_x + side * half_width
        draw.arc(
            (base_x - 42, center_y - height // 2, base_x + 42, center_y + height // 2),
            80 if side < 0 else 100,
            280 if side < 0 else 260,
            fill=color,
            width=3,
        )
        for step in range(5):
            y = center_y - 44 + step * 23
            offset = 15 + abs(step - 2) * 4
            x = base_x + side * offset
            draw.ellipse((x - 10, y - 15, x + 10, y + 15), fill=color)


def fit_locale_font(draw, locale, lines, initial_size, max_width):
    size = initial_size
    text_font = locale_serif(locale, size)
    while max(draw.textbbox((0, 0), line, font=text_font)[2] for line in lines) > max_width:
        size -= 2
        text_font = locale_serif(locale, size)
    return text_font, size


def render_localized_treatment_poster(source_path, output, locale, index):
    if locale == "en":
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, output)
        return output
    with Image.open(source_path) as opened:
        source = opened.convert("RGB")
    canvas = erase_flattened_green_copy(source, TREATMENT_ERASE_BOXES[index])
    source.close()
    draw = ImageDraw.Draw(canvas)
    copy = TREATMENT_COPY[locale][index - 1]
    title_font, title_size = fit_locale_font(
        draw,
        locale,
        copy["title"],
        116 if locale != "ja" else 102,
        1140,
    )
    draw_leaf_mark(draw, 78, 150, 1.05)
    y = 188
    for line in copy["title"]:
        draw.text((78, y), line, font=title_font, fill=GREEN)
        y += title_size + 28
    if index == 2:
        note_font = locale_sans(locale, 40 if locale != "ja" else 34)
        note = copy["group"]
        if locale == "zh":
            note = "拼图片\n组合"
        elif locale == "zht":
            note = "拼圖片\n組合"
        elif locale == "ja":
            note = "ピースを\nまとめる"
        draw.multiline_text(
            (1165, 2065),
            note,
            font=note_font,
            fill=GREEN,
            anchor="mm",
            align="center",
            spacing=4,
        )
    elif index == 3:
        center_x, center_y = 280, 760
        draw_laurel(draw, center_x, center_y)
        badge_font = locale_sans(locale, 43 if locale != "ja" else 35)
        draw.text((center_x, center_y), copy["badge"], font=badge_font, fill=MUTED, anchor="mm")
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output, format="PNG", optimize=True)
    canvas.close()
    return output


def rounded_mask(size, radius):
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        (0, 0, size[0] - 1, size[1] - 1), radius=radius, fill=255
    )
    return mask


def phone_layer(source_path, phone_width):
    with Image.open(source_path) as opened:
        screenshot = opened.convert("RGB")
    outer_width = phone_width
    outer_height = round(phone_width * IPHONE_H / IPHONE_W)
    border = max(18, round(phone_width * 0.035))
    radius = round(phone_width * 0.105)
    screen_size = (outer_width - border * 2, outer_height - border * 2)
    screen = screenshot.resize(screen_size, Image.Resampling.LANCZOS)
    screenshot.close()

    phone = Image.new("RGBA", (outer_width, outer_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(phone)
    draw.rounded_rectangle(
        (0, 0, outer_width - 1, outer_height - 1), radius=radius, fill=(20, 23, 22, 255)
    )
    screen_mask = rounded_mask(screen_size, max(8, radius - border))
    phone.paste(screen.convert("RGBA"), (border, border), screen_mask)
    draw.rounded_rectangle(
        (border, border, outer_width - border - 1, outer_height - border - 1),
        radius=max(8, radius - border),
        outline=(255, 255, 255, 55),
        width=2,
    )
    screen.close()
    screen_mask.close()
    return phone


def paste_with_shadow(canvas, layer, center, angle):
    alpha = layer.getchannel("A")
    shadow = Image.new("RGBA", layer.size, (15, 35, 28, 120))
    shadow.putalpha(alpha.filter(ImageFilter.GaussianBlur(22)))
    rotated_shadow = shadow.rotate(angle, expand=True, resample=Image.Resampling.BICUBIC)
    rotated = layer.rotate(angle, expand=True, resample=Image.Resampling.BICUBIC)
    x = round(center[0] - rotated.width / 2)
    y = round(center[1] - rotated.height / 2)
    canvas.alpha_composite(rotated_shadow, (x + 18, y + 32))
    canvas.alpha_composite(rotated, (x, y))
    alpha.close()
    shadow.close()
    rotated_shadow.close()
    rotated.close()


def draw_leaf_mark(draw, x, y, scale=1.0):
    width = max(1, round(3 * scale))
    draw.line((x, y, x + 72 * scale, y), fill=MUTED, width=width)
    stem_x = x + 96 * scale
    draw.line((stem_x, y, stem_x + 30 * scale, y - 18 * scale), fill=MUTED, width=width)
    draw.ellipse(
        (stem_x + 20 * scale, y - 35 * scale, stem_x + 50 * scale, y - 10 * scale),
        fill=MUTED,
    )
    draw.ellipse(
        (stem_x + 3 * scale, y - 18 * scale, stem_x + 30 * scale, y + 4 * scale),
        fill=MUTED,
    )


def draw_treatment_title(draw, lines):
    x, y = 82, 178
    draw_leaf_mark(draw, x, y - 42, 1.05)
    draw.multiline_text(
        (x, y),
        "\n".join(lines),
        font=font(TITLE_FONT, 126),
        fill=GREEN,
        spacing=6,
    )


def draw_brand_pill(canvas):
    width, height = 455, 86
    layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    draw.rounded_rectangle(
        (0, 0, width - 1, height - 1),
        radius=43,
        fill=(232, 241, 236, 184),
        outline=(117, 150, 140, 75),
        width=1,
    )
    draw_leaf_mark(draw, 42, 45, 0.65)
    draw.text((122, 23), "Pieceful Moment", font=font(TITLE_FONT, 34), fill=GREEN)
    canvas.alpha_composite(layer, ((IPHONE_W - width) // 2, 2706))
    layer.close()


def original_background():
    strip = Image.new("RGB", (1, IPHONE_H))
    pixels = strip.load()
    paper = (250, 250, 246)
    mist = (232, 240, 245)
    for y in range(IPHONE_H):
        t = min(1, (y / IPHONE_H) * 1.22)
        pixels[0, y] = tuple(lerp(paper[i], mist[i], t) for i in range(3))
    canvas = strip.resize((IPHONE_W, IPHONE_H), Image.Resampling.BICUBIC).convert("RGBA")
    strip.close()
    return canvas


def localize_iphone_completion(locale):
    with Image.open(COMPLETION_SOURCE) as opened:
        source = opened.convert("RGB")
    if locale == "en":
        return source
    header_icon = source.crop((150, 120, 250, 250))
    localized = erase_box_to_gradient(
        source,
        (150, 115, 1035, 270),
        sample_left=80,
        sample_right=1060,
    )
    source.close()
    localized.paste(header_icon, (150, 120))
    header_icon.close()
    cleaned = erase_box_to_gradient(
        localized,
        (190, 2020, 650, 2280),
        sample_left=190,
        sample_right=650,
    )
    localized.close()
    localized = cleaned
    draw = ImageDraw.Draw(localized)
    copy = COMPLETION_COPY[locale]
    header_font = locale_sans(locale, 31 if locale != "ja" else 27)
    draw.text((255, 166), copy["header"], font=header_font, fill=(47, 66, 69))
    draw.text((205, 2070), copy["brand"], font=locale_sans(locale, 29), fill=(39, 65, 67))
    draw.text((205, 2114), copy["cta"], font=locale_sans(locale, 21), fill=(39, 65, 67))
    return localized


def original_completion_layer(locale="en"):
    source = localize_iphone_completion(locale)
    screen_width = 1100
    screen_height = round(source.height * screen_width / source.width)
    screen = source.resize((screen_width, screen_height), Image.Resampling.LANCZOS).convert("RGBA")
    source.close()
    mask = rounded_mask(screen.size, 72)
    pad = 34
    layer = Image.new("RGBA", (screen_width + pad * 2, screen_height + pad * 2), (0, 0, 0, 0))
    shadow = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    shadow_shape = Image.new("RGBA", screen.size, (38, 50, 64, 45))
    shadow.paste(shadow_shape, (pad, pad), mask)
    blurred = shadow.filter(ImageFilter.GaussianBlur(24))
    layer.alpha_composite(blurred)
    layer.paste(screen, (pad, pad), mask)
    rotated = layer.rotate(0.4, expand=True, resample=Image.Resampling.BICUBIC)
    screen.close()
    mask.close()
    shadow.close()
    shadow_shape.close()
    blurred.close()
    layer.close()
    return rotated


def render_iphone_completion(output, locale="en"):
    canvas = original_background()
    draw = ImageDraw.Draw(canvas)
    lines = COMPLETION_COPY[locale]["title"]
    if locale == "en":
        draw.text((92, 74), lines[0], font=font(TITLE_LIGHT, 116), fill=(42, 47, 53))
        draw.text((92, 196), lines[1], font=font(TITLE_ITALIC, 116), fill=(42, 47, 53))
    else:
        title_font, title_size = fit_locale_font(draw, locale, lines, 108 if locale != "ja" else 92, 1130)
        draw.text((92, 74), lines[0], font=title_font, fill=(42, 47, 53))
        draw.text((92, 74 + title_size + 24), lines[1], font=title_font, fill=(42, 47, 53))
    layer = original_completion_layer(locale)
    canvas.alpha_composite(layer, ((IPHONE_W - layer.width) // 2, 400))
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(output, format="PNG", optimize=True)
    layer.close()
    canvas.close()


def ipad_background():
    strip = Image.new("RGB", (1, IPAD_H))
    pixels = strip.load()
    for y in range(IPAD_H):
        t = min(1, y / IPAD_H * 1.25)
        pixels[0, y] = tuple(lerp(IPAD_PAPER[i], IPAD_MIST[i], t) for i in range(3))
    canvas = strip.resize((IPAD_W, IPAD_H), Image.Resampling.BICUBIC).convert("RGBA")
    strip.close()
    return canvas


def erase_to_background(image, box, sample_x=40):
    draw = ImageDraw.Draw(image)
    left, top, right, bottom = box
    for y in range(top, bottom):
        draw.line((left, y, right, y), fill=image.getpixel((sample_x, y)))


def localize_ipad_completion(locale="en"):
    with Image.open(IPAD_COMPLETION_SOURCE) as opened:
        source = opened.convert("RGB")
    if locale == "zh":
        return source
    erase_to_background(source, (350, 65, 1045, 155))
    erase_to_background(source, (320, 1230, 610, 1375))
    draw = ImageDraw.Draw(source)
    copy = IPAD_COPY[locale]
    header = copy["header"]
    header_size = 25 if locale == "en" else 24
    header_font = locale_sans(locale, header_size)
    while draw.textbbox((0, 0), header, font=header_font)[2] > 650 and header_size > 18:
        header_size -= 1
        header_font = locale_sans(locale, header_size)
    draw.text((365, 91), header, font=header_font, fill=(47, 66, 69))
    draw.text((330, 1244), copy["brand"], font=locale_sans(locale, 24), fill=(39, 65, 67))
    draw.text((330, 1278), copy["cta"], font=locale_sans(locale, 18), fill=(39, 65, 67))
    return source


def completion_card(source_input, width, crop_box=None):
    if isinstance(source_input, Image.Image):
        source = source_input.convert("RGB")
    else:
        with Image.open(source_input) as opened:
            source = opened.convert("RGB")
    if crop_box is not None:
        cropped = source.crop(crop_box)
        source.close()
        source = cropped
    height = round(source.height * width / source.width)
    card = source.resize((width, height), Image.Resampling.LANCZOS).convert("RGBA")
    source.close()
    mask = rounded_mask(card.size, 52)
    composed = Image.new("RGBA", (width + 90, height + 90), (0, 0, 0, 0))
    shadow = Image.new("RGBA", card.size, (35, 45, 52, 78))
    shadow.putalpha(mask.filter(ImageFilter.GaussianBlur(34)))
    composed.alpha_composite(shadow, (54, 58))
    composed.paste(card, (34, 28), mask)
    card.close()
    mask.close()
    shadow.close()
    return composed


def render_ipad_completion(output, locale="en"):
    canvas = ipad_background()
    draw = ImageDraw.Draw(canvas)
    x, y = 150, 78
    copy = IPAD_COPY[locale]
    if locale == "en":
        draw.text((x, y), copy["title"][0], font=font(TITLE_LIGHT, 148), fill=IPAD_INK)
        draw.text((x, y + 162), copy["title"][1], font=font(TITLE_ITALIC, 148), fill=IPAD_INK)
    else:
        title_font, title_size = fit_locale_font(draw, locale, copy["title"], 132 if locale != "ja" else 112, 1600)
        draw.text((x, y), copy["title"][0], font=title_font, fill=IPAD_INK)
        draw.text((x, y + title_size + 24), copy["title"][1], font=title_font, fill=IPAD_INK)
    draw.text(
        (x, y + 362),
        copy["subtitle"],
        font=locale_sans(locale, 48 if locale == "en" else 44),
        fill=IPAD_SOFT,
    )
    localized = localize_ipad_completion(locale)
    card = completion_card(localized, 1450)
    localized.close()
    canvas.alpha_composite(card, ((IPAD_W - card.width) // 2, 535))
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(output, format="PNG", optimize=True)
    card.close()
    canvas.close()


def make_contact_sheet(paths, output, columns=5, thumb_width=300):
    opened = []
    try:
        for path in paths:
            with Image.open(path) as source:
                image = source.convert("RGB")
            thumb_height = round(image.height * thumb_width / image.width)
            thumb = image.resize((thumb_width, thumb_height), Image.Resampling.LANCZOS)
            image.close()
            opened.append(thumb)
        rows = math.ceil(len(opened) / columns)
        gutter = 22
        sheet = Image.new(
            "RGB",
            (
                columns * thumb_width + (columns + 1) * gutter,
                rows * opened[0].height + (rows + 1) * gutter,
            ),
            (244, 246, 243),
        )
        for index, image in enumerate(opened):
            col = index % columns
            row = index // columns
            sheet.paste(
                image,
                (gutter + col * (thumb_width + gutter), gutter + row * (image.height + gutter)),
            )
        output.parent.mkdir(parents=True, exist_ok=True)
        sheet.save(output, format="JPEG", quality=90, optimize=True)
        sheet.close()
    finally:
        for image in opened:
            image.close()


def required_sources():
    return (
        LOCKED_IPHONE_SOURCES
        + UNCHANGED_IPHONE_SOURCES
        + [COMPLETION_SOURCE, IPAD_COMPLETION_SOURCE]
        + [IPAD_SOURCE_DIR / filename for filename in IPAD_OUTPUT_FILES]
    )


def validate_sources():
    missing = [path for path in required_sources() if not path.is_file()]
    if missing:
        raise FileNotFoundError("Missing source assets:\n" + "\n".join(str(path) for path in missing))


def render_localized_updates(output_root=ROOT):
    output_root = Path(output_root)
    validate_sources()
    rendered = {}
    for locale in LOCALES:
        iphone_dir = output_root / iphone_output_dir(locale)
        ipad_dir = output_root / ipad_output_dir(locale)
        iphone_dir.mkdir(parents=True, exist_ok=True)
        ipad_dir.mkdir(parents=True, exist_ok=True)
        iphone_paths = []
        for index, (filename, source) in enumerate(
            zip(IPHONE_OUTPUT_FILES[:3], LOCKED_IPHONE_SOURCES),
            start=1,
        ):
            path = iphone_dir / filename
            render_localized_treatment_poster(source, path, locale, index)
            iphone_paths.append(path)
        completion_path = iphone_dir / IPHONE_OUTPUT_FILES[3]
        render_iphone_completion(completion_path, locale)
        iphone_paths.append(completion_path)
        make_contact_sheet(
            iphone_paths,
            iphone_dir / "contact-sheet-updated.jpg",
            columns=4,
            thumb_width=300,
        )
        ipad_path = ipad_dir / "06-finish-continue.png"
        render_ipad_completion(ipad_path, locale)
        rendered[locale] = {"iphone": iphone_paths, "ipad": ipad_path}
    return rendered


def export_website_updates(output_root=ROOT):
    output_root = Path(output_root)
    exported = []
    for locale in LOCALES:
        iphone_source_dir = output_root / iphone_output_dir(locale)
        iphone_web_dir = output_root / f"assets/img/shots/v8/{locale}"
        iphone_web_dir.mkdir(parents=True, exist_ok=True)
        for number, filename in enumerate(IPHONE_OUTPUT_FILES[:4], start=1):
            source_path = iphone_source_dir / filename
            output_path = iphone_web_dir / f"{number:02d}.jpg"
            with Image.open(source_path) as opened:
                web = opened.convert("RGB").resize((414, 900), Image.Resampling.LANCZOS)
            web.save(output_path, format="JPEG", quality=88, optimize=True, progressive=True)
            web.close()
            exported.append(output_path)

        ipad_source = output_root / ipad_output_dir(locale) / "06-finish-continue.png"
        ipad_web_dir = output_root / f"assets/img/shots/v113-ipad/{locale}"
        ipad_web_dir.mkdir(parents=True, exist_ok=True)
        ipad_output = ipad_web_dir / "06.jpg"
        with Image.open(ipad_source) as opened:
            web = opened.convert("RGB").resize((720, 960), Image.Resampling.LANCZOS)
        web.save(ipad_output, format="JPEG", quality=88, optimize=True, progressive=True)
        web.close()
        exported.append(ipad_output)
    return exported


def render_all(output_root=ROOT):
    output_root = Path(output_root)
    validate_sources()
    iphone_dir = output_root / IPHONE_RELATIVE_OUTPUT
    ipad_dir = output_root / IPAD_RELATIVE_OUTPUT
    iphone_dir.mkdir(parents=True, exist_ok=True)
    ipad_dir.mkdir(parents=True, exist_ok=True)

    for filename, source in zip(IPHONE_OUTPUT_FILES[:3], LOCKED_IPHONE_SOURCES):
        shutil.copy2(source, iphone_dir / filename)
    render_iphone_completion(iphone_dir / IPHONE_OUTPUT_FILES[3])
    for filename, source in zip(IPHONE_OUTPUT_FILES[4:], UNCHANGED_IPHONE_SOURCES):
        shutil.copy2(source, iphone_dir / filename)

    for filename in IPAD_OUTPUT_FILES:
        shutil.copy2(IPAD_SOURCE_DIR / filename, ipad_dir / filename)
    render_ipad_completion(ipad_dir / IPAD_OUTPUT_FILES[5])

    iphone_paths = [iphone_dir / filename for filename in IPHONE_OUTPUT_FILES]
    ipad_paths = [ipad_dir / filename for filename in IPAD_OUTPUT_FILES]
    make_contact_sheet(iphone_paths, iphone_dir / "contact-sheet.jpg")
    make_contact_sheet(ipad_paths, ipad_dir / "contact-sheet.jpg")
    render_localized_updates(output_root)
    return iphone_paths, ipad_paths


def main():
    iphone_paths, ipad_paths = render_all()
    for path in iphone_paths + ipad_paths:
        print(path)


if __name__ == "__main__":
    main()
