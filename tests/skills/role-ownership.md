# Skill Role Ownership

This file records which skills remain main-session methods and why. It is maintenance evidence, not a runtime catalog and not a requirement to create one Agent per skill.

| Skill | Primary owner | Agent extraction decision |
| --- | --- | --- |
| `plan-work` | Main session | Keep the planning result contiguous with implementation; no generic planner Agent. |
| `design-codebase` | Main session | Keep final architecture and ownership decisions with the implementation owner; independent option analysis remains an optional future role only when a caller and output consumer exist. |
| `debug-systematically` | Main session | Keep the modify-run-observe loop together; a failure-path investigator is optional only for a bounded caller with a concrete evidence consumer. |
| `test-strategy` | Main session | Keep test seam and acceptance decisions with the implementation flow; do not create a generic test Agent. |
| `reliability-check` | Main session | It depends on the user's correction, current stage, and conversation history; an isolated Agent cannot replace that context. |
| `review-and-finish` | Main session | It owns feedback triage, repair, completion/readiness judgment, and branch-action separation; `fresh-findings-reviewer` is an optional bounded findings producer, not the owner of review completion. |
| `agent-workflow` | Main session method / Workflow glue | It owns decomposition, handoff, integration, and stop rules; stable leaf roles are separate Agents. |
| `finish-branch`, `memory-handoff`, `issue-workflow`, `markdown-memory`, `decision-map`, `skill-refactorer` | Main session | Authorization, durable state, user intent, or maintenance scope must remain with the controlling session; no independent Agent caller is currently required. |

A new Agent requires a bounded input, a distinct tool or context boundary, a structured output consumer, and a focused positive/negative/safety check. Directory symmetry alone is not sufficient.
