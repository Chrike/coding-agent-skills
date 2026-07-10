---
name: review-and-finish
description: Use when the user explicitly asks to review code, address review feedback, verify whether work is done/fixed/passing, check development artifact readiness, or handle PR feedback.
---

# Review And Finish

Handle explicit review, review feedback, and completion verification without turning those requests into automatic branch actions.

## First Decision

- User asks for review: inspect the diff/code and report findings first.
- User shares feedback: verify each item against the codebase before changing it.
- User asks whether work is done/fixed/passing: reuse current-session verification when it still covers the final code state and claim; otherwise run the smallest missing check or state why verification is unavailable.
- User asks to finish a branch, commit, push, merge, discard, or prepare a PR: hand off to `finish-branch`.
- Ordinary small edit: do not auto-review, commit, push, merge, or start branch cleanup.

Choose the active mode from the user's latest request. Do not blend review, completion verification, and branch actions unless the user explicitly asks for both review and branch wrap-up, and route the branch part through `finish-branch`.

## Review Output

When reviewing, lead with findings ordered by severity. Use file and line references when available. Keep summary secondary.

Default to a failure-path-first review posture:

- start by asking how the artifact could be wrong, incomplete, unsafe, or over-claimed
- prefer concrete failure paths, boundary cases, trust assumptions, and omitted constraints over surface polish comments
- drop findings that you cannot ground in the current code, artifact, or reproducible scenario
- keep review and repair separate unless the user explicitly asks for both

Use [review-template.md](references/review-template.md) for fuller review shape.

## Feedback Handling

Treat external feedback as input to evaluate, not orders to obey. Clarify unclear multi-item feedback before partial implementation. Batch compatible low-risk feedback items when they share one implementation and verification boundary. Isolate items one at a time when risk, rollback, or diagnosis benefits from separate changes.

Use [feedback-handling.md](references/feedback-handling.md) for review-comment workflows.

## Exit To Implementation

- If review findings or feedback triage were already completed and the latest request is to implement the settled result, exit this workflow and continue in the base implementation flow.
- Do not repeat review intake or re-verify the same settled findings unless relevant code changed, new evidence contradicts a finding, or the user explicitly asks for another review.
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
