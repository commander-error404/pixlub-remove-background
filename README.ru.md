[English](README.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Português](README.pt-BR.md) | **Русский** | [中文](README.zh-CN.md) | [日本語](README.ja.md)

# Удаление фона с изображения через API (Python)

Удаляйте фон с фотографий автоматически, по одной или целой папкой за раз,
с помощью небольшого скрипта на Python и API удаления фона [Pixlub](https://pixlub.com).
На выходе получается вырезанный объект на прозрачном фоне, в PNG или WebP без потерь:
для фото товаров, аватарок, стикеров и дизайна.

![До и после: фото мопса в пледе и тот же мопс, вырезанный на прозрачном фоне](examples/before-after.jpg)

## Возможности

- **Удаление фона с помощью ИИ**: объект определяется автоматически, с аккуратными краями на волосах и шерсти.
- **Пакетная обработка**: несколько изображений или целая папка.
- **Прозрачный фон**: по умолчанию WebP без потерь, PNG с флагом `--png`.
- **Понятная стоимость**: для каждого изображения выводятся потраченные кредиты и остаток.
- **Коротко и понятно**: около 100 строк на Python с официальным SDK [`pixlub`](https://pypi.org/project/pixlub/).

## Требования

- Python 3.9 или новее
- API-ключ Pixlub: создайте его в [настройках рабочего пространства](https://pixlub.com/en/settings/workspace).
  Для API-ключей нужен [платный тариф](https://pixlub.com/en/plans).

## Установка

```bash
git clone https://github.com/pixlub/pixlub-remove-background.git
cd pixlub-remove-background
pip install -r requirements.txt
```

Храните API-ключ в переменной окружения, а не в коде:

```bash
export PIXLUB_API_KEY="pix.xxxxxxxx.xxxxxxxx..."     # macOS, Linux
$env:PIXLUB_API_KEY = "pix.xxxxxxxx.xxxxxxxx..."     # Windows PowerShell
```

## Использование

```bash
# Одно изображение: результат сохраняется в no-bg/photo-no-bg.webp
python remove_background.py photo.jpg

# Целая папка, с сохранением в прозрачный PNG
python remove_background.py photos/ --output cutouts --png
```

```text
examples/pug.jpg -> no-bg/pug-no-bg.png  (10 credits, 506 left)
```

| Параметр | Описание |
| --- | --- |
| `-o`, `--output` | Папка для результатов (по умолчанию `no-bg`) |
| `--png` | Сохранять PNG вместо WebP без потерь (нужен Pillow) |
| `--overwrite` | Заменять уже существующие результаты |

В папках обрабатываются файлы `.jpg`, `.jpeg`, `.png` и `.webp`.

## В своём коде

```python
import pixlub

client = pixlub.Client()  # читает PIXLUB_API_KEY
result = client.tools.run("removeBgApi", image="photo.jpg")
result.save(f"photo-no-bg{result.extension}")
```

## Стоимость

Удаление фона стоит **10 кредитов за изображение**. Стоимость и остаток выводятся после каждого изображения.

## Без кода

Чтобы удалить фон вручную, откройте тот же [инструмент удаления фона с ИИ](https://pixlub.com/en/module/removeBgApi)
на pixlub.com (нужна учётная запись). Однотонный фон (хромакей, студия) убирает бесплатный
[инструмент для однотонного фона](https://pixlub.com/en/module/removeBg): он работает прямо в браузере
и не отправляет фото на сервер.

## Ссылки

- [Начало работы с API Pixlub](https://pixlub.com/en/docs/api/getting-started)
- [Справка по инструменту удаления фона](https://pixlub.com/en/docs/modules/removeBgApi)
- Официальные SDK: [Python](https://pypi.org/project/pixlub/), [Node.js](https://www.npmjs.com/package/pixlub), [Go](https://pkg.go.dev/github.com/pixlub/pixlub-go)

## Лицензия

[MIT](LICENSE)
