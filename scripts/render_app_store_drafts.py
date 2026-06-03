from pathlib import Path
import math
import textwrap

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
FONTS = ROOT / "marketing-assets" / "next-version-prep" / "fonts"
OUT = ROOT / "marketing-assets" / "next-version-prep" / "drafts" / "iphone-6.9-en" / "v5"

W, H = 1320, 2868
PAPER = (250, 250, 246)
MIST = (233, 240, 245)
MIST_DEEP = (215, 226, 236)
SAGE = (132, 153, 137)
INK = (44, 49, 56)
INK_SOFT = (86, 93, 102)
WHITE = (255, 255, 255)


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


SERIF = "Fraunces-300.ttf"
SERIF_ITALIC = "Fraunces-Italic-300.ttf"
SANS = "HankenGrotesk-400.ttf"
SANS_MED = "HankenGrotesk-500.ttf"


ITEMS = [
    {
        "file": "01-quiet-jigsaw-moments.png",
        "source": "marketing-assets/next-version-prep/sources/iphone-6.9/07-gallery-season-calendar-1320x2868.png",
        "eyebrow": "",
        "title": ["Quiet", "moments."],
        "subtitle": "Relaxing puzzles for small breaks.",
        "tilt": -0.8,
        "crop_top": 116,
        "scale": 0.88,
        "y": 520,
    },
    {
        "file": "02-softer-way-to-play.png",
        "source": "marketing-assets/next-version-prep/sources/iphone-6.9/09-lime-soda-gameplay-scattered-1320x2868.png",
        "eyebrow": "",
        "title": ["Soft", "focus."],
        "subtitle": "No countdowns. No pressure.",
        "tilt": 0.8,
        "crop_top": 116,
        "scale": 0.88,
        "y": 510,
    },
    {
        "file": "03-your-photos-as-puzzles.png",
        "source": "marketing-assets/next-version-prep/sources/iphone-6.9/03-child-art-difficulty-select-1320x2868.png",
        "eyebrow": "",
        "title": ["Your photos,", "as puzzles."],
        "subtitle": "Personal, private, offline.",
        "tilt": -0.7,
        "crop_top": 260,
        "scale": 0.88,
        "y": 525,
    },
    {
        "file": "04-no-ads-no-account.png",
        "source": "marketing-assets/next-version-prep/sources/iphone-6.9/17-cranes-gameplay-scattered-1320x2868.png",
        "eyebrow": "",
        "title": ["No ads.", "No account."],
        "subtitle": "Just open, play, and slow down.",
        "tilt": 0.8,
        "crop_top": 116,
        "scale": 0.88,
        "y": 510,
    },
    {
        "file": "05-keep-the-finished-moment.png",
        "source": "marketing-assets/next-version-prep/sources/iphone-6.9/06-child-art-finished-memory-note-1320x2868.png",
        "eyebrow": "",
        "title": ["Keep the", "moment."],
        "subtitle": "A quiet finish, with a note.",
        "tilt": -0.7,
        "crop_top": 116,
        "scale": 0.88,
        "y": 525,
    },
    {
        "file": "06-gentle-collections.png",
        "source": "marketing-assets/upload-ready/IMG_3022.PNG",
        "eyebrow": "",
        "title": ["Gentle", "collections."],
        "subtitle": "Find a picture for the mood.",
        "tilt": 0.7,
        "crop_top": 116,
        "scale": 0.88,
        "y": 510,
    },
]


def lerp(a, b, t):
    return int(a + (b - a) * t)


def background():
    img = Image.new("RGB", (W, H), PAPER)
    px = img.load()
    for y in range(H):
        for x in range(W):
            t = y / H
            r = lerp(PAPER[0], MIST[0], min(1, t * 1.35))
            g = lerp(PAPER[1], MIST[1], min(1, t * 1.35))
            b = lerp(PAPER[2], MIST[2], min(1, t * 1.35))
            dx = (x - W * 0.78) / W
            dy = (y - H * 0.08) / H
            glow = max(0, 1 - math.sqrt(dx * dx + dy * dy) * 2.1)
            px[x, y] = (
                min(255, lerp(r, 255, glow * 0.42)),
                min(255, lerp(g, 255, glow * 0.42)),
                min(255, lerp(b, 255, glow * 0.42)),
            )
    return img


def draw_wrapped(draw, text, xy, max_width, font_obj, fill, line_gap=14):
    words = text.split()
    lines = []
    line = ""
    for word in words:
        probe = (line + " " + word).strip()
        if draw.textbbox((0, 0), probe, font=font_obj)[2] <= max_width or not line:
            line = probe
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    x, y = xy
    for line in lines:
        draw.text((x, y), line, font=font_obj, fill=fill)
        bbox = draw.textbbox((x, y), line, font=font_obj)
        y = bbox[3] + line_gap


def rounded_rect_mask(size, radius):
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, size[0] - 1, size[1] - 1), radius=radius, fill=255)
    return mask


def phone_layer(source, crop_top, scale, tilt):
    src = Image.open(ROOT / source).convert("RGB")
    src = src.crop((0, crop_top, src.width, src.height))
    sw = int(W * scale)
    sh = int(src.height * (sw / src.width))
    screen = src.resize((sw, sh), Image.Resampling.LANCZOS)
    radius = int(sw * 0.065)
    mask = rounded_rect_mask(screen.size, radius)

    pad = 30
    composed = Image.new("RGBA", (sw + pad * 2, sh + pad * 2), (0, 0, 0, 0))
    shadow = Image.new("RGBA", composed.size, (0, 0, 0, 0))
    shadow_mask = rounded_rect_mask((sw, sh), radius)
    shadow_layer = Image.new("RGBA", (sw, sh), (38, 50, 64, 72))
    shadow.paste(shadow_layer, (pad, pad), shadow_mask)
    shadow = shadow.filter(ImageFilter.GaussianBlur(30))
    composed = Image.alpha_composite(composed, shadow)
    composed.paste(screen.convert("RGBA"), (pad, pad), mask)
    return composed.rotate(tilt, expand=True, resample=Image.Resampling.BICUBIC)


def render(item):
    canvas = background().convert("RGBA")
    draw = ImageDraw.Draw(canvas)

    x = 104
    y = 132
    if item["eyebrow"]:
        draw.text((x, y), item["eyebrow"], font=font(SANS_MED, 27), fill=SAGE)
        y += 86

    for i, line in enumerate(item["title"]):
        f = font(SERIF_ITALIC if i == 1 else SERIF, 102)
        draw.text((x, y), line, font=f, fill=INK)
        y += 108

    draw_wrapped(draw, item["subtitle"], (x, y + 10), 770, font(SANS, 34), INK_SOFT, 12)

    layer = phone_layer(item["source"], item["crop_top"], item["scale"], item["tilt"])
    px = (W - layer.width) // 2
    py = item["y"]
    canvas.alpha_composite(layer, (px, py))

    OUT.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(OUT / item["file"], quality=96)


def main():
    for item in ITEMS:
        render(item)
        print(OUT / item["file"])


if __name__ == "__main__":
    main()
