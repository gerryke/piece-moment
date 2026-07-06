from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "img" / "share.jpg"
OUTPUT = ROOT / "assets" / "img" / "share-pieceful.jpg"
FONTS = ROOT / "marketing-assets" / "next-version-prep" / "fonts"


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


with Image.open(SOURCE) as source:
    image = source.convert("RGB")

overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
pixels = overlay.load()
cream = (250, 247, 237)
for x in range(480):
    alpha = 255 if x < 360 else round(255 * (1 - (x - 360) / 120))
    for y in range(image.height):
        pixels[x, y] = (*cream, max(0, alpha))

image = Image.alpha_composite(image.convert("RGBA"), overlay)
draw = ImageDraw.Draw(image)
ink = (35, 48, 66, 255)
muted = (78, 91, 106, 255)

draw.text((54, 104), "Pieceful", font=font("HankenGrotesk-600.ttf", 58), fill=ink)
draw.text((54, 166), "Moment", font=font("HankenGrotesk-600.ttf", 58), fill=ink)
draw.text((57, 258), "Cozy Jigsaw Puzzles", font=font("HankenGrotesk-500.ttf", 25), fill=ink)
draw.text(
    (57, 310),
    "A quiet moment, piece by piece.",
    font=font("Fraunces-Italic-300.ttf", 24),
    fill=muted,
)
draw.rounded_rectangle((57, 365, 220, 369), radius=2, fill=(57, 91, 109, 255))

image.convert("RGB").save(OUTPUT, quality=92, optimize=True)
print(OUTPUT)
