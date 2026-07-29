#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys


LIB = Path(__file__).resolve().parent / "lib"
sys.path.insert(0, str(LIB))

from common import (  # noqa: E402
    extract_tool_names,
    json_output,
    load_state,
    normalized_tool_tokens,
    read_stdin_json,
    read_transcript_delta,
    project_path,
    route_report,
    save_state,
)


def main() -> int:
    event = read_stdin_json()
    cwd = project_path(event.get("cwd"))
    session_id = str(event.get("session_id") or "unknown")
    state = load_state(session_id, cwd)
    classification = state.get("classification", {})
    if not state or not classification.get("substantive"):
        return 0

    # Claude may retry a Stop hook. Challenge completion at most once per turn.
    if bool(event.get("stop_hook_active")) or int(state.get("stop_blocks", 0)) >= 1:
        return 0

    report = route_report(str(event.get("last_assistant_message") or ""))
    if report:
        state.update(report)

    delta = read_transcript_delta(
        state.get("transcript_path"),
        int(state.get("transcript_offset", 0)),
    )
    tools = normalized_tool_tokens(extract_tool_names(delta))
    requirements = state.get("requirements", {})
    missing: list[str] = []

    if requirements.get("project_inspection") and "inspect" not in tools:
        missing.append(
            "inspect the relevant project files or explicitly explain why the task is not project-dependent"
        )
    if requirements.get("observable_check") and "execute" not in tools:
        missing.append(
            "run an observable non-destructive check, or explicitly state why execution is impossible and what remains unverified"
        )
    if requirements.get("context_enrichment") and "context" not in tools:
        missing.append(
            "obtain one bounded Context Pack from capability-harness:context-scout, or explicitly state why context enrichment is unavailable and what quality risk remains"
        )
    if requirements.get("focused_web_guidance") and "web" not in tools:
        missing.append(
            "perform one focused WebSearch/WebFetch pass using official or primary sources, or explicitly state why external guidance cannot materially change the result"
        )
    if requirements.get("independent_branch_or_evaluation") and not ({"branch", "evaluate"} & tools):
        missing.append(
            "obtain one independent alternative or skeptical evaluation from the named Harness agent, or explicitly justify why it could not materially change the result"
        )

    if not missing:
        if report:
            save_state(session_id, cwd, state)
        return 0

    reason = (
        "Before finalizing this substantive turn, "
        + "; ".join(missing)
        + ". Preserve the current best result and avoid repeating completed work."
    )
    state["stop_blocks"] = int(state.get("stop_blocks", 0)) + 1
    state["last_stop_reason"] = reason
    save_state(session_id, cwd, state)
    json_output({"decision": "block", "reason": reason})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
