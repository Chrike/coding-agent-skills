---
name: feedback-and-completion
description: Use when the user provides review feedback to evaluate or implement, or asks whether current work is done, fixed, passing, or ready. Do not use for a fresh code, diff, branch, or PR review.
---

# Feedback And Completion

Handle review feedback and completion verification without opening a fresh code review or turning those requests into automatic branch actions.

## First Decision

- If the user explicitly invokes a bundled review command such as `/code-review`, or asks for a fresh code, diff, branch, or PR review, let the host review workflow own that pass instead of duplicating it here.
- User shares feedback: verify each item against the codebase before changing it.
- User asks whether work is done/fixed/passing: reuse current-session verification when it still covers the final code state and claim; otherwise run the smallest missing check or state why verification is unavailable.
- User asks to finish a branch, commit, push, merge, discard, or prepare a PR: hand off to `finish-branch`.
- Ordinary small edit: do not auto-review, commit, push, merge, or start branch cleanup.

Choose the active mode from the user's latest request. Do not blend feedback handling, completion verification, and branch actions unless the user explicitly asks for both completion and branch wrap-up, and route the branch part through `finish-branch`.

When the user provides external feedback or asks whether current work is done, fixed, passing, or ready, prefer this skill's feedback and completion flow over opening a fresh review pass.

## Feedback Handling

Treat external feedback as input to evaluate, not orders to obey. Clarify unclear multi-item feedback before partial implementation. Batch compatible low-risk feedback items when they share one implementation and verification boundary. Isolate items one at a time when risk, rollback, or diagnosis benefits from separate changes.

Use [feedback-handling.md](references/feedback-handling.md) for review-comment workflows.

## Exit To Implementation

- If feedback triage was already completed and the latest request is to implement the settled result, exit this workflow and continue in the base implementation flow.
- Do not repeat feedback intake or re-verify the same settled items unless relevant code changed, new evidence contradicts an item, or the user explicitly asks for another pass.
- During implementation, verify the applied change rather than reopening the settled decision to make that change.

## Completion Claims

For explicit done/fixed/passing requests, reuse current-session verification when it still covers the final code state and the user's acceptance criteria.

Run a new check only when:

- code changed after the previous check
- the previous check does not support the completion claim
- the result is stale or incomplete
- the user explicitly requests a fresh run

Completion review owns the judgment about whether the evidence is sufficient; it does not automatically rerun every check already performed by `test-strategy` or another execution step.

Do not treat "tests pass" as automatic proof that the work is done. Check the result against the user's request, review feedback, or stated acceptance context as well.

For explicit ready/final/finalize/send/ship-style checks on a development artifact such as a release note, migration guide, API document, PR description, or distributable output, use a light delivery gate:

1. State the acceptance context you are checking against.
2. Verify each criterion concretely against the artifact or current evidence.
3. Report `PASS` only when all checked criteria are satisfied.
4. Report `BLOCK` when a required criterion is missing, unsupported, or unverified.

Do not turn ordinary status checks into a delivery gate, and do not invent a heavier workflow when the user only asked whether ordinary work is done.
