#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from typing import Any


PLUGIN_PREFIX = "capability-harness:"
EXPECTED = {
    "context-scout": [
        "## Capability decision",
        "## Context gaps",
        "## Decision brief",
        "## Evidence",
        "## Plan implications",
    ],
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
    "context-scout",
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


def top_level_lines(message: str) -> set[str]:
    lines: set[str] = set()
    fence_char = ""
    fence_length = 0

    for raw_line in message.splitlines():
        line = raw_line.rstrip()
        candidate = line.lstrip(" ")
        indent = len(line) - len(candidate)

        marker_char = candidate[:1]
        marker_length = 0
        if indent <= 3 and marker_char in {"`", "~"}:
            marker_length = len(candidate) - len(candidate.lstrip(marker_char))

        if fence_char:
            remainder = candidate[marker_length:]
            if marker_char == fence_char and marker_length >= fence_length and not remainder.strip():
                fence_char = ""
                fence_length = 0
            continue

        if marker_length >= 3:
            fence_char = marker_char
            fence_length = marker_length
            continue

        lines.add(line.casefold())

    return lines


def has_heading(lines: set[str], heading: str) -> bool:
    return heading.casefold() in lines


def main() -> int:
    event = read_event()
    agent_type = str(event.get("agent_type") or "")
    if not agent_type.startswith(PLUGIN_PREFIX):
        return 0

    local_name = agent_type[len(PLUGIN_PREFIX) :]
    if local_name not in EXPECTED or bool(event.get("stop_hook_active")):
        return 0

    message = str(event.get("last_assistant_message") or "")
    lines = top_level_lines(message)
    if local_name in BLOCKABLE and has_heading(lines, "## Blocked brief") and has_heading(lines, "## Required next input"):
        return 0
    if local_name == "context-scout" and has_heading(lines, "## Capability decision") and has_heading(
        lines, "## Skip reason"
    ):
        return 0

    missing = [heading for heading in EXPECTED[local_name] if not has_heading(lines, heading)]
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
