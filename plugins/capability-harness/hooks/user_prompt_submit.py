#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys


LIB = Path(__file__).resolve().parent / "lib"
sys.path.insert(0, str(LIB))

from common import (  # noqa: E402
    classify_prompt,
    json_output,
    read_stdin_json,
    select_pre_action_route,
)


def route_context(route: str, reason: str, external_discovery_disallowed: bool = False) -> str:
    contract = (
        "This is a selected pre-action route, not a generic suggestion. Before material work, the active controller "
        "must execute exactly this one route once. If the route is unavailable, unsafe, or its bounded result is not useful, "
        "return the route's explicit skip or unavailable-evidence outcome and then continue; do not silently omit it, "
        "and do not add unrelated workers or a post-hoc completion gate. "
    )
    if route == "project_inspection":
        external_follow_up = (
            "External discovery is disabled for this prompt; use local project evidence only."
            if external_discovery_disallowed
            else "If the minimum local inspection exposes one remaining current external uncertainty, use one bounded "
            "capability-harness:evidence-researcher brief for that exact question."
        )
        return (
            "Capability-harness selected pre-action route: project inspection. "
            f"Reason: {reason} {contract}Before materially generating, modifying, or recommending, inspect only the "
            "current files, configuration, history, or local conventions that can change the decision. Do not broaden "
            "inspection mechanically, and do not substitute generic web guidance for repository evidence. "
            f"{external_follow_up}"
        )
    if route == "evidence_research":
        return (
            "Capability-harness selected pre-action route: focused evidence research. "
            f"Reason: {reason} {contract}Before materially generating or recommending, invoke "
            "capability-harness:evidence-researcher once for the one fact that can change the approach. Give it the "
            "original task, exact evidence question, and any explicit source or data constraints. This selected route "
            "authorizes public, non-sensitive research from current official or primary sources; an explicit user source "
            "or network constraint overrides that default. The agent's own contract supplies its return format and stop "
            "condition. Never include private prompts, source code, identifiers, credentials, or repository data in a "
            "query. Use the finding to make the decision, not as a post-hoc citation."
        )
    if route == "context_discovery":
        return (
            "Capability-harness selected pre-action route: bounded context discovery. "
            f"Reason: {reason} {contract}Before material generation or recommendation, invoke "
            "capability-harness:context-scout once with the original request, the one construction, design, or selection "
            "decision it must inform, and any explicit source or data constraints. This selected route authorizes public, "
            "non-sensitive discovery; an explicit user source or network constraint overrides that default. The agent's "
            "own contract supplies its Pre-action Decision Brief format and stop condition. A plausible material "
            "context gap is enough "
            "to search; do not require advance proof that search will improve the result. Use only searches or repository "
            "inspections that inform the selected decision, stop as soon as the Brief has actionable input or information "
            "value is clearly diminishing, and use five focused searches or inspections as an upper bound rather than a "
            "target. Search across direct, component, and adjacent-principle evidence. Do not put private prompt or "
            "repository details into queries. Feed the returned Brief into the construction or selection plan before "
            "material work; do not merely cite it or paste raw results. A scout direct-route skip is the valid basis for "
            "proceeding without search; do not silently downgrade this route because direct generation is faster."
        )
    return (
        "Capability harness routing: this prompt appears adequately specified for a direct path. "
        "Do not add search, subagents, or review unless the request itself makes them necessary."
    )


def main() -> int:
    event = read_stdin_json()
    prompt = str(event.get("prompt") or "")
    if "[harness:off]" in prompt.lower():
        return 0

    classification = classify_prompt(prompt)
    if classification.get("controller_owned"):
        return 0

    route, reason = select_pre_action_route(classification)
    if route == "direct":
        return 0

    context = route_context(route, reason, bool(classification.get("external_discovery_disallowed")))

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
