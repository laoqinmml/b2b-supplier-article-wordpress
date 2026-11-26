"""Convert one screenshot/photo to WebP without changing its source."""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageOps


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--lossy', action='store_true')
    parser.add_argument('--quality', type=int, default=88)
    parser.add_argument('--max-width', type=int)
    args = parser.parse_args()
    if args.output.suffix.lower() != '.webp':
        parser.error('Output extension must be .webp')
    if args.source.resolve() == args.output.resolve() or args.output.exists():
        parser.error('Choose a new output path; never overwrite the source or an existing file')
    if not 0 <= args.quality <= 100 or (args.max_width is not None and args.max_width < 1):
        parser.error('Invalid quality or width')
    with Image.open(args.source) as original:
        oriented = ImageOps.exif_transpose(original)
        image = oriented.convert('RGBA' if 'A' in oriented.getbands() or 'transparency' in oriented.info else 'RGB')
        if args.max_width and image.width > args.max_width:
            image.thumbnail((args.max_width, max(1, round(image.height * args.max_width / image.width))), Image.Resampling.LANCZOS)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        image.save(args.output, 'WEBP', lossless=not args.lossy, quality=args.quality, method=6)
        with Image.open(args.output) as result:
            assert result.format == 'WEBP' and result.size == image.size
            if not args.lossy:
                assert result.convert(image.mode).tobytes() == image.tobytes(), 'Pixel verification failed'
    print(json.dumps({'output': str(args.output.resolve()), 'format': 'WEBP', 'size': image.size,
                      'bytes': args.output.stat().st_size, 'lossless': not args.lossy}))


if __name__ == '__main__':
    main()
