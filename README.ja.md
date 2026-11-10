[English](README.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Português](README.pt-BR.md) | [Русский](README.ru.md) | [中文](README.zh-CN.md) | **日本語**

# API で画像の背景を削除する（Python）

小さな Python スクリプトと [Pixlub](https://pixlub.com) の背景削除 API で、写真の背景を自動で削除します。
1 枚ずつでも、フォルダごとまとめてでも処理できます。
透過背景の切り抜き画像（PNG またはロスレス WebP）が得られ、商品写真、プロフィール画像、
ステッカー、デザインにそのまま使えます。

![ビフォーアフター：毛布にくるまったパグの写真と、透過背景に切り抜かれた同じパグ](examples/before-after.jpg)

## 特長

- **AI による背景削除**：被写体を自動で検出し、髪の毛や毛並みの輪郭もきれいに切り抜きます。
- **一括処理**：複数の画像やフォルダ全体を指定できます。
- **透過背景**：標準はロスレス WebP、`--png` で PNG を出力します。
- **わかりやすい料金**：画像ごとに使用クレジットと残高を表示します。
- **短く読みやすい**：公式 SDK [`pixlub`](https://pypi.org/project/pixlub/) を使った約 100 行の Python です。

## 必要なもの

- Python 3.9 以降
- Pixlub の API キー：[ワークスペース設定](https://pixlub.com/en/settings/workspace)で作成します。
  API キーには[有料プラン](https://pixlub.com/en/plans)が必要です。

## インストール

```bash
git clone https://github.com/pixlub/pixlub-remove-background.git
cd pixlub-remove-background
pip install -r requirements.txt
```

API キーはコードに書かず、環境変数に設定してください：

```bash
export PIXLUB_API_KEY="pix.xxxxxxxx.xxxxxxxx..."     # macOS、Linux
$env:PIXLUB_API_KEY = "pix.xxxxxxxx.xxxxxxxx..."     # Windows PowerShell
```

## 使い方

```bash
# 1 枚の画像：結果は no-bg/photo-no-bg.webp に保存されます
python remove_background.py photo.jpg

# フォルダ全体を透過 PNG で保存
python remove_background.py photos/ --output cutouts --png
```

```text
examples/pug.jpg -> no-bg/pug-no-bg.png  (10 credits, 506 left)
```

| オプション | 説明 |
| --- | --- |
| `-o`, `--output` | 結果の保存先フォルダ（既定：`no-bg`） |
| `--png` | ロスレス WebP の代わりに PNG で保存（Pillow が必要） |
| `--overwrite` | 既存の結果を上書き |

フォルダ内の `.jpg`、`.jpeg`、`.png`、`.webp` ファイルが処理されます。

## 自分のコードで使う

```python
import pixlub

client = pixlub.Client()  # PIXLUB_API_KEY を読み込みます
result = client.tools.run("removeBgApi", image="photo.jpg")
result.save(f"photo-no-bg{result.extension}")
```

## 料金

背景削除は **1 枚あたり 10 クレジット**です。画像ごとに料金と残高が表示されます。

## コードを書かずに使う

手作業で背景を削除するには、pixlub.com の同じ [AI 背景削除ツール](https://pixlub.com/en/module/removeBgApi)を使えます（アカウントが必要）。
単色の背景（グリーンバック、スタジオ）なら、無料の[単色背景削除ツール](https://pixlub.com/en/module/removeBg)が
ブラウザ内で動作し、写真をアップロードしません。

## リンク

- [Pixlub API 入門](https://pixlub.com/en/docs/api/getting-started)
- [背景削除ツールのリファレンス](https://pixlub.com/en/docs/modules/removeBgApi)
- 公式 SDK：[Python](https://pypi.org/project/pixlub/)、[Node.js](https://www.npmjs.com/package/pixlub)、[Go](https://pkg.go.dev/github.com/pixlub/pixlub-go)

## ライセンス

[MIT](LICENSE)
