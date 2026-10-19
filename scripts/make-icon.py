#!/usr/bin/env python3
"""Draw the Real Weather dock icon (gold field, cream sun)."""

import math
from pathlib import Path

from PIL import Image, ImageDraw

SIZE = 1024
OUT = Path(__file__).resolve().parents[1] / "assets" / "icon.png"


def lerp(a: int, b: int, t: float) -> int:
    return int(a + (b - a) * t)


def main() -> None:
    img = Image.new("RGB", (SIZE, SIZE))
    px = img.load()
    for y in range(SIZE):
        for x in range(SIZE):
            t = (x * 0.35 + y * 0.65) / (SIZE - 1)
            px[x, y] = (
                lerp(255, 236, t),
                lerp(214, 146, t),
                lerp(120, 42, t),
            )

    draw = ImageDraw.Draw(img)
    cx = cy = SIZE // 2
    cream = (255, 248, 230)
    core = (196, 112, 28)

    for i in range(12):
        ang = math.radians(i * 30 - 90)
        inner, outer = 250, 400
        spread = math.radians(7.5)
        points = [
            (
                cx + inner * math.cos(ang - spread),
                cy + inner * math.sin(ang - spread),
            ),
            (
                cx + outer * math.cos(ang - spread * 0.35),
                cy + outer * math.sin(ang - spread * 0.35),
            ),
            (
                cx + outer * math.cos(ang + spread * 0.35),
                cy + outer * math.sin(ang + spread * 0.35),
            ),
            (
                cx + inner * math.cos(ang + spread),
                cy + inner * math.sin(ang + spread),
            ),
        ]
        draw.polygon(points, fill=cream)

    sun_r = 210
    draw.ellipse((cx - sun_r, cy - sun_r, cx + sun_r, cy + sun_r), fill=cream)
    core_r = 64
    draw.ellipse((cx - core_r, cy - core_r, cx + core_r, cy + core_r), fill=core)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, "PNG")
    print(OUT)


if __name__ == "__main__":
    main()
