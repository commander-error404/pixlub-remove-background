[English](README.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | **Español** | [Português](README.pt-BR.md) | [Русский](README.ru.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md)

# Quitar el fondo de una imagen con una API (Python)

Quita el fondo de tus fotos automáticamente, una imagen o una carpeta entera a la vez,
con un pequeño script de Python y la API de eliminación de fondos de [Pixlub](https://pixlub.com).
Obtienes un recorte sobre fondo transparente, en PNG o WebP sin pérdida, listo para
fotos de producto, fotos de perfil, stickers o diseño gráfico.

![Antes y después: la foto de un pug envuelto en una manta y el mismo pug recortado sobre fondo transparente](examples/before-after.jpg)

## Características

- **Recorte con IA**: el sujeto se detecta automáticamente, con bordes finos en el pelo y el pelaje.
- **Procesamiento por lotes**: varias imágenes o una carpeta entera.
- **Fondo transparente**: WebP sin pérdida por defecto, PNG con `--png`.
- **Costes claros**: cada imagen muestra los créditos usados y el saldo restante.
- **Corto y legible**: unas 100 líneas de Python con el SDK oficial [`pixlub`](https://pypi.org/project/pixlub/).

## Requisitos

- Python 3.9 o posterior
- Una clave de API de Pixlub: créala en los [ajustes de tu espacio de trabajo](https://pixlub.com/en/settings/workspace).
  Las claves de API requieren un [plan de pago](https://pixlub.com/en/plans).

## Instalación

```bash
git clone https://github.com/pixlub/pixlub-remove-background.git
cd pixlub-remove-background
pip install -r requirements.txt
```

Guarda tu clave de API en una variable de entorno, nunca en el código:

```bash
export PIXLUB_API_KEY="pix.xxxxxxxx.xxxxxxxx..."     # macOS, Linux
$env:PIXLUB_API_KEY = "pix.xxxxxxxx.xxxxxxxx..."     # Windows PowerShell
```

## Uso

```bash
# Una imagen: el resultado va a no-bg/photo-no-bg.webp
python remove_background.py photo.jpg

# Una carpeta entera, guardada como PNG transparente
python remove_background.py fotos/ --output recortes --png
```

```text
examples/pug.jpg -> no-bg/pug-no-bg.png  (10 credits, 506 left)
```

| Opción | Descripción |
| --- | --- |
| `-o`, `--output` | Carpeta de resultados (por defecto: `no-bg`) |
| `--png` | Guarda PNG en lugar de WebP sin pérdida (requiere Pillow) |
| `--overwrite` | Reemplaza los resultados que ya existen |

En una carpeta se procesan los archivos `.jpg`, `.jpeg`, `.png` y `.webp`.

## En tu propio código

```python
import pixlub

client = pixlub.Client()  # lee PIXLUB_API_KEY
result = client.tools.run("removeBgApi", image="photo.jpg")
result.save(f"photo-no-bg{result.extension}")
```

## Precio

Quitar el fondo cuesta **10 créditos por imagen**. El coste y tu saldo se muestran después de cada imagen.

## Sin código

Para quitar un fondo a mano, usa el mismo [eliminador de fondos con IA](https://pixlub.com/en/module/removeBgApi)
en pixlub.com (se necesita una cuenta). Para un fondo liso de un solo color (pantalla verde, estudio),
la herramienta gratuita [para fondos lisos](https://pixlub.com/en/module/removeBg) funciona en tu navegador,
sin subir tu foto.

## Enlaces

- [Primeros pasos con la API de Pixlub](https://pixlub.com/en/docs/api/getting-started)
- [Referencia de la herramienta de recorte](https://pixlub.com/en/docs/modules/removeBgApi)
- SDK oficiales: [Python](https://pypi.org/project/pixlub/), [Node.js](https://www.npmjs.com/package/pixlub), [Go](https://pkg.go.dev/github.com/pixlub/pixlub-go)

## Licencia

[MIT](LICENSE)
