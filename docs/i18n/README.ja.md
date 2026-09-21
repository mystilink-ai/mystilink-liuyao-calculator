# Mystilink 六爻計算機

> Languages: [English](../../README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Français](README.fr.md) | [Español](README.es.md)

## 概要

三枚硬貨モデルで六爻（下から上）を起卦します。出力は本卦/変卦のビット列と動爻フラグを含む構造化チャート JSON です。画像や CDN アセットは含まれません。

硬貨の合計：9 = 老陽（動）、8 = 少陽、7 = 少陰、6 = 老陰（動）。

## プラットフォームと言語

| 対象 | 提供物 |
|------|--------|
| Python | インストール可能なパッケージ `mystilink-liuyao-calculator` と CLI `liuyao` |
| JavaScript / Node | `bindings/js` 配下の npm パッケージ（CLI を起動；ブラウザは注入可能な `runCli`） |
| C | CLI を呼び出して JSON を返すヘッダ + ライブラリ |
| C++ | C API 上の薄いラッパー |
| C# | CLI のプロセスラッパー |
| Java | CLI の ProcessBuilder ラッパー |

Python 以外のバインディングはすべて `PATH` 上の `liuyao`（または `MYSTILINK_LIUYAO_CLI`）を呼び出します。互換のため長い別名 `mystilink-liuyao` もインストールされます。

## 要件

- Python 3.9 以降
- 言語バインディング：CLI がインストールされ `PATH` で利用可能であること

## インストールとクイックスタート

```bash
cd mystilink-liuyao-calculator
python3 -m pip install -e .
liuyao cast --seed 123
```

または：

```bash
python3 -m mystilink_liuyao cast --throws "9,8,7,6,8,9"
```

## CLI

デフォルトの stdout は裸のチャート JSON（`mystilink.liuyao.chart/0.1`）です。

```bash
liuyao cast [--seed N] [--throws "9,8,7,6,8,9"] [--envelope] [--locale en]
liuyao version
```

| オプション | 説明 |
|-----------|------|
| `--seed` | 決定論的 RNG シード（`--throws` 設定時は無視；そのとき出力 `seed` は `null`） |
| `--throws` | 六つの硬貨合計、`{6,7,8,9}`、カンマ/コロン/空白区切り |
| `--envelope` | `mystilink.envelope/0.1` で包む（`system`=`liuyao`；subject は省略） |
| `--locale` | `--envelope` 使用時のロケール文字列（デフォルト `en`） |

## Python API

```python
from mystilink_liuyao import cast_lines

chart = cast_lines(seed=123)
# or: cast_lines(throws="9,8,7,6,8,9")
print(chart["original_bits"], chart["has_moving"])
```

## 例

実行可能なサンプルは `examples/{c,cpp,csharp,java,js,node,python}/` にあります。バインディングソースは `bindings/` にあります。チャート JSON Schema は `schema/chart.json` にあります。

## 制限

- 硬貨モデルは製品の起卦スクリプトに一致します；卦名や解釈文は生成されません。
- 手動 `--throws` では出力 `seed` が `null` になります。
- 本パッケージはフォント、画像、リモートアセット検索を同梱しません。

## ライセンス

MIT。[LICENSE](../../LICENSE) を参照。

## フィードバック

不具合報告時は次を添付：CLI バージョン（`liuyao version`）、正確なコマンドライン（架空のシードのみ）、stderr/stdout JSON。
