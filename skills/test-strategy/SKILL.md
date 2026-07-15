---
name: test-strategy
description: Use when the primary problem is test design, test seams, regression coverage, mocks, assertions, fixtures, or timing and wait strategy, or when a requested change needs a non-obvious test level, seam, regression signal, or acceptance proof.
---

# Test Strategy

Choose tests that prove the claimed behavior without turning every task into strict TDD.

## First Decision

- If the user asks for strict TDD, use TDD mode.
- If the product behavior or root cause is still unclear and a failing or flaky test is only the symptom, use `debug-systematically` first.
- If adding regression coverage for a bug, choose the narrowest seam that reproduces the real failure pattern.
- If the needed test level, seam, regression signal, fixture/mocking boundary, or acceptance proof is non-obvious, use this skill to settle it.
- If improving or adding tests, prefer observable behavior through public interfaces without forcing unnecessary implementation coupling.
- If the task is ordinary implementation and tests are not central, do not force a test-first workflow.

## Testing Defaults

- Test what the system does, not how internal collaborators are called.
- Choose the test level with the best evidence-to-cost ratio for the stated behavior and concrete risk.
- Prefer the most direct proof available; widen only when a narrower check cannot cover the behavior, contract, acceptance criteria, or risk being claimed.
- Use unit, property, type, benchmark, stress, integration, or end-to-end checks according to the evidence each claim requires.
- Keep each test focused on one behavior or one regression.
- Use existing project test tools, fixtures, naming, and setup patterns.
- Run the fastest high-signal test command that covers the changed behavior first; widen only when affected surface, risk, acceptance criteria, or an evidence gap requires broader proof.
- Prefer vertical slices: one behavior, one proving test or small group, then implementation; do not write all tests first and all code later.

Read [good-tests.md](references/good-tests.md) when the test shape itself is the main question.

## TDD Mode

When the user asks for TDD, red-green-refactor, or test-first work:

1. Pick one behavior.
2. Write one failing test.
3. Run it and confirm it fails for the expected reason.
4. Write only enough implementation to pass.
5. Run the focused test green.
6. Refactor after green, keeping tests green.

Read [tdd-mode.md](references/tdd-mode.md) for stricter details.

## Mocks

Mock system boundaries such as external APIs, time, randomness, slow services, or filesystem access when using the real thing is costly or unreliable.

Do not mock internal collaborators by default. Do not assert that a mock component or mock function exists unless that is the behavior the user cares about.

Read [mocking.md](references/mocking.md) when mocks, test doubles, or mock-heavy failures are involved.

## Flaky Tests

For timing, async, or intermittent failures, wait for the condition that proves progress instead of sleeping for a guessed duration. Read [flaky-tests.md](references/flaky-tests.md).
