[English](README.md) | **Français** | [Deutsch](README.de.md) | [Español](README.es.md) | [Português](README.pt-BR.md) | [Русский](README.ru.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md)

# Supprimer l'arrière-plan d'une image avec une API (Python)

Supprimez automatiquement le fond de vos photos, image par image ou un dossier entier d'un coup,
avec un petit script Python et l'API de détourage de [Pixlub](https://pixlub.com/fr).
Vous obtenez un détourage sur fond transparent, en PNG ou en WebP sans perte, prêt pour
les photos produit, les photos de profil, les stickers ou la création graphique.

![Avant et après : la photo d'un carlin dans une couverture, puis le même carlin détouré sur fond transparent](examples/before-after.jpg)

## Fonctionnalités

- **Détourage par IA** : le sujet est détecté automatiquement, avec des contours fins sur les cheveux et les poils.
- **Traitement par lots** : plusieurs images ou un dossier entier.
- **Fond transparent** : WebP sans perte par défaut, PNG avec `--png`.
- **Coût visible** : chaque image affiche les crédits utilisés et le solde restant.
- **Court et lisible** : une centaine de lignes de Python avec le SDK officiel [`pixlub`](https://pypi.org/project/pixlub/).

## Prérequis

- Python 3.9 ou plus récent
- Une clé API Pixlub : créez-la dans les [réglages de votre espace](https://pixlub.com/fr/settings/workspace).
  Les clés API nécessitent un [abonnement payant](https://pixlub.com/fr/plans).

## Installation

```bash
git clone https://github.com/pixlub/pixlub-remove-background.git
cd pixlub-remove-background
pip install -r requirements.txt
```

Gardez votre clé API dans une variable d'environnement, jamais dans votre code :

```bash
export PIXLUB_API_KEY="pix.xxxxxxxx.xxxxxxxx..."     # macOS, Linux
$env:PIXLUB_API_KEY = "pix.xxxxxxxx.xxxxxxxx..."     # Windows PowerShell
```

## Utilisation

```bash
# Une image : le résultat va dans no-bg/photo-no-bg.webp
python remove_background.py photo.jpg

# Un dossier entier, enregistré en PNG transparent
python remove_background.py photos/ --output detourages --png
```

```text
examples/pug.jpg -> no-bg/pug-no-bg.png  (10 credits, 506 left)
```

| Option | Description |
| --- | --- |
| `-o`, `--output` | Dossier des résultats (par défaut : `no-bg`) |
| `--png` | Enregistre en PNG au lieu du WebP sans perte (nécessite Pillow) |
| `--overwrite` | Remplace les résultats déjà présents |

Dans un dossier, les fichiers `.jpg`, `.jpeg`, `.png` et `.webp` sont traités.

## Dans votre propre code

```python
import pixlub

client = pixlub.Client()  # lit PIXLUB_API_KEY
result = client.tools.run("removeBgApi", image="photo.jpg")
result.save(f"photo-no-bg{result.extension}")
```

## Prix

Le détourage coûte **10 crédits par image**. Le coût et votre solde s'affichent après chaque image.

## Sans code

Pour détourer à la main, utilisez le même [outil de suppression de fond par IA](https://pixlub.com/fr/module/removeBgApi)
sur pixlub.com (compte requis). Pour un fond uni d'une seule couleur (fond vert, studio),
l'outil gratuit [Retirer un fond uni](https://pixlub.com/fr/module/removeBg) fonctionne dans votre navigateur,
sans envoyer votre photo.

## Liens

- [Premiers pas avec l'API Pixlub](https://pixlub.com/fr/docs/api/getting-started)
- [Référence de l'outil de détourage](https://pixlub.com/fr/docs/modules/removeBgApi)
- SDK officiels : [Python](https://pypi.org/project/pixlub/), [Node.js](https://www.npmjs.com/package/pixlub), [Go](https://pkg.go.dev/github.com/pixlub/pixlub-go)

## Licence

[MIT](LICENSE)
