---
name: debug-systematically
description: Use when a bug, failing test, regression, flaky behavior, slow path, or repeated failed fix needs diagnosis before changing code, especially when the cause is unclear or reproduction is unreliable.
---

# Debug Systematically

Diagnose unclear failures by making the bug observable, then testing causes one at a time. Use this when guessing is likely to waste more time than building a feedback loop.

## First Decision

Do not use the full workflow for obvious compile errors, typos, missing imports, or direct one-line failures. Make the narrow fix and run a focused check.

Use this workflow when the bug is unclear, flaky, cross-component, performance-related, a regression, or has survived previous fixes.

## Core Loop

1. **Build a feedback signal.** Prefer a failing test, focused CLI command, HTTP request, browser script, fixture replay, or small harness. The signal catches the user's symptom, not merely "runs."
2. **Run it red.** Confirm the signal reproduces the reported failure. For flaky bugs, raise the reproduction rate until it is debuggable.
3. **Minimize.** Remove inputs, steps, config, and callers one at a time until the remaining repro is load-bearing.
4. **Check recent change and working examples.** Look at the nearest relevant diff, config change, or dependency change, and compare against a similar working path in the same codebase when one exists.
5. **Hypothesize.** Write 2-4 ranked causes. Each predicts what evidence would confirm or disprove it.
6. **Probe one variable.** Use a debugger, focused logs, data-flow trace, profiler, or diff. Tag temporary logs with a unique prefix.
7. **Take the narrow win when it is justified.** If one hypothesis has enough evidence to support a narrow, reversible fix, implement and test it instead of exhausting every remaining hypothesis first.
8. **Fix the root cause.** Avoid bundled refactors and symptom patches.
9. **Verify and clean up.** Re-run the original signal, add or keep a regression check when there is a correct seam, and remove debug instrumentation.

For performance regressions, measure a baseline before changing code, then verify the same measurement after the fix.

If no correct regression seam exists, say that clearly instead of adding a false-confidence test.

If two or three grounded fix attempts fail, stop stacking guesses. Reassess whether the bug is really exposing a design, state-sharing, or boundary problem.

## If No Signal Exists

State what you tried and ask for the missing artifact: repro steps, logs, HAR/network capture, failing input, screen recording with timestamps, access to the reproducing environment, or permission for temporary instrumentation.

Do not present a confident fix without evidence.

## Debug Techniques

- Bad value appears deep in a stack: read [root-cause-tracing.md](references/root-cause-tracing.md).
- Flaky async behavior or timeout-based tests: read [condition-based-waiting.md](references/condition-based-waiting.md).
- Invalid data could enter through multiple paths: read [defense-in-depth.md](references/defense-in-depth.md).
