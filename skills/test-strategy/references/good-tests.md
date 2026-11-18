# Good Tests

Use tests that describe observable behavior and survive internal refactors.

## Prefer

- Public API, endpoint, UI behavior, CLI command, service boundary, or domain interface.
- Test names that describe the behavior: "rejects expired token" rather than "calls validateToken".
- Assertions on returned values, visible state, emitted events, persisted behavior through an interface, or error messages.

## Avoid

- Private method tests.
- Tests that pass when behavior is broken.
- Tests that break when only implementation changes.
- Production methods that exist only for tests.

## Regression Coverage

For a bug fix, first identify the real failure pattern. A good regression test fails before the fix and exercises the same path the bug used. If no correct seam exists, note the testability gap rather than adding a false-confidence unit test.
