# Root Cause Tracing

Use when a failure appears deep in a call stack, but the real bad input or decision likely happened earlier.

## Pattern

1. Observe the exact symptom: error, wrong value, slow step, missing state.
2. Find the immediate failing operation.
3. Ask what called it and what value/config it received.
4. Trace callers upward until the original invalid value or wrong decision appears.
5. Fix at the source. Add a nearby guard only when it prevents recurrence without hiding the source.

## Probes

- Log the value, caller context, and stack before the dangerous operation.
- In tests, prefer direct console output if the logger is suppressed.
- Trace data shape changes at component boundaries.
- Compare a working path and broken path with the same input.

## Stop Conditions

- Stop tracing when you find the earliest place the bad value is created or accepted.
- If tracing reaches external input, validate at the boundary and document the expected contract.
