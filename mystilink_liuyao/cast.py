# -*- coding: utf-8 -*-
"""Liu Yao six casts — coin model (ported from mystilink-liuyao-skill)."""
from __future__ import annotations

import re
import secrets
from typing import Any, Callable, Dict, List, Optional, Sequence, Union

SCHEMA_VERSION = "mystilink.liuyao.chart/0.1"
NAMES = ["chu", "er", "san", "si", "wu", "shang"]
VALID_SUMS = {6, 7, 8, 9}


def _imul(a: int, b: int) -> int:
    return ((a & 0xFFFFFFFF) * (b & 0xFFFFFFFF)) & 0xFFFFFFFF


def mulberry32(seed: int) -> Callable[[], float]:
    state = seed & 0xFFFFFFFF

    def rand() -> float:
        nonlocal state
        state = (state + 0x6D2B79F5) & 0xFFFFFFFF
        t = state
        t = _imul(t ^ (t >> 15), t | 1)
        t = (t ^ ((t + _imul(t ^ (t >> 7), t | 61)) & 0xFFFFFFFF)) & 0xFFFFFFFF
        return ((t ^ (t >> 14)) & 0xFFFFFFFF) / 4294967296.0

    return rand


def line_from_sum(sum_v: int) -> Dict[str, Any]:
    if sum_v == 9:
        return {"yin_yang": "yang", "moving": True, "label": "old_yang", "sum": sum_v}
    if sum_v == 8:
        return {"yin_yang": "yang", "moving": False, "label": "young_yang", "sum": sum_v}
    if sum_v == 7:
        return {"yin_yang": "yin", "moving": False, "label": "young_yin", "sum": sum_v}
    if sum_v == 6:
        return {"yin_yang": "yin", "moving": True, "label": "old_yin", "sum": sum_v}
    raise ValueError(f"invalid coin sum {sum_v}")


def random_throw(rand: Callable[[], float]) -> int:
    total = 0
    for _ in range(3):
        total += 3 if rand() < 0.5 else 2
    return total


def random_seed() -> int:
    return secrets.randbelow((2**31 - 1) - 1) + 1


def parse_throws(raw: str) -> List[int]:
    parts = [p for p in re.split(r"[,:\s]+", raw.strip()) if p]
    sums = [int(p) for p in parts]
    if len(sums) != 6 or any(n not in VALID_SUMS for n in sums):
        raise ValueError("throws must be six values in {6,7,8,9}")
    return sums


def cast_lines(
    *,
    seed: Optional[int] = None,
    throws: Optional[Union[Sequence[int], str]] = None,
) -> Dict[str, Any]:
    """
    Cast six lines bottom → top.

    When `throws` is provided, `seed` in the output is null (manual throws).
    """
    used_manual = throws is not None

    if used_manual:
        if isinstance(throws, str):
            sums = parse_throws(throws)
        else:
            sums = list(throws)  # type: ignore[arg-type]
            if len(sums) != 6 or any(n not in VALID_SUMS for n in sums):
                raise ValueError("throws must be six values in {6,7,8,9}")
        out_seed: Optional[int] = None
    else:
        if seed is None:
            seed = random_seed()
        out_seed = int(seed)
        rand = mulberry32(out_seed)
        sums = [random_throw(rand) for _ in range(6)]

    lines: List[Dict[str, Any]] = []
    for i, sum_v in enumerate(sums):
        L = line_from_sum(sum_v)
        lines.append(
            {
                "index": i + 1,
                "name": NAMES[i],
                **L,
                "binary": 1 if L["yin_yang"] == "yang" else 0,
            }
        )

    has_moving = any(L["moving"] for L in lines)
    if has_moving:
        resulting_bits: Optional[str] = "".join(
            str(L["binary"] ^ 1 if L["moving"] else L["binary"]) for L in lines
        )
    else:
        resulting_bits = None

    return {
        "schema_version": SCHEMA_VERSION,
        "seed": out_seed,
        "order": "bottom_to_top",
        "lines": lines,
        "original_bits": "".join(str(L["binary"]) for L in lines),
        "resulting_bits": resulting_bits,
        "has_moving": has_moving,
        "wiki_hint": {
            "method": "liuyao.method.six-casts",
            "rule": "liuyao.rule.ben-zhi-bian",
            "index": "liuyao.table.64-gua",
            "classics": "shared.work.yijing",
        },
    }
