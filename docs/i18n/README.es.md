# Mystilink Calculadora Liu Yao

> Languages: [English](../../README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Français](README.fr.md) | [Español](README.es.md)

## Resumen

Lanza seis líneas Liu Yao (abajo → arriba) con un modelo de tres monedas. La salida es JSON de chart estructurado con cadenas de bits originales/resultantes e indicadores de líneas móviles. No se incluyen imágenes ni recursos CDN.

Sumas de monedas: 9 = yang viejo (móvil), 8 = yang joven, 7 = yin joven, 6 = yin viejo (móvil).

## Plataformas e idiomas

| Objetivo | Entrega |
|----------|----------|
| Python | Paquete instalable `mystilink-liuyao-calculator` y CLI `liuyao` |
| JavaScript / Node | Paquete npm bajo `bindings/js` (lanza el CLI; navegador vía `runCli` inyectable) |
| C | Cabecera + biblioteca que invoca el CLI y devuelve JSON |
| C++ | Envoltorio ligero sobre la API C |
| C# | Envoltorio de proceso sobre el CLI |
| Java | Envoltorio ProcessBuilder sobre el CLI |

Todos los enlaces no Python llaman al ejecutable `liuyao` en `PATH` (o `MYSTILINK_LIUYAO_CLI`). El alias largo `mystilink-liuyao` sigue instalándose por compatibilidad.

## Requisitos

- Python 3.9 o superior
- Para enlaces de lenguaje: el CLI debe estar instalado y disponible en `PATH`

## Instalación e inicio rápido

```bash
cd mystilink-liuyao-calculator
python3 -m pip install -e .
liuyao cast --seed 123
```

También:

```bash
python3 -m mystilink_liuyao cast --throws "9,8,7,6,8,9"
```

## CLI

El stdout predeterminado es JSON de chart desnudo (`mystilink.liuyao.chart/0.1`).

```bash
liuyao cast [--seed N] [--throws "9,8,7,6,8,9"] [--envelope] [--locale en]
liuyao version
```

| Opción | Descripción |
|--------|-------------|
| `--seed` | Semilla RNG determinista (se ignora si se define `--throws`; entonces la salida `seed` es `null`) |
| `--throws` | Seis sumas de monedas en `{6,7,8,9}`, separadas por coma/dos puntos/espacio |
| `--envelope` | Envolver como `mystilink.envelope/0.1` con `system`=`liuyao` (subject omitido) |
| `--locale` | Cadena de configuración regional al usar `--envelope` (predeterminado `en`) |

## API de Python

```python
from mystilink_liuyao import cast_lines

chart = cast_lines(seed=123)
# or: cast_lines(throws="9,8,7,6,8,9")
print(chart["original_bits"], chart["has_moving"])
```

## Ejemplos

Las muestras ejecutables están en `examples/{c,cpp,csharp,java,js,node,python}/`. Las fuentes de enlaces están en `bindings/`. El JSON Schema del chart está en `schema/chart.json`.

## Límites

- El modelo de monedas coincide con el script de tirada del producto; no se genera nombre de hexagrama ni texto de interpretación.
- `--throws` manual fija la salida `seed` en `null`.
- Este paquete no incluye tipografías, imágenes ni búsquedas de recursos remotos.

## Licencia

MIT. Véase [LICENSE](../../LICENSE).

## Comentarios

Informe defectos con: versión CLI (`liuyao version`), línea de comando exacta (solo semillas ficticias) y JSON stderr/stdout.
