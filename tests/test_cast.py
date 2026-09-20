# -*- coding: utf-8 -*-
from __future__ import annotations

from mystilink_liuyao.cast import cast_lines


def test_seed_deterministic_lines() -> None:
    a = cast_lines(seed=123)
    b = cast_lines(seed=123)
    assert a["schema_version"] == "mystilink.liuyao.chart/0.1"
    assert a["seed"] == 123
    assert a["order"] == "bottom_to_top"
    assert len(a["lines"]) == 6
    assert [L["sum"] for L in a["lines"]] == [L["sum"] for L in b["lines"]]
    assert a["original_bits"] == b["original_bits"]
    assert a["resulting_bits"] == b["resulting_bits"]
    assert a["has_moving"] == b["has_moving"]


def test_manual_throws() -> None:
    chart = cast_lines(throws="9,8,7,6,8,9")
    assert chart["seed"] is None
    assert [L["sum"] for L in chart["lines"]] == [9, 8, 7, 6, 8, 9]
    assert chart["has_moving"] is True
    assert chart["lines"][0]["label"] == "old_yang"
    assert chart["lines"][3]["label"] == "old_yin"
    assert len(chart["original_bits"]) == 6
    assert chart["resulting_bits"] is not None
