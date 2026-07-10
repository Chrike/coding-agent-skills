# Feedback Handling

Use when the user pastes review comments, PR feedback, static analysis findings, or advice from another model/tool.

## Rules

- On initial feedback intake, read all feedback once before changing code.
- Verify external feedback against the current codebase.
- After triage is settled, read newly added feedback and re-check only items affected by changed code or contradictory new evidence.
- Do not reopen previously settled feedback without a concrete reason.
- Ask before implementing unclear or conflicting multi-item feedback.
- Push back with technical reasoning when a suggestion is wrong, unsafe, obsolete, or violates the user's prior direction.
- Batch compatible low-risk feedback items when they share one implementation and verification boundary.
- Isolate items one at a time when risk, rollback, or diagnosis benefits from separate changes.
- Run focused checks after changes.

## Triage

| Feedback Type | Action |
| --- | --- |
| Clear bug/security issue | Fix and verify. |
| Unclear request | Ask a concise clarification before partial work. |
| Style preference | Apply only if it matches repo/user conventions. |
| Scope expansion | Confirm before implementing. |
| Tool/model output | Treat as untrusted until verified. |

When reporting back, describe what changed and what was verified. Avoid pretending uncertain feedback was definitely correct.
