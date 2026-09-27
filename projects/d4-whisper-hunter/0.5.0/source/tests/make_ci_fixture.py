from __future__ import annotations

import argparse
from pathlib import Path

import cv2
import numpy as np


def make_textured_map(width: int = 1500, height: int = 1000) -> np.ndarray:
    rng = np.random.default_rng(20260925)
    image = np.full((height, width, 3), 72, np.uint8)
    noise = rng.integers(-22, 23, size=(height, width, 1), dtype=np.int16)
    image = np.clip(image.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    for i in range(500):
        x = int(rng.integers(16, width - 16))
        y = int(rng.integers(16, height - 16))
        radius = int(rng.integers(2, 11))
        c = int(rng.integers(40, 160))
        cv2.circle(image, (x, y), radius, (c, min(255, c + 6), c), 1)
    for i in range(90):
        p1 = (int(rng.integers(0, width)), int(rng.integers(0, height)))
        p2 = (int(rng.integers(0, width)), int(rng.integers(0, height)))
        cv2.line(image, p1, p2, (112, 103, 95), 1)
    for i in range(35):
        cv2.putText(
            image,
            f"R{i:02d}",
            (30 + (i * 71) % 1320, 50 + (i * 97) % 850),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (150, 142, 132),
            1,
            cv2.LINE_AA,
        )
    return image


def add_whisper(image: np.ndarray, center: tuple[int, int], color: tuple[int, int, int]) -> None:
    x, y = center
    cv2.circle(image, (x, y), 12, color, 4)
    cv2.line(image, (x - 14, y), (x + 14, y), color, 3)
    cv2.line(image, (x, y - 14), (x, y + 14), color, 3)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    base = make_textured_map()
    query = base[160:860, 260:1320].copy()
    add_whisper(query, (230, 260), (180, 170, 245))
    add_whisper(query, (530, 360), (90, 70, 215))
    add_whisper(query, (820, 480), (30, 20, 150))

    danger = np.full((1080, 1920, 3), (28, 28, 31), np.uint8)
    cv2.circle(danger, (960, 540), 128, (32, 72, 238), 18)
    cv2.circle(danger, (960, 540), 78, (20, 45, 180), 8)

    executioner = np.full((1080, 1920, 3), (28, 28, 31), np.uint8)
    blade = np.array([[948,315],[972,315],[970,505],[960,535],[950,505]], np.int32)
    cv2.fillConvexPoly(executioner, blade, (205, 215, 225))
    cv2.rectangle(executioner, (925,485), (995,500), (45,170,225), -1)
    cv2.circle(executioner, (960,540), 58, (32,72,238), 9)

    map_path = args.out / "fixture-map.png"
    query_path = args.out / "fixture-query.png"
    danger_path = args.out / "fixture-danger.png"
    executioner_path = args.out / "fixture-executioner.png"
    if (
        not cv2.imwrite(str(map_path), base)
        or not cv2.imwrite(str(query_path), query)
        or not cv2.imwrite(str(danger_path), danger)
        or not cv2.imwrite(str(executioner_path), executioner)
    ):
        raise SystemExit("Could not write CI fixture images")
    print(map_path)
    print(query_path)
    print(danger_path)
    print(executioner_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
