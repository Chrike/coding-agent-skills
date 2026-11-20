#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys


LIB = Path(__file__).resolve().parent / "lib"
sys.path.insert(0, str(LIB))

from common import has_harness_opt_out, json_output, read_stdin_json  # noqa: E402  # type: ignore[reportMissingImports]


PURE_GREETINGS = frozenset(
    {
        "hi",
        "hello",
        "hey",
        "thanks",
        "thank you",
        "ok",
        "okay",
        "yes",
        "no",
        "你好",
        "嗨",
        "谢谢",
        "好的",
        "可以",
        "是",
        "否",
    }
)
HOST_COMMANDS = ("/security-review", "/code-review", "/adaptive-long-horizon")
ADDITIONAL_CONTEXT = (
    "Capability Harness — choose one route:\n"
    "- Direct: proceed when no independent signal will change the result.\n"
    "- Project inspection: inspect local files, configuration, or history when they control the decision.\n"
    "- Evidence: ask evidence-researcher one bounded evidence question.\n"
    "- Context: ask context-scout one missing-context question before creation or recommendation.\n"
    "- Before material work, briefly state your route and why; use at most one route.\n"
    "- Honor explicit no-search, no-network, and no-agent limits; never disclose private prompts, project data/source code, "
    "identifiers, or secrets to external services."
)


def is_pure_greeting(prompt: str) -> bool:
    return prompt.strip().rstrip(" .!?。！？").casefold() in PURE_GREETINGS


def starts_host_command(prompt: str) -> bool:
    stripped = prompt.lstrip().casefold()
    return any(
        stripped == command or (stripped.startswith(command) and stripped[len(command)].isspace())
        for command in HOST_COMMANDS
    )


def main() -> int:
    event = read_stdin_json()
    prompt = str(event.get("prompt") or "")
    if (
        not prompt.strip()
        or has_harness_opt_out(prompt)
        or is_pure_greeting(prompt)
        or starts_host_command(prompt)
    ):
        return 0

    json_output(
        {
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": ADDITIONAL_CONTEXT,
            }
        }
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
