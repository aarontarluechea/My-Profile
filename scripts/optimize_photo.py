#!/usr/bin/env python3
"""
Optimize a source profile photo and write `assets/photo.jpg`.

Usage:
  1. Place your original photo in `assets/photo-original.jpg` (or .png).
  2. From project root run: `python scripts/optimize_photo.py`

The script will resize to a max dimension and save a compressed JPEG.
"""
from pathlib import Path
from PIL import Image
import sys

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
ASSETS.mkdir(parents=True, exist_ok=True)

def find_source():
    for name in ('photo-original.jpg','photo-original.jpeg','photo-original.png','photo.jpg','photo.png'):
        p = ASSETS / name
        if p.exists():
            return p
    return None

def optimize(src: Path, dest: Path, max_size=800, quality=80):
    img = Image.open(src)
    img = img.convert('RGB')
    img.thumbnail((max_size, max_size), Image.LANCZOS)
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest, 'JPEG', quality=quality, optimize=True, progressive=True)

def main():
    src = find_source()
    if not src:
        print('No source image found. Place your photo as `assets/photo-original.jpg` or `assets/photo.jpg` and retry.')
        sys.exit(2)
    dest = ASSETS / 'photo.jpg'
    print(f'Optimizing {src.name} -> {dest.name} ...')
    try:
        optimize(src, dest)
        print('Saved', dest)
    except Exception as e:
        print('Failed to optimize image:', e)
        sys.exit(1)

if __name__ == '__main__':
    main()
