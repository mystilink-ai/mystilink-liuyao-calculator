"""Optional mystilink.envelope/0.1 wrapping helpers."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, Optional


ENVELOPE_VERSION = "mystilink.envelope/0.1"


def wrap_envelope(
    *,
    system: str,
    chart: Dict[str, Any],
    subject: Optional[Dict[str, Any]] = None,
    locale: Optional[str] = None,
    produced_by: Optional[str] = None,
    interpretation: Optional[Dict[str, Any]] = None,
    request_id: Optional[str] = None,
) -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "schema_version": ENVELOPE_VERSION,
        "system": system,
        "chart": chart,
    }
    if subject is not None:
        out["subject"] = subject
    if locale:
        out["locale"] = locale
    if interpretation is not None:
        out["interpretation"] = interpretation
    meta: Dict[str, Any] = {
        "created_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
    }
    if produced_by:
        meta["produced_by"] = produced_by
    if request_id:
        meta["request_id"] = request_id
    out["meta"] = meta
    return out


def structured_error(code: str, message: str, details: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    err: Dict[str, Any] = {"code": code, "message": message}
    if details is not None:
        err["details"] = details
    return {"error": err}
