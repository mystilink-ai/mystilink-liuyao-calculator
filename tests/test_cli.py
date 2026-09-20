# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "mystilink_liuyao", *args],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )


def test_cli_cast_smoke() -> None:
    proc = _run("cast", "--seed", "123")
    assert proc.returncode == 0, proc.stderr
    data = json.loads(proc.stdout)
    assert data["schema_version"] == "mystilink.liuyao.chart/0.1"
    assert data["seed"] == 123
    assert len(data["lines"]) == 6
    assert "ok" not in data


def test_cli_throws() -> None:
    proc = _run("cast", "--throws", "9,8,7,6,8,9")
    assert proc.returncode == 0, proc.stderr
    data = json.loads(proc.stdout)
    assert data["seed"] is None
    assert data["has_moving"] is True


def test_cli_envelope() -> None:
    proc = _run("cast", "--seed", "123", "--envelope", "--locale", "en")
    assert proc.returncode == 0, proc.stderr
    data = json.loads(proc.stdout)
    assert data["schema_version"] == "mystilink.envelope/0.1"
    assert data["system"] == "liuyao"
    assert data["chart"]["schema_version"] == "mystilink.liuyao.chart/0.1"
    assert "subject" not in data


def test_cli_version() -> None:
    proc = _run("version")
    assert proc.returncode == 0, proc.stderr
    data = json.loads(proc.stdout)
    assert data["version"] == "0.1.0"
    assert data["cli"] == "liuyao"
