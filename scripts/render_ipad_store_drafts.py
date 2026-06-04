from pathlib import Path
import math

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
FONTS = ROOT / "marketing-assets" / "next-version-prep" / "fonts"
OUT = ROOT / "marketing-assets" / "next-version-prep" / "drafts" / "ipad-13-en" / "v1"

W, H = 2064, 2752
PAPER = (250, 250, 246)
MIST = (233, 240, 245)
SAGE = (132, 153, 137)
INK = (44, 49, 56)
INK_SOFT = (86, 93, 102)


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


SERIF = "Fraunces-300.ttf"
SERIF_ITALIC = "Fraunces-Italic-300.ttf"
SANS = "HankenGrotesk-400.ttf"


ITEMS = [
    {
        "file": "01-spacious-browsing.png",
        "source": "marketing-assets/ipad-upload-ready/2548-2064x2752.png",
        "title": ["Spacious", "browsing."],
        "subtitle": "More room for calm collections.",
        "tilt": -0.4,
        "crop_top": 126,
    },
    {
        "file": "02-birds-and-seasons.png",
        "source": "marketing-assets/ipad-upload-ready/6217-2064x2752.png",
        "title": ["Birds,", "seasons."],
        "subtitle": "Find a picture for the moment.",
        "tilt": 0.5,
        "crop_top": 126,
    },
    {
        "file": "03-choose-your-challenge.png",
        "source": "marketing-assets/ipad-upload-ready/1715-2064x2752.png",
        "title": ["Choose", "your pace."],
        "subtitle": "Easy or challenging, always quiet.",
        "tilt": -0.45,
        "crop_top": 126,
    },
    {
        "file": "04-big-pieces-soft-pace.png",
        "source": "marketing-assets/ipad-upload-ready/2546-2064x2752.png",
        "title": ["Big pieces,", "soft pace."],
        "subtitle": "A wider canvas for focused play.",
        "tilt": 0.45,
        "crop_top": 126,
    },
    {
        "file": "05-a-gentle-finish.png",
        "source": "marketing-assets/ipad-upload-ready/2547-2064x2752.png",
        "title": ["A gentle", "finish."],
        "subtitle": "Complete the image, then keep going.",
        "tilt": -0.45,
        "crop_top": 126,
    },
    {
        "file": "06-more-room-to-play.png",
        "source": "marketing-assets/ipad-upload-ready/微信图片_20260529224643_890_17-2064x2752.png",
        "title": ["More room", "to play."],
        "subtitle": "Designed to feel calm on iPad.",
        "tilt": 0.45,
        "crop_top": 126,
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
            r = lerp(PAPER[0], MIST[0], min(1, t * 1.25))
            g = lerp(PAPER[1], MIST[1], min(1, t * 1.25))
            b = lerp(PAPER[2], MIST[2], min(1, t * 1.25))
            dx = (x - W * 0.78) / W
            dy = (y - H * 0.04) / H
            glow = max(0, 1 - math.sqrt(dx * dx + dy * dy) * 2.0)
            px[x, y] = (
                min(255, lerp(r, 255, glow * 0.42)),
                min(255, lerp(g, 255, glow * 0.42)),
                min(255, lerp(b, 255, glow * 0.42)),
            )
    return img


def draw_wrapped(draw, text, xy, max_width, font_obj, fill, line_gap=16):
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


def screen_layer(source, crop_top, tilt):
    src = Image.open(ROOT / source).convert("RGB")
    src = src.crop((0, crop_top, src.width, src.height))
    sw = int(W * 0.84)
    sh = int(src.height * (sw / src.width))
    screen = src.resize((sw, sh), Image.Resampling.LANCZOS)
    radius = int(sw * 0.045)
    mask = rounded_rect_mask(screen.size, radius)

    pad = 44
    composed = Image.new("RGBA", (sw + pad * 2, sh + pad * 2), (0, 0, 0, 0))
    shadow = Image.new("RGBA", composed.size, (0, 0, 0, 0))
    shadow_mask = rounded_rect_mask((sw, sh), radius)
    shadow_layer = Image.new("RGBA", (sw, sh), (38, 50, 64, 66))
    shadow.paste(shadow_layer, (pad, pad), shadow_mask)
    shadow = shadow.filter(ImageFilter.GaussianBlur(34))
    composed = Image.alpha_composite(composed, shadow)
    composed.paste(screen.convert("RGBA"), (pad, pad), mask)
    return composed.rotate(tilt, expand=True, resample=Image.Resampling.BICUBIC)


def render(item):
    canvas = background().convert("RGBA")
    draw = ImageDraw.Draw(canvas)

    x = 150
    y = 78
    for i, line in enumerate(item["title"]):
        f = font(SERIF_ITALIC if i == 1 else SERIF, 148)
        draw.text((x, y), line, font=f, fill=INK)
        y += 162

    draw_wrapped(draw, item["subtitle"], (x, y + 38), 1200, font(SANS, 48), INK_SOFT, 14)

    layer = screen_layer(item["source"], item["crop_top"], item["tilt"])
    px = (W - layer.width) // 2
    py = 610
    canvas.alpha_composite(layer, (px, py))

    OUT.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(OUT / item["file"], quality=96)


def main():
    for item in ITEMS:
        render(item)
        print(OUT / item["file"])


if __name__ == "__main__":
    main()
