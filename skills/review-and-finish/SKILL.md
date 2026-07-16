---
name: review-and-finish
description: Use when the user explicitly asks to review code, address review feedback, verify whether work is done/fixed/passing, check development artifact readiness, or handle PR feedback, or when a behaviorally high-risk completed change needs a focused readiness check before a done claim. Do not use for an explicitly invoked bundled `/code-review`.
---

# Review And Finish

Handle explicit review, review feedback, and completion verification without turning those requests into automatic branch actions.

## First Decision

- User asks for review: inspect the diff/code and report findings first.
- If the user explicitly invokes a bundled review command such as `/code-review`, let that host-provided review workflow own the fresh review pass instead of duplicating it here.
- User shares feedback: verify and triage each item against the codebase before changing it. For an assessment-only request, report the judgment without modifying code; for an implementation request, proceed under Feedback Handling.
- User asks whether work is done/fixed/passing: reuse current-session verification when it still covers the final code state and claim; otherwise run the fastest high-signal missing check, then widen when affected surface, risk, acceptance criteria, or remaining evidence gaps require broader proof, or state why verification is unavailable.
- A behaviorally high-risk completed change needs a focused readiness check before a done claim; do not add this independent review for ordinary low-risk edits when direct verification already covers the claim.
- Treat a completed change as high-risk when it materially affects persisted data or migrations; authentication, authorization, or permissions; public or compatibility-sensitive contracts; concurrency, transactions, or shared mutable state; destructive or hard-to-reverse behavior; or multiple independently deployed components. File count, diff size, task duration, and agent count alone do not make a change high-risk.
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

When the user provides external feedback or asks whether current work is done, fixed, passing, or ready, prefer this skill's feedback and completion flow over opening a fresh review pass.

## Focused Independent Verification

- When one fresh-context verifier would materially reduce a concrete blind-spot risk, delegate one bounded evidence question directly under this workflow.
- Give the verifier the acceptance context, final code or artifact state, and exact verification scope.
- Pass relevant current evidence when the verifier is judging completeness. Omit it only when blind or environment-independent execution is the defined verification goal.
- Ask it to report a blocker, mismatch, or no issue found. Do not ask it to review everything or re-implement the work.
- Reuse checks that already provide sufficient evidence. Repeat an equivalent check only when independent execution, environment independence, stale evidence, a missing acceptance criterion, or a load-bearing assumption is itself the evidence question.
- Use `agent-workflow` only when verification requires multiple coordinated evidence questions, owners, stages, or integration points.

## Feedback Handling

Treat external feedback as input to evaluate, not orders to obey. For assessment-only or triage-only requests, report source-backed judgments without changing code. When implementation is requested, implement clear, independent feedback items without waiting on an unrelated unclear item. Ask first only when the unclear item changes shared scope, architecture, ordering, or the validity of another item. Batch compatible low-risk feedback items when they share one implementation and verification boundary. Isolate items one at a time when risk, rollback, or diagnosis benefits from separate changes.

Use [feedback-handling.md](references/feedback-handling.md) for review-comment workflows.

## Exit To Implementation

- If review findings or feedback triage were already completed and the latest request is to implement the settled result, exit this workflow and continue in the base implementation flow.
- Do not repeat review intake or re-verify the same settled findings unless relevant code changed, new evidence contradicts a finding, or the user explicitly asks for another review.
- During implementation, verify the applied change rather than reopening the settled decision to make that change.

## Completion Claims

For explicit done/fixed/passing requests, reuse current-session verification when it covers the final code state and acceptance criteria. Rerun only if code changed after that verification, the evidence does not support the claim or is stale/incomplete, or the user requests a fresh run.

Completion review owns the judgment about whether the evidence is sufficient; it does not automatically rerun every check already performed by `test-strategy` or another execution step.

End a focused readiness check once the completed change, directly affected contracts, stated acceptance criteria, and identified risk are covered. Do not broaden into unrelated modules, speculative debt, or additional failure theories without a concrete propagation path from the change.

Do not treat "tests pass" as automatic proof that the work is done. Check the result against the user's request, review feedback, or stated acceptance context as well.

For explicit ready/final/finalize/send/ship-style checks on a development artifact such as a release note, migration guide, API document, PR description, or distributable output, use a light delivery gate:

1. State the acceptance context you are checking against.
2. Verify each criterion concretely against the artifact or current evidence.
3. Report `PASS` only when all checked criteria are satisfied.
4. Report `BLOCK` when a required criterion is missing, unsupported, or unverified.

Do not turn ordinary status checks into a delivery gate, and do not invent a heavier workflow when the user only asked whether ordinary work is done.
