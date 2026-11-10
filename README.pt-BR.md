[English](README.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Español](README.es.md) | **Português** | [Русский](README.ru.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md)

# Remover o fundo de uma imagem com uma API (Python)

Remova o fundo das suas fotos automaticamente, uma imagem ou uma pasta inteira de uma vez,
com um pequeno script em Python e a API de remoção de fundo da [Pixlub](https://pixlub.com).
Você recebe um recorte com fundo transparente, em PNG ou WebP sem perdas, pronto para
fotos de produto, fotos de perfil, figurinhas ou design gráfico.

![Antes e depois: a foto de um pug enrolado em um cobertor e o mesmo pug recortado com fundo transparente](examples/before-after.jpg)

## Recursos

- **Recorte com IA**: o objeto é detectado automaticamente, com bordas finas em cabelos e pelos.
- **Processamento em lote**: várias imagens ou uma pasta inteira.
- **Fundo transparente**: WebP sem perdas por padrão, PNG com `--png`.
- **Custo claro**: cada imagem mostra os créditos usados e o saldo restante.
- **Curto e legível**: cerca de 100 linhas de Python com o SDK oficial [`pixlub`](https://pypi.org/project/pixlub/).

## Requisitos

- Python 3.9 ou mais recente
- Uma chave de API da Pixlub: crie nas [configurações do seu espaço de trabalho](https://pixlub.com/en/settings/workspace).
  As chaves de API exigem um [plano pago](https://pixlub.com/en/plans).

## Instalação

```bash
git clone https://github.com/pixlub/pixlub-remove-background.git
cd pixlub-remove-background
pip install -r requirements.txt
```

Guarde sua chave de API em uma variável de ambiente, nunca no código:

```bash
export PIXLUB_API_KEY="pix.xxxxxxxx.xxxxxxxx..."     # macOS, Linux
$env:PIXLUB_API_KEY = "pix.xxxxxxxx.xxxxxxxx..."     # Windows PowerShell
```

## Uso

```bash
# Uma imagem: o resultado vai para no-bg/photo-no-bg.webp
python remove_background.py photo.jpg

# Uma pasta inteira, salva como PNG transparente
python remove_background.py fotos/ --output recortes --png
```

```text
examples/pug.jpg -> no-bg/pug-no-bg.png  (10 credits, 506 left)
```

| Opção | Descrição |
| --- | --- |
| `-o`, `--output` | Pasta dos resultados (padrão: `no-bg`) |
| `--png` | Salva PNG em vez de WebP sem perdas (requer Pillow) |
| `--overwrite` | Substitui resultados que já existem |

Em uma pasta, são processados os arquivos `.jpg`, `.jpeg`, `.png` e `.webp`.

## No seu próprio código

```python
import pixlub

client = pixlub.Client()  # lê PIXLUB_API_KEY
result = client.tools.run("removeBgApi", image="photo.jpg")
result.save(f"photo-no-bg{result.extension}")
```

## Preço

A remoção de fundo custa **10 créditos por imagem**. O custo e o seu saldo aparecem depois de cada imagem.

## Sem código

Para remover um fundo manualmente, use o mesmo [removedor de fundo com IA](https://pixlub.com/en/module/removeBgApi)
no pixlub.com (conta necessária). Para um fundo liso de uma só cor (tela verde, estúdio),
a ferramenta gratuita [para fundos lisos](https://pixlub.com/en/module/removeBg) funciona no seu navegador,
sem enviar sua foto.

## Links

- [Primeiros passos com a API da Pixlub](https://pixlub.com/en/docs/api/getting-started)
- [Referência da ferramenta de recorte](https://pixlub.com/en/docs/modules/removeBgApi)
- SDKs oficiais: [Python](https://pypi.org/project/pixlub/), [Node.js](https://www.npmjs.com/package/pixlub), [Go](https://pkg.go.dev/github.com/pixlub/pixlub-go)

## Licença

[MIT](LICENSE)
