# Mystilink Liu Yao Calculator

> Languages: [English](README.md) | [简体中文](README.zh-CN.md)

## Overview

Cast six Liu Yao lines (bottom → top) using a three-coin model. Output is structured chart JSON with original/resulting bitstrings and moving-line flags. Image or CDN assets are not included.

Coin sums: 9 = old yang (moving), 8 = young yang, 7 = young yin, 6 = old yin (moving).

## Platforms and languages

| Target | Delivery |
|--------|----------|
| Python | Installable package `mystilink-liuyao-calculator` and CLI `liuyao` |
| JavaScript / Node | npm package under `bindings/js` (spawns CLI; browser via injectable `runCli`) |
| C | Header + library that invokes the CLI and returns JSON |
| C++ | Thin wrapper over the C API |
| C# | Process wrapper over the CLI |
| Java | ProcessBuilder wrapper over the CLI |

All non-Python bindings call the `liuyao` executable on `PATH` (or `MYSTILINK_LIUYAO_CLI`). The long alias `mystilink-liuyao` remains installed for compatibility.

## Requirements

- Python 3.9 or newer
- For language bindings: the CLI must be installed and available on `PATH`

## Install and quick start

```bash
cd mystilink-liuyao-calculator
python3 -m pip install -e .
liuyao cast --seed 123
```

Also:

```bash
python3 -m mystilink_liuyao cast --throws "9,8,7,6,8,9"
```

## CLI

Default stdout is bare chart JSON (`mystilink.liuyao.chart/0.1`).

```bash
liuyao cast [--seed N] [--throws "9,8,7,6,8,9"] [--envelope] [--locale en]
liuyao version
```

| Option | Description |
|--------|-------------|
| `--seed` | Deterministic RNG seed (ignored when `--throws` is set; output `seed` is then `null`) |
| `--throws` | Six coin sums in `{6,7,8,9}`, comma/colon/space separated |
| `--envelope` | Wrap as `mystilink.envelope/0.1` with `system`=`liuyao` (subject omitted) |
| `--locale` | Locale string when using `--envelope` (default `en`) |

## Python API

```python
from mystilink_liuyao import cast_lines

chart = cast_lines(seed=123)
# or: cast_lines(throws="9,8,7,6,8,9")
print(chart["original_bits"], chart["has_moving"])
```

## Examples

Runnable samples live under `examples/{c,cpp,csharp,java,js,node,python}/`. Binding sources live under `bindings/`. Chart JSON Schema is in `schema/chart.json`.

## Limits

- Coin model matches the product cast script; no hexagram naming or interpretation text is generated.
- Manual `--throws` sets output `seed` to `null`.
- This package does not ship fonts, images, or remote asset lookups.

## License

MIT. See [LICENSE](LICENSE).

## Feedback

Report defects with: CLI version (`liuyao version`), exact command line (fictional seeds only), and stderr/stdout JSON.
