#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys


LIB = Path(__file__).resolve().parent / "lib"
sys.path.insert(0, str(LIB))

from common import (  # noqa: E402
    SCHEMA_VERSION,
    classify_prompt,
    derive_requirements,
    hash_text,
    json_output,
    prune_state,
    project_path,
    read_stdin_json,
    save_state,
    transcript_offset,
    utc_now,
)


def main() -> int:
    event = read_stdin_json()
    prompt = str(event.get("prompt") or "")
    if "[harness:off]" in prompt.lower():
        return 0

    cwd = project_path(event.get("cwd"))
    session_id = str(event.get("session_id") or "unknown")
    classification = classify_prompt(prompt)
    requirements = derive_requirements(classification)
    state = {
        "schema_version": SCHEMA_VERSION,
        "session_id": session_id,
        "cwd": str(cwd),
        "prompt": prompt,
        "prompt_hash": hash_text(prompt),
        "started_at": utc_now(),
        "transcript_path": str(event.get("transcript_path") or ""),
        "transcript_offset": transcript_offset(event.get("transcript_path")),
        "classification": classification,
        "requirements": requirements,
        "route": "",
        "harness": "",
        "route_reason": "",
        "stop_blocks": 0,
        "last_stop_reason": "",
    }
    save_state(session_id, cwd, state)
    prune_state(cwd)

    if not classification["substantive"]:
        context = (
            "Capability harness routing: this prompt appears low-complexity. Answer directly. "
            "Do not add search, subagents, or review unless the request itself makes them necessary."
        )
    else:
        classification_signals = [
            name for name, enabled in classification.items() if enabled and name != "substantive"
        ]
        requirement_signals = [name for name, enabled in requirements.items() if enabled]
        context_rule = (
            "For this open-ended quality-sensitive task, invoke capability-harness:context-scout before generating or recommending. "
            "Ask it to search direct, component, and adjacent questions and return a compact Context Pack; do not require the user to add those details to the prompt. "
            if requirements.get("context_enrichment")
            else ""
        )
        context = (
            "Apply the capability-harness protocol for this substantive turn. "
            "Capability harness routing context: "
            "Build a compact task contract and choose only the smallest module that can materially change the result. "
            f"Classification signals: {', '.join(classification_signals) if classification_signals else 'none'}. "
            f"Required checks: {', '.join(requirement_signals) if requirement_signals else 'none'}. "
            "Inspect project facts before generic guidance when relevant; verify current or version-specific claims; "
            "run observable checks for implementation work; use independent alternatives or evaluation only for material trade-offs. "
            f"{context_rule}"
            "For open-ended design, recommendation, or quality decisions, prefer one focused WebSearch/WebFetch pass "
            "with official, primary, or directly applicable sources when it can materially improve the result. "
            "Do not launch all workers by default or create a second controller. "
            "At completion, report the route, whether the Harness was used, and the reason it was skipped or selected."
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
