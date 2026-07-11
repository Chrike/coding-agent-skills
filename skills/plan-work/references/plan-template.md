# Plan Template

Use this for durable plans, handoffs, or work that spans sessions. Keep it specific enough to execute, but avoid pasting large code blocks unless the exact code is the decision.

```markdown
# <Feature Or Refactor> Plan

## Goal

<One sentence describing the intended outcome.>

## Context

- Current behavior:
- Desired behavior:
- Relevant constraints:
- Out of scope:

## Approach

<Chosen approach and why it fits the codebase. Mention rejected alternatives only when the trade-off matters.>

## Files And Ownership

| Path | Action | Responsibility |
| --- | --- | --- |
| `path/to/file` | Modify/Create | What this file owns after the change. |

## Steps

1. <Step that produces a meaningful, reviewable change.>
   - Likely files:
   - Verification:
   - Depends on:

2. <Next step.>
   - Likely files:
   - Verification:
   - Depends on:

## Risks

- <Risk or unknown, with how to reduce it.>

## Verification

- Fastest high-signal check that directly covers the changed behavior:
- Broader check when affected surface, risk, acceptance criteria, or remaining evidence gaps require it:
```

## Self-Check

Before presenting the plan:

- Remove placeholders such as `TBD`, `TODO`, "handle edge cases", or "write tests" without detail.
- Confirm every step has a visible outcome and a verification idea.
- Confirm file paths and commands are based on inspected project context, not guesses.
- Keep commits, branches, PRs, and issue publication out unless requested.
