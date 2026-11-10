[English](README.md) | [Français](README.fr.md) | **Deutsch** | [Español](README.es.md) | [Português](README.pt-BR.md) | [Русский](README.ru.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md)

# Bildhintergrund per API entfernen (Python)

Entfernen Sie den Hintergrund Ihrer Fotos automatisch, einzeln oder für einen ganzen Ordner auf einmal,
mit einem kleinen Python-Skript und der Hintergrundentfernungs-API von [Pixlub](https://pixlub.com).
Sie erhalten ein freigestelltes Motiv auf transparentem Hintergrund, als PNG oder verlustfreies WebP,
bereit für Produktfotos, Profilbilder, Sticker oder Grafikdesign.

![Vorher und nachher: das Foto eines Mopses in einer Decke, dann derselbe Mops freigestellt auf transparentem Hintergrund](examples/before-after.jpg)

## Funktionen

- **Freistellen mit KI**: Das Motiv wird automatisch erkannt, mit feinen Kanten bei Haaren und Fell.
- **Stapelverarbeitung**: mehrere Bilder oder ein ganzer Ordner.
- **Transparenter Hintergrund**: standardmäßig verlustfreies WebP, PNG mit `--png`.
- **Klare Kosten**: Zu jedem Bild werden die verbrauchten Credits und das Restguthaben angezeigt.
- **Kurz und lesbar**: rund 100 Zeilen Python mit dem offiziellen SDK [`pixlub`](https://pypi.org/project/pixlub/).

## Voraussetzungen

- Python 3.9 oder neuer
- Ein Pixlub-API-Schlüssel: Erstellen Sie ihn in den [Workspace-Einstellungen](https://pixlub.com/en/settings/workspace).
  API-Schlüssel erfordern einen [kostenpflichtigen Tarif](https://pixlub.com/en/plans).

## Installation

```bash
git clone https://github.com/pixlub/pixlub-remove-background.git
cd pixlub-remove-background
pip install -r requirements.txt
```

Bewahren Sie Ihren API-Schlüssel in einer Umgebungsvariable auf, nie im Code:

```bash
export PIXLUB_API_KEY="pix.xxxxxxxx.xxxxxxxx..."     # macOS, Linux
$env:PIXLUB_API_KEY = "pix.xxxxxxxx.xxxxxxxx..."     # Windows PowerShell
```

## Verwendung

```bash
# Ein Bild: Das Ergebnis landet in no-bg/photo-no-bg.webp
python remove_background.py photo.jpg

# Ein ganzer Ordner, als transparentes PNG gespeichert
python remove_background.py fotos/ --output freigestellt --png
```

```text
examples/pug.jpg -> no-bg/pug-no-bg.png  (10 credits, 506 left)
```

| Option | Beschreibung |
| --- | --- |
| `-o`, `--output` | Ordner für die Ergebnisse (Standard: `no-bg`) |
| `--png` | Speichert PNG statt verlustfreiem WebP (benötigt Pillow) |
| `--overwrite` | Ersetzt bereits vorhandene Ergebnisse |

In Ordnern werden `.jpg`-, `.jpeg`-, `.png`- und `.webp`-Dateien verarbeitet.

## Im eigenen Code

```python
import pixlub

client = pixlub.Client()  # liest PIXLUB_API_KEY
result = client.tools.run("removeBgApi", image="photo.jpg")
result.save(f"photo-no-bg{result.extension}")
```

## Preis

Die Hintergrundentfernung kostet **10 Credits pro Bild**. Kosten und Guthaben werden nach jedem Bild angezeigt.

## Ohne Code

Zum Freistellen von Hand nutzen Sie denselben [KI-Hintergrundentferner](https://pixlub.com/en/module/removeBgApi)
auf pixlub.com (Konto erforderlich). Für einen einfarbigen Hintergrund (Greenscreen, Studio)
läuft der kostenlose [Entferner für einfarbige Hintergründe](https://pixlub.com/en/module/removeBg) in Ihrem Browser,
ohne Ihr Foto hochzuladen.

## Links

- [Erste Schritte mit der Pixlub-API](https://pixlub.com/en/docs/api/getting-started)
- [Referenz des Freistellungs-Tools](https://pixlub.com/en/docs/modules/removeBgApi)
- Offizielle SDKs: [Python](https://pypi.org/project/pixlub/), [Node.js](https://www.npmjs.com/package/pixlub), [Go](https://pkg.go.dev/github.com/pixlub/pixlub-go)

## Lizenz

[MIT](LICENSE)
