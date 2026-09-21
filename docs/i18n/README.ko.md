# Mystilink 육효 계산기

> Languages: [English](../../README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Français](README.fr.md) | [Español](README.es.md)

## 개요

세 개의 동전 모델로 육효(아래→위)를 기괘합니다. 출력은 본괘/변괘 비트열과 동효 플래그가 포함된 구조화 차트 JSON 입니다. 이미지나 CDN 자산은 포함되지 않습니다.

동전 합: 9 = 노양(동), 8 = 소양, 7 = 소음, 6 = 노음(동).

## 플랫폼 및 언어

| 대상 | 제공물 |
|------|--------|
| Python | 설치 가능 패키지 `mystilink-liuyao-calculator` 및 CLI `liuyao` |
| JavaScript / Node | `bindings/js` 아래 npm 패키지(CLI 실행; 브라우저는 주입 가능한 `runCli`) |
| C | CLI 를 호출해 JSON 을 반환하는 헤더 + 라이브러리 |
| C++ | C API 위의 얇은 래퍼 |
| C# | CLI 프로세스 래퍼 |
| Java | CLI ProcessBuilder 래퍼 |

Python 외 바인딩은 모두 `PATH` 상의 `liuyao`(또는 `MYSTILINK_LIUYAO_CLI`)를 호출합니다. 호환을 위해 긴 별칭 `mystilink-liuyao` 도 설치됩니다.

## 요구 사항

- Python 3.9 이상
- 언어 바인딩: CLI 가 설치되어 `PATH` 에서 사용 가능해야 함

## 설치 및 빠른 시작

```bash
cd mystilink-liuyao-calculator
python3 -m pip install -e .
liuyao cast --seed 123
```

또한:

```bash
python3 -m mystilink_liuyao cast --throws "9,8,7,6,8,9"
```

## CLI

기본 stdout 은 원시 차트 JSON(`mystilink.liuyao.chart/0.1`)입니다.

```bash
liuyao cast [--seed N] [--throws "9,8,7,6,8,9"] [--envelope] [--locale en]
liuyao version
```

| 옵션 | 설명 |
|------|------|
| `--seed` | 결정적 RNG 시드(`--throws` 설정 시 무시; 이때 출력 `seed` 는 `null`) |
| `--throws` | 여섯 동전 합, `{6,7,8,9}`, 쉼표/콜론/공백 구분 |
| `--envelope` | `mystilink.envelope/0.1` 로 감쌈(`system`=`liuyao`; subject 생략) |
| `--locale` | `--envelope` 사용 시 locale 문자열(기본 `en`) |

## Python API

```python
from mystilink_liuyao import cast_lines

chart = cast_lines(seed=123)
# or: cast_lines(throws="9,8,7,6,8,9")
print(chart["original_bits"], chart["has_moving"])
```

## 예제

실행 가능 샘플은 `examples/{c,cpp,csharp,java,js,node,python}/` 에 있습니다. 바인딩 소스는 `bindings/` 에 있습니다. 차트 JSON Schema 는 `schema/chart.json` 에 있습니다.

## 제한

- 동전 모델은 제품 기괘 스크립트와 일치합니다; 괘명이나 해석 텍스트는 생성되지 않습니다.
- 수동 `--throws` 는 출력 `seed` 를 `null` 로 만듭니다.
- 이 패키지는 글꼴, 이미지, 원격 자산 조회를 포함하지 않습니다.

## 라이선스

MIT. [LICENSE](../../LICENSE) 참조.

## 피드백

결함 보고 시 첨부: CLI 버전(`liuyao version`), 정확한 명령줄(가상 시드만), stderr/stdout JSON.
