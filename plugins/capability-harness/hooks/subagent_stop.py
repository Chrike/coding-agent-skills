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


def top_level_lines(message: str) -> list[str]:
    lines: list[str] = []
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

        lines.append(line)

    return lines


def has_heading(lines: list[str], heading: str) -> bool:
    return any(line.casefold() == heading.casefold() for line in lines)


def is_top_level_heading(line: str) -> bool:
    return line.startswith("## ")


def section_body(lines: list[str], heading: str) -> list[str]:
    target = heading.casefold()
    for index, line in enumerate(lines):
        if line.casefold() != target:
            continue
        end = next(
            (candidate_index for candidate_index in range(index + 1, len(lines)) if is_top_level_heading(lines[candidate_index])),
            len(lines),
        )
        return [line.strip() for line in lines[index + 1 : end] if line.strip()]
    return []


def contract_problems(lines: list[str], headings: list[str]) -> list[str]:
    missing = [heading for heading in headings if not has_heading(lines, heading)]
    problems: list[str] = []
    if missing:
        problems.append(f"Missing headings: {', '.join(missing)}")

    positions = [
        next(index for index, line in enumerate(lines) if line.casefold() == heading.casefold())
        for heading in headings
        if has_heading(lines, heading)
    ]
    if positions != sorted(positions):
        problems.append("Required headings are out of order")

    empty = [heading for heading in headings if has_heading(lines, heading) and not section_body(lines, heading)]
    if empty:
        problems.append(f"Empty sections: {', '.join(empty)}")
    return problems


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
    if local_name in BLOCKABLE and (
        has_heading(lines, "## Blocked brief") or has_heading(lines, "## Required next input")
    ):
        problems = contract_problems(lines, ["## Blocked brief", "## Required next input"])
        if not problems:
            if has_heading(lines, "## Skip reason"):
                problems.append("Blocked brief cannot also include a skip contract")
            if any(has_heading(lines, heading) for heading in EXPECTED[local_name]):
                problems.append("Blocked brief cannot also include the normal success contract")
        if not problems:
            return 0
        reason = (
            f"Return the result using the required {agent_type} blocked contract. "
            f"Contract problems: {'; '.join(problems)}. Keep the response bounded and state the missing input."
        )
        json.dump({"decision": "block", "reason": reason}, sys.stdout, ensure_ascii=False)
        return 0

    if local_name == "context-scout" and has_heading(lines, "## Skip reason"):
        problems = contract_problems(lines, ["## Capability decision", "## Skip reason"])
        if not problems:
            normal_only = [heading for heading in EXPECTED[local_name] if heading != "## Capability decision"]
            if any(has_heading(lines, heading) for heading in normal_only):
                problems.append("Skip contract cannot also include normal discovery sections")
            if has_heading(lines, "## Blocked brief") or has_heading(lines, "## Required next input"):
                problems.append("Skip contract cannot also include a blocked contract")
        if not problems:
            return 0
        reason = (
            f"Return the result using the required {agent_type} skip contract. "
            f"Contract problems: {'; '.join(problems)}. Keep the response bounded and explain the skip."
        )
        json.dump({"decision": "block", "reason": reason}, sys.stdout, ensure_ascii=False)
        return 0

    problems = contract_problems(lines, EXPECTED[local_name])
    if not problems:
        return 0

    reason = (
        f"Return the result using the required {agent_type} contract. "
        f"Contract problems: {'; '.join(problems)}. "
        "Keep the response bounded, evidence-based, and free of delegation."
    )
    json.dump({"decision": "block", "reason": reason}, sys.stdout, ensure_ascii=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
