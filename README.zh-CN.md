[English](README.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Português](README.pt-BR.md) | [Русский](README.ru.md) | **中文** | [日本語](README.ja.md)

# 使用 API 去除图片背景（Python）

借助一个简短的 Python 脚本和 [Pixlub](https://pixlub.com) 抠图 API，自动去除照片背景，
可以处理单张图片，也可以一次处理整个文件夹。
输出为透明背景的抠图结果（PNG 或无损 WebP），可直接用于商品图、头像、贴纸和设计。

![处理前后对比：裹着毯子的巴哥犬照片，以及抠出后放在透明背景上的同一只巴哥犬](examples/before-after.jpg)

## 功能

- **AI 智能抠图**：自动识别主体，头发和毛发边缘细腻。
- **批量处理**：可传入多张图片或整个文件夹。
- **透明背景**：默认输出无损 WebP，加上 `--png` 输出 PNG。
- **费用清晰**：每张图片都会显示消耗的积分和剩余余额。
- **简短易读**：基于官方 SDK [`pixlub`](https://pypi.org/project/pixlub/)，约 100 行 Python 代码。

## 环境要求

- Python 3.9 或更高版本
- Pixlub API 密钥：在[工作区设置](https://pixlub.com/en/settings/workspace)中创建。
  API 密钥需要[付费套餐](https://pixlub.com/en/plans)。

## 安装

```bash
git clone https://github.com/pixlub/pixlub-remove-background.git
cd pixlub-remove-background
pip install -r requirements.txt
```

请把 API 密钥放在环境变量中，不要写进代码：

```bash
export PIXLUB_API_KEY="pix.xxxxxxxx.xxxxxxxx..."     # macOS、Linux
$env:PIXLUB_API_KEY = "pix.xxxxxxxx.xxxxxxxx..."     # Windows PowerShell
```

## 使用方法

```bash
# 单张图片：结果保存为 no-bg/photo-no-bg.webp
python remove_background.py photo.jpg

# 整个文件夹，保存为透明 PNG
python remove_background.py photos/ --output cutouts --png
```

```text
examples/pug.jpg -> no-bg/pug-no-bg.png  (10 credits, 506 left)
```

| 选项 | 说明 |
| --- | --- |
| `-o`, `--output` | 结果保存目录（默认：`no-bg`） |
| `--png` | 保存为 PNG 而不是无损 WebP（需要 Pillow） |
| `--overwrite` | 覆盖已存在的结果 |

处理文件夹时，会处理其中的 `.jpg`、`.jpeg`、`.png` 和 `.webp` 文件。

## 在你自己的代码中使用

```python
import pixlub

client = pixlub.Client()  # 读取 PIXLUB_API_KEY
result = client.tools.run("removeBgApi", image="photo.jpg")
result.save(f"photo-no-bg{result.extension}")
```

## 价格

去除背景每张图片消耗 **10 积分**。每处理完一张图片都会显示费用和余额。

## 无需编程

如需手动抠图，可在 pixlub.com 使用同一个 [AI 去背景工具](https://pixlub.com/en/module/removeBgApi)（需要账号）。
对于单一纯色背景（绿幕、影棚），免费的[纯色背景去除工具](https://pixlub.com/en/module/removeBg)
直接在浏览器中运行，不会上传你的照片。

## 链接

- [Pixlub API 入门](https://pixlub.com/en/docs/api/getting-started)
- [抠图工具参考文档](https://pixlub.com/en/docs/modules/removeBgApi)
- 官方 SDK：[Python](https://pypi.org/project/pixlub/)、[Node.js](https://www.npmjs.com/package/pixlub)、[Go](https://pkg.go.dev/github.com/pixlub/pixlub-go)

## 许可证

[MIT](LICENSE)
