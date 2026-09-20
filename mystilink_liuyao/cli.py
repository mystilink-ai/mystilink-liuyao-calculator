# -*- coding: utf-8 -*-
"""CLI for Mystilink Liu Yao calculator. Prints JSON to stdout on success."""
from __future__ import annotations

import argparse
import json
import sys
from importlib.metadata import PackageNotFoundError, version
from typing import Any, Optional

from mystilink_liuyao.cast import cast_lines
from mystilink_liuyao.envelope import structured_error, wrap_envelope

PACKAGE_NAME = "mystilink-liuyao-calculator"
FALLBACK_VERSION = "0.1.0"
SYSTEM = "liuyao"


def get_version() -> str:
    try:
        return version(PACKAGE_NAME)
    except PackageNotFoundError:
        return FALLBACK_VERSION


def _print_json(data: Any) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2))


def _emit_error(message: str, *, code: str, use_envelope: bool, exit_code: int = 1) -> None:
    if use_envelope:
        _print_json(structured_error(code, message))
    else:
        print(json.dumps({"error": message}, ensure_ascii=False), file=sys.stderr)
    raise SystemExit(exit_code)


def cmd_cast(args: argparse.Namespace) -> None:
    use_envelope = bool(args.envelope)
    try:
        chart = cast_lines(seed=args.seed, throws=args.throws)
    except ValueError as exc:
        _emit_error(str(exc), code="invalid_argument", use_envelope=use_envelope)

    if use_envelope:
        out = wrap_envelope(
            system=SYSTEM,
            chart=chart,
            subject=None,
            locale=args.locale,
            produced_by=f"{PACKAGE_NAME}@{get_version()}",
        )
        _print_json(out)
    else:
        _print_json(chart)


def cmd_version(_: argparse.Namespace) -> None:
    _print_json({"version": get_version(), "cli": "liuyao", "package": PACKAGE_NAME})


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="liuyao", description="Mystilink Liu Yao calculator")
    sub = parser.add_subparsers(dest="command", required=True)

    p_cast = sub.add_parser("cast", help="Cast six lines (bottom to top)")
    p_cast.add_argument("--seed", type=int, default=None, help="Deterministic RNG seed")
    p_cast.add_argument(
        "--throws",
        default=None,
        help='Manual six coin sums, e.g. "9,8,7,6,8,9" (values in {6,7,8,9})',
    )
    p_cast.add_argument(
        "--envelope",
        action="store_true",
        help="Wrap chart as mystilink.envelope/0.1 (system=liuyao)",
    )
    p_cast.add_argument("--locale", default="en", help="Locale for envelope (default: en)")
    p_cast.set_defaults(func=cmd_cast)

    p_ver = sub.add_parser("version", help="Print package version JSON")
    p_ver.set_defaults(func=cmd_version)

    return parser


def main(argv: Optional[list[str]] = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
