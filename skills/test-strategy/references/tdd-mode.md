# TDD Mode

Use when the user explicitly asks for TDD, test-first, or red-green-refactor.

## Cycle

1. Choose one observable behavior.
2. Write the smallest test that should fail.
3. Run it and confirm the failure is expected, not a typo or setup error.
4. Implement only enough code to pass that test.
5. Run the focused test green.
6. Refactor only after green.
7. Repeat for the next behavior.

## Guardrails

- Do not write all tests first and then all implementation. Use vertical slices.
- Do not add speculative features for later tests.
- Do not refactor while red.
- If a test passes immediately, it did not prove the missing behavior.
- If the test is hard to write, treat that as design feedback.

## Existing Code

When code already exists, do not delete, revert, disable, or broadly rewrite existing work merely to force a red test. A request for strict TDD does not authorize deletion or rollback.

Prefer adding a meaningful regression or characterization test, or identify a genuinely missing behavior that can produce an expected red result. Any deletion or rollback requires separate authorization bound to the exact files and operation.
