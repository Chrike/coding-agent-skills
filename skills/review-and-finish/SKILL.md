---
name: review-and-finish
description: Use when the user explicitly asks to review code, address review feedback, verify whether work is done/fixed/passing, or handle PR feedback.
---

# Review And Finish

Handle explicit review, review feedback, and completion verification without turning those requests into automatic branch actions.

## First Decision

- User asks for review: inspect the diff/code and report findings first.
- User shares feedback: verify each item against the codebase before changing it.
- User asks whether work is done/fixed/passing: verify with a fresh command or state why verification is unavailable.
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

Treat external feedback as input to evaluate, not orders to obey. Clarify unclear multi-item feedback before partial implementation. Implement verified items one at a time and run focused checks.

Use [feedback-handling.md](references/feedback-handling.md) for review-comment workflows.

## Exit To Implementation

- If review findings or feedback triage were already completed and the latest request is to implement the settled result, exit this workflow and continue in the base implementation flow.
- Do not repeat review intake or re-verify the same settled findings unless relevant code changed, new evidence contradicts a finding, or the user explicitly asks for another review.
- During implementation, verify the applied change rather than reopening the settled decision to make that change.

## Completion Claims

For explicit done/fixed/passing requests, verify with a fresh command or observation when practical and proportionate, then report the actual result, including skipped checks.

Do not treat "tests pass" as automatic proof that the work is done. Check the result against the user's request, review feedback, or stated acceptance context as well.

For explicit ready/final/finalize/send/ship-style checks on an external-facing artifact, use a light delivery gate:

1. State the acceptance context you are checking against.
2. Verify each criterion concretely against the artifact or current evidence.
3. Report `PASS` only when all checked criteria are satisfied.
4. Report `BLOCK` when a required criterion is missing, unsupported, or unverified.

Do not turn ordinary status checks into a delivery gate, and do not invent a heavier workflow when the user only asked whether ordinary work is done.
