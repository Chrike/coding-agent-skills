from __future__ import annotations

import json
import sys
from typing import Any


def read_stdin_json() -> dict[str, Any]:
    try:
        raw = sys.stdin.buffer.read()
        value = json.loads(raw.decode("utf-8") or "{}")
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def json_output(data: dict[str, Any]) -> None:
    payload = json.dumps(data, ensure_ascii=True, separators=(",", ":")).encode("utf-8")
    sys.stdout.buffer.write(payload)
    sys.stdout.buffer.flush()
