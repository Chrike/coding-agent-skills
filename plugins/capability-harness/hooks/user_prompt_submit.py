#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from typing import Any


def read_event() -> dict[str, Any]:
    try:
        value = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        return {}
    return value if isinstance(value, dict) else {}


def main() -> int:
    event = read_event()
    prompt = str(event.get("prompt") or "")
    if "[harness:off]" in prompt.lower():
        return 0

    context = (
        "Capability Harness is available as /capability-harness:capability-harness. "
        "Decide from the task's meaning, not keywords, length, or installed capability alone, whether current evidence, "
        "a materially independent alternative, observable verification, or skeptical evaluation could materially improve the result. "
        "If so, invoke it and select only the useful modules. Otherwise continue directly. "
        "Do not start a second controller when another workflow owns the scope."
    )
    output = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": context,
        }
    }
    json.dump(output, sys.stdout, ensure_ascii=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
