#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys


LIB = Path(__file__).resolve().parent / "lib"
sys.path.insert(0, str(LIB))

from common import candidate_actions, classify_prompt, json_output, read_stdin_json  # noqa: E402


def main() -> int:
    event = read_stdin_json()
    prompt = str(event.get("prompt") or "")
    if "[harness:off]" in prompt.lower():
        return 0

    classification = classify_prompt(prompt)
    if not classification["substantive"]:
        context = (
            "Capability harness routing: this prompt appears low-complexity. Answer directly. "
            "Do not add search, subagents, or review unless the request itself makes them necessary."
        )
    else:
        candidates = [name for name, enabled in candidate_actions(classification).items() if enabled]
        context = (
            "Capability-harness preflight: before materially generating, modifying, or recommending, identify the single "
            "highest-impact unknown or quality risk. Decide whether an external action can provide a signal that would "
            "change the approach or result. Then choose either the direct path or the smallest useful capability: local "
            "inspection, bounded context discovery, focused evidence research, an independent alternative, observable "
            "verification, or evaluation of an actual artifact. Candidate signals are leads, not requirements: "
            f"{', '.join(candidates) if candidates else 'none'}. "
            "Do not run a search, Context Pack, agent, or review merely because it is available. Do not defer the decision "
            "until after implementation. Keep the active domain method in control, preserve the user prompt, and state "
            "the selected route and reason only when it helps make a material decision observable."
        )

    json_output(
        {
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": context,
            }
        }
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
