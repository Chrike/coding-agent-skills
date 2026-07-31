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
    if route == "project_inspection":
        external_follow_up = (
            "External discovery is disabled for this prompt; use local project evidence only."
            if external_discovery_disallowed
            else "If local inspection exposes one remaining current external uncertainty, use one bounded "
            "capability-harness:evidence-researcher brief for that exact question."
        )
        return (
            "Capability-harness selected pre-action route: project inspection. "
            f"Reason: {reason} Before materially generating, modifying, or recommending, inspect the relevant "
            "current files, configuration, history, and local conventions. Do not substitute generic web guidance "
            f"for repository evidence. {external_follow_up}"
        )
    if route == "evidence_research":
        return (
            "Capability-harness selected pre-action route: focused evidence research. "
            f"Reason: {reason} Before materially generating or recommending, invoke "
            "capability-harness:evidence-researcher once for the one fact that can change the approach. Its brief must "
            "include the original task, exact evidence question, public official-or-primary source scope, public "
            "non-sensitive network authorization, a Findings/Evidence return, and a stop condition of answering that "
            "one question. Never include private prompts, source code, identifiers, credentials, or repository data in a "
            "query. Use the finding to make the decision, not as a post-hoc citation."
        )
    if route == "context_discovery":
        return (
            "Capability-harness selected pre-action route: bounded context discovery. "
            f"Reason: {reason} Before material generation or recommendation, invoke "
            "capability-harness:context-scout once with the original request and the one construction, design, or "
            "selection decision it must inform. Its brief must state public, non-sensitive network authorization and "
            "return a Pre-action Decision Brief with context gaps, findings, applicability, plan implications, and "
            "uncertainty. A plausible material context gap is enough to search; do not require advance proof that the "
            "search will improve the result. Stop after 3-5 focused public searches or when the brief has actionable "
            "input. Search across direct, component, and adjacent-principle evidence. Do not put private prompt or "
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
    if classification.get("workflow_owned"):
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
