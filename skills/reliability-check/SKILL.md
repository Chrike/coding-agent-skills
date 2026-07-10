---
name: reliability-check
description: Use when the user explicitly asks the agent to reassess evidence, source use, the active stage, stale context, unsupported confidence, hallucination, guessing, source-vs-memory confusion, example-vs-task confusion, or whether it read the right files.
---

# Reliability Check

Reassess the current state when the user explicitly challenges reliability. Use this to correct unsupported conclusions without turning ordinary work into a default ceremony.

## First Decision

- Use this only when the user explicitly challenges reliability, evidence, source use, active stage, stale context, hallucination, guessing, or explicitly asks to reassess one of those reliability concerns.
- Do not use this merely because a request involves saved state, examples, reviews, plans, or uncertainty.
- Do not use this for ordinary coding, debugging, test writing, planning, architecture, review, issue drafting, delegation, or handoff unless the user flags reliability trouble.
- Stop new edits and unrelated tool actions while reassessing; reading the named evidence is allowed.

## Reliability Loop

1. Restate the latest reliability concern or user correction in one sentence.
2. Identify the current user-requested stage or mode.
3. Separate:
   - current source-backed facts
   - user-stated corrections
   - external or reference material
   - assistant assumptions
   - unverified claims
4. Reread the named files or artifacts that the correction depends on.
5. State the correction:
   - wrong source
   - wrong stage
   - wrong artifact
   - wrong target object
   - wrong scope update
   - wrong strategy interpretation
   - wrong workflow
   - unsupported conclusion
   - stale state
6. Continue from the corrected current state. If the current request still requires execution and no user-only blocker remains, resume the work immediately; otherwise state the next concrete action or blocker.

## Exit Rule

- Perform one reassessment pass for the named reliability concern.
- After stating the correction, exit this workflow and immediately resume the current requested stage when execution is still required.
- Do not activate this workflow again for the same concern unless the user provides new evidence or explicitly requests another reassessment.
- A complaint that execution is slow is not by itself a request to reread the same evidence.

## Boundaries

This skill does not replace:

- the ordinary implementation flow for straightforward work.
- `debug-systematically` for code bugs and root-cause diagnosis.
- `test-strategy` for testing choices and regression proof.
- `review-and-finish` for explicit code review, feedback handling, or completion verification.
- `finish-branch` for explicit branch-ending actions.
- `plan-work` for requested implementation planning.
- `memory-handoff` for routine compression and resume.

Do not turn this into a universal "think harder" step, a long checklist, or a default preflight for normal tasks.
