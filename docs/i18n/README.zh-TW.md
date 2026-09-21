# Mystilink 六爻計算器

> Languages: [English](../../README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Français](README.fr.md) | [Español](README.es.md)

## 概述

以三枚銅錢模型起卦六爻（自下而上）。輸出為結構化卦象 JSON，含本卦/變卦位元串與動爻標記。不包含圖片或 CDN 資源。

銅錢點數：9 = 老陽（動）、8 = 少陽、7 = 少陰、6 = 老陰（動）。

## 平台與語言

| 目標 | 交付 |
|------|------|
| Python | 可安裝套件 `mystilink-liuyao-calculator` 與 CLI `liuyao` |
| JavaScript / Node | `bindings/js` 下的 npm 套件（拉起 CLI；瀏覽器透過可注入的 `runCli`） |
| C | 標頭檔 + 呼叫 CLI 並回傳 JSON 的函式庫 |
| C++ | 對 C API 的薄封裝 |
| C# | 對 CLI 的行程封裝 |
| Java | 對 CLI 的 ProcessBuilder 封裝 |

非 Python 綁定均呼叫 `PATH` 上的 `liuyao`（或 `MYSTILINK_LIUYAO_CLI`）。長別名 `mystilink-liuyao` 仍會安裝以保持相容。

## 環境需求

- Python 3.9 或更高
- 語言綁定：CLI 須已安裝並可在 `PATH` 中找到

## 安裝與快速開始

```bash
cd mystilink-liuyao-calculator
python3 -m pip install -e .
liuyao cast --seed 123
```

亦可：

```bash
python3 -m mystilink_liuyao cast --throws "9,8,7,6,8,9"
```

## CLI

預設 stdout 為裸卦象 JSON（`mystilink.liuyao.chart/0.1`）。

```bash
liuyao cast [--seed N] [--throws "9,8,7,6,8,9"] [--envelope] [--locale en]
liuyao version
```

| 選項 | 說明 |
|------|------|
| `--seed` | 確定性隨機種子（使用 `--throws` 時忽略；此時輸出 `seed` 為 `null`） |
| `--throws` | 六個銅錢點數，取值 `{6,7,8,9}`，可用逗號/冒號/空格分隔 |
| `--envelope` | 包裝為 `mystilink.envelope/0.1`，`system`=`liuyao`（可省略 subject） |
| `--locale` | 使用 `--envelope` 時的 locale（預設 `en`） |

## Python API

```python
from mystilink_liuyao import cast_lines

chart = cast_lines(seed=123)
# or: cast_lines(throws="9,8,7,6,8,9")
print(chart["original_bits"], chart["has_moving"])
```

## 範例

可執行範例位於 `examples/{c,cpp,csharp,java,js,node,python}/`。綁定原始碼位於 `bindings/`。卦象 JSON Schema 見 `schema/chart.json`。

## 限制

- 銅錢模型與產品起卦腳本一致；不產生卦名或解讀文案。
- 手工 `--throws` 時輸出 `seed` 為 `null`。
- 本套件不附帶字型、圖片或遠端資源查詢。

## 授權

MIT。見 [LICENSE](../../LICENSE)。

## 問題回報

回報缺陷時請附帶：CLI 版本（`liuyao version`）、完整命令列（僅使用虛構種子）、以及 stderr/stdout JSON。
