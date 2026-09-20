#!/usr/bin/env python3
"""Minimal Python example using the installed package."""
from mystilink_liuyao import cast_lines

chart = cast_lines(seed=123)
print("schema:", chart["schema_version"])
print("bits:", chart["original_bits"], "moving:", chart["has_moving"])
