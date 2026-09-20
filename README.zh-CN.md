# Mystilink 六爻计算器

> Languages: [English](README.md) | [简体中文](README.zh-CN.md)

## 概述

以三枚铜钱模型起卦六爻（自下而上）。输出为结构化卦象 JSON，含本卦/变卦比特串与动爻标记。不包含图片或 CDN 资源。

铜钱点数：9 = 老阳（动）、8 = 少阳、7 = 少阴、6 = 老阴（动）。

## 平台与语言

| 目标 | 交付 |
|------|------|
| Python | 可安装包 `mystilink-liuyao-calculator` 与 CLI `liuyao` |
| JavaScript / Node | `bindings/js` 下的 npm 包（拉起 CLI；浏览器通过可注入的 `runCli`） |
| C | 头文件 + 调用 CLI 并返回 JSON 的库 |
| C++ | 对 C API 的薄封装 |
| C# | 对 CLI 的进程封装 |
| Java | 对 CLI 的 ProcessBuilder 封装 |

非 Python 绑定均调用 `PATH` 上的 `liuyao`（或 `MYSTILINK_LIUYAO_CLI`）。长别名 `mystilink-liuyao` 仍会安装以保持兼容。

## 要求

- Python 3.9 或更高
- 语言绑定：CLI 须已安装并可在 `PATH` 中找到

## 安装与快速开始

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

默认 stdout 为裸卦象 JSON（`mystilink.liuyao.chart/0.1`）。

```bash
liuyao cast [--seed N] [--throws "9,8,7,6,8,9"] [--envelope] [--locale en]
liuyao version
```

| 选项 | 说明 |
|------|------|
| `--seed` | 确定性随机种子（使用 `--throws` 时忽略；此时输出 `seed` 为 `null`） |
| `--throws` | 六个铜钱点数，取值 `{6,7,8,9}`，可用逗号/冒号/空格分隔 |
| `--envelope` | 包装为 `mystilink.envelope/0.1`，`system`=`liuyao`（可省略 subject） |
| `--locale` | 使用 `--envelope` 时的 locale（默认 `en`） |

## Python API

```python
from mystilink_liuyao import cast_lines

chart = cast_lines(seed=123)
# 或: cast_lines(throws="9,8,7,6,8,9")
print(chart["original_bits"], chart["has_moving"])
```

## 示例

可运行示例位于 `examples/{c,cpp,csharp,java,js,node,python}/`。绑定源码位于 `bindings/`。卦象 JSON Schema 见 `schema/chart.json`。

## 限制

- 铜钱模型与产品起卦脚本一致；不生成卦名或解读文案。
- 手工 `--throws` 时输出 `seed` 为 `null`。
- 本包不附带字体、图片或远程资源查询。

## 许可

MIT。见 [LICENSE](LICENSE)。

## 反馈

报告缺陷时请附带：CLI 版本（`liuyao version`）、完整命令行（仅使用虚构种子）、以及 stderr/stdout JSON。
