**English** | [Français](README.fr.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Português](README.pt-BR.md) | [Русский](README.ru.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md)

# Remove Image Background with an API (Python)

Remove the background from your photos automatically, one image or a whole folder at a time,
with a small Python script and the [Pixlub](https://pixlub.com) background removal API.
You get a cut-out on a transparent background, as PNG or lossless WebP, ready for product
photos, profile pictures, stickers or design work.

![Before and after: a photo of a pug in a blanket, then the same pug cut out on a transparent background](examples/before-after.jpg)

## Features

- **AI background removal**: the subject is detected automatically, with fine edges on hair and fur.
- **Batch processing**: pass several images or a whole folder.
- **Transparent output**: lossless WebP by default, PNG with `--png`.
- **Clear costs**: each image prints the credits it used and your remaining balance.
- **Short and readable**: about 100 lines of Python on top of the official [`pixlub`](https://pypi.org/project/pixlub/) SDK.

## Requirements

- Python 3.9 or newer
- A Pixlub API key: create one in your [workspace settings](https://pixlub.com/en/settings/workspace).
  API keys need a [paid plan](https://pixlub.com/en/plans).

## Installation

```bash
git clone https://github.com/pixlub/pixlub-remove-background.git
cd pixlub-remove-background
pip install -r requirements.txt
```

Keep your API key in an environment variable, never in your code:

```bash
export PIXLUB_API_KEY="pix.xxxxxxxx.xxxxxxxx..."     # macOS, Linux
$env:PIXLUB_API_KEY = "pix.xxxxxxxx.xxxxxxxx..."     # Windows PowerShell
```

## Usage

```bash
# One image: the result goes to no-bg/photo-no-bg.webp
python remove_background.py photo.jpg

# A whole folder, saved as transparent PNG
python remove_background.py photos/ --output cutouts --png
```

```text
examples/pug.jpg -> no-bg/pug-no-bg.png  (10 credits, 506 left)
```

| Option | Description |
| --- | --- |
| `-o`, `--output` | Folder for the results (default: `no-bg`) |
| `--png` | Save PNG instead of lossless WebP (needs Pillow) |
| `--overwrite` | Replace results that already exist |

Folders are scanned for `.jpg`, `.jpeg`, `.png` and `.webp` files.

## In your own code

```python
import pixlub

client = pixlub.Client()  # reads PIXLUB_API_KEY
result = client.tools.run("removeBgApi", image="photo.jpg")
result.save(f"photo-no-bg{result.extension}")
```

## Price

Background removal costs **10 credits per image**. The cost and your balance are shown
after every image.

## Without code

To remove a background by hand, use the same [AI background remover](https://pixlub.com/en/module/removeBgApi)
on pixlub.com (account required). For a plain, single-colour background (green screen, studio),
the free [solid background remover](https://pixlub.com/en/module/removeBg) runs in your browser,
without uploading your photo.

## Links

- [Getting started with the Pixlub API](https://pixlub.com/en/docs/api/getting-started)
- [Background removal tool reference](https://pixlub.com/en/docs/modules/removeBgApi)
- Official SDKs: [Python](https://pypi.org/project/pixlub/), [Node.js](https://www.npmjs.com/package/pixlub), [Go](https://pkg.go.dev/github.com/pixlub/pixlub-go)

## License

[MIT](LICENSE)
