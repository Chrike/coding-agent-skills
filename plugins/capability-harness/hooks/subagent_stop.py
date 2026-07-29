#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from typing import Any


PLUGIN_PREFIX = "capability-harness:"
EXPECTED = {
    "evidence-researcher": ["## Findings", "## Evidence"],
    "independent-brancher": [
        "## Approach",
        "## Assumptions",
        "## Plan",
        "## Strengths",
        "## Failure conditions",
        "## Validation",
    ],
    "execution-verifier": [
        "## Verification target",
        "## Checks executed",
        "## Evidence result",
    ],
    "skeptical-evaluator": [
        "## Hard-constraint verdict",
        "## Comparative judgment",
        "## Decisive evidence",
    ],
}
BLOCKABLE = {
    "evidence-researcher",
    "independent-brancher",
    "skeptical-evaluator",
}


def read_event() -> dict[str, Any]:
    try:
        value = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        return {}
    return value if isinstance(value, dict) else {}


def has_heading(message: str, heading: str) -> bool:
    return heading.casefold() in message.casefold()


def main() -> int:
    event = read_event()
    agent_type = str(event.get("agent_type") or "")
    if not agent_type.startswith(PLUGIN_PREFIX):
        return 0

    local_name = agent_type.removeprefix(PLUGIN_PREFIX)
    if local_name not in EXPECTED or bool(event.get("stop_hook_active")):
        return 0

    message = str(event.get("last_assistant_message") or "")
    if local_name in BLOCKABLE and has_heading(message, "## Blocked brief") and has_heading(message, "## Required next input"):
        return 0

    missing = [heading for heading in EXPECTED[local_name] if not has_heading(message, heading)]
    if not missing:
        return 0

    reason = (
        f"Return the result using the required {agent_type} contract. "
        f"Missing headings: {', '.join(missing)}. "
        "Keep the response bounded, evidence-based, and free of delegation."
    )
    json.dump({"decision": "block", "reason": reason}, sys.stdout, ensure_ascii=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
