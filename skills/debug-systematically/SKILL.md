---
name: debug-systematically
description: Use when the product behavior or root cause is unclear, including when a failing or flaky test is only the symptom. Diagnose the underlying behavior before choosing a fix.
---

# Debug Systematically

Diagnose unclear failures by making the bug observable, then testing causes one at a time. Use this when guessing is likely to waste more time than building a feedback loop.

## First Decision

Do not use the full workflow for obvious compile errors, typos, missing imports, or direct one-line failures. Make the narrow fix and run a focused check.

If the primary problem is test design, test seams, fixtures, mocks, assertions, or wait strategy rather than unclear product behavior, use `test-strategy` instead.

If the problem concerns Claude Code installation, session behavior, tool execution, or runtime logs rather than project code, use bundled `/debug` instead.

Use this workflow when the bug is unclear, flaky, cross-component, performance-related, a regression, or has survived previous fixes.

## Core Loop

1. **Build a feedback signal.** Prefer a failing test, focused CLI command, HTTP request, browser script, fixture replay, or small harness. The signal catches the user's symptom, not merely "runs."
2. **Run it red.** Confirm the signal reproduces the reported failure. For flaky bugs, raise the reproduction rate until it is debuggable.
3. **Minimize.** Remove inputs, steps, config, and callers one at a time until the remaining repro is load-bearing.
4. **Check recent change and working examples.** Look at the nearest relevant diff, config change, dependency change, or a similar working path in the same codebase when that comparison can discriminate between plausible causes.
5. **Hypothesize.** Form the smallest useful set of grounded hypotheses. Use multiple ranked causes only when more than one cause remains genuinely plausible.
6. **Probe one variable.** Use a debugger, focused logs, data-flow trace, profiler, or diff. Tag temporary logs with a unique prefix.
7. **Take the narrow win when it is justified.** If one hypothesis has enough evidence to support a narrow, reversible fix, implement and test it instead of exhausting every remaining hypothesis first.
8. **Fix the root cause.** Avoid bundled refactors and symptom patches.
9. **Verify and clean up.** Re-run the original signal, add or keep a regression check when there is a correct seam, and remove debug instrumentation.

For performance regressions, measure a baseline before changing code, then verify the same measurement after the fix.

If no correct regression seam exists, say that clearly instead of adding a false-confidence test.

If a few grounded fix attempts fail, stop stacking guesses. Reassess whether the bug is really exposing a design, state-sharing, or boundary problem.

## If No Signal Exists

State what you tried and ask for the missing artifact: repro steps, logs, HAR/network capture, failing input, screen recording with timestamps, access to the reproducing environment, or permission for temporary instrumentation.

Do not present a confident fix without evidence.

## Debug Techniques

- Bad value appears deep in a stack: read [root-cause-tracing.md](references/root-cause-tracing.md).
- Flaky async behavior or timeout-based tests: if the flakiness is primarily caused by test timing or wait strategy rather than unclear product behavior, use `test-strategy` and read [flaky-tests.md](../test-strategy/references/flaky-tests.md).
- Invalid data could enter through multiple paths: read [defense-in-depth.md](references/defense-in-depth.md).
