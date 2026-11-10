"""Remove the background of images with the Pixlub API.

Usage:
    export PIXLUB_API_KEY="pix.xxxxxxxx.xxxxxxxx..."
    python remove_background.py photo.jpg
    python remove_background.py photos/ --output cutouts --png
"""

from __future__ import annotations

import argparse
import io
import sys
from pathlib import Path

import pixlub

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def find_images(paths: list[str]) -> list[Path]:
    """Files given on the command line, plus the images found in the given folders."""
    images: list[Path] = []
    for name in paths:
        path = Path(name)
        if path.is_dir():
            images.extend(sorted(p for p in path.iterdir() if p.suffix.lower() in IMAGE_EXTENSIONS))
        elif path.is_file():
            images.append(path)
        else:
            print(f"Skipped {name}: no such file or folder", file=sys.stderr)
    return images


def to_png(content: bytes, target: Path) -> None:
    """Converts the WebP cut-out to PNG, keeping the transparency."""
    try:
        from PIL import Image
    except ImportError:
        sys.exit("--png needs Pillow: pip install pillow")
    with Image.open(io.BytesIO(content)) as image:
        image.save(target, "PNG")


def main() -> int:
    parser = argparse.ArgumentParser(description="Remove the background of images with the Pixlub API.")
    parser.add_argument("paths", nargs="+", help="images or folders of images")
    parser.add_argument("-o", "--output", default="no-bg", help="folder for the results (default: no-bg)")
    parser.add_argument("--png", action="store_true", help="save PNG instead of lossless WebP")
    parser.add_argument("--overwrite", action="store_true", help="replace results that already exist")
    args = parser.parse_args()

    images = find_images(args.paths)
    if not images:
        print("No image to process.", file=sys.stderr)
        return 1

    try:
        client = pixlub.Client()  # reads PIXLUB_API_KEY
    except pixlub.ConfigurationError:
        print("Set your API key first: export PIXLUB_API_KEY=\"pix....\"", file=sys.stderr)
        print("Create one at https://pixlub.com/en/settings/workspace", file=sys.stderr)
        return 1

    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    failed = 0
    with client:
        for image in images:
            extension = ".png" if args.png else ".webp"
            target = output / f"{image.stem}-no-bg{extension}"
            if target.exists() and not args.overwrite:
                print(f"Skipped {image}: {target} already exists (use --overwrite)")
                continue
            try:
                result = client.tools.run("removeBgApi", image=str(image))
            except (pixlub.AuthenticationError, pixlub.InsufficientCreditsError) as error:
                # Every next file would fail the same way.
                print(f"Stopped: {error}", file=sys.stderr)
                return 1
            except pixlub.PixlubError as error:
                print(f"Failed {image}: {error}", file=sys.stderr)
                failed += 1
                continue
            if args.png:
                to_png(result.image, target)
            else:
                result.save(target, overwrite=True)
            print(f"{image} -> {target}  ({result.cost} credits, {result.credits_balance} left)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
