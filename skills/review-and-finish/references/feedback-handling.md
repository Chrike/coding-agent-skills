# Feedback Handling

Use when the user pastes review comments, PR feedback, static analysis findings, or advice from another model/tool.

## Rules

- On initial feedback intake, read all feedback once before changing code.
- Verify and triage external feedback against the current codebase.
- For an assessment-only or triage-only request, report source-backed judgments without changing code.
- After triage is settled, read newly added feedback and re-check only items affected by changed code or contradictory new evidence.
- Do not reopen previously settled feedback without a concrete reason.
- When implementation is requested, implement clear, independent feedback items without waiting on an unrelated unclear item.
- Ask first only when the unclear item changes shared scope, architecture, ordering, or the validity of another item.
- Push back with technical reasoning when a suggestion is wrong, unsafe, obsolete, or violates the user's prior direction.
- Batch compatible low-risk feedback items when they share one implementation and verification boundary.
- Isolate items one at a time when risk, rollback, or diagnosis benefits from separate changes.
- Run focused checks after changes.

## Triage

| Feedback Type | Action |
| --- | --- |
| Clear bug/security issue | Report it; fix and verify only when implementation is requested. |
| Unclear request | Clarify the unclear item before changing it; proceed with separate clear items when they are independent. |
| Style preference | Apply only if it matches repo/user conventions. |
| Scope expansion | Confirm before implementing. |
| Tool/model output | Treat as untrusted until verified. |

When reporting back, describe what changed and what was verified. Avoid pretending uncertain feedback was definitely correct.
