# Fresh-Context Verification

Use this after `agent-workflow` is already active when milestone risk or blind-spot cost justifies a separate delegated verifier.

## When to use

Use a fresh-context verifier when:

- a milestone is important enough that you do not want to compound more work on top of unchecked assumptions
- a small batch of dependent slices has landed and the controller wants an independent mismatch check
- the implementer may be carrying assumptions that a verifier should not inherit

## Verifier input

Give the verifier:

- the specification
- changed output or artifact
- verification scope
- expected report format

Do not give the verifier the controller's original reasoning unless the task truly requires it.

## Verifier role

- the verifier checks for mismatches against the spec
- the verifier does not re-implement the task
- the verifier reports blocker, mismatch, or no issue found
- the verifier does not claim absolute correctness

## Controller rules

- reuse implementation evidence when it identifies the final code state, command or observation, and result
- do not rerun the implementer's checks merely to reproduce the same evidence
- run an independent check only when environment independence, stale evidence, a missing acceptance criterion, or a load-bearing assumption requires it
- if a verifier finds a blocker that invalidates later work, fix or re-scope before further fan-out
- do not turn every tiny delegated step into implementer plus verifier by default
