# Fresh-Context Verification

Use this only after `agent-workflow` is already active, when milestone risk or blind-spot cost justifies a separate verifier within an existing multi-slice workflow. One focused verifier for one defined evidence question is ordinary direct delegation, not a reason to activate orchestration.

## When to use

Use a fresh-context verifier when:

- a milestone is important enough that you do not want to compound more work on top of unchecked assumptions
- a small batch of dependent slices has landed and the controller wants an independent mismatch check
- the implementer may be carrying assumptions that a verifier should not inherit

## Verifier input

Give the verifier:

- the specification
- changed output or artifact
- the relevant final code, commit, or worktree state
- existing verification evidence when the verifier is judging completeness
- verification scope
- expected report format

Omit existing evidence only when blind or environment-independent execution is the specific verification goal.

Do not give the verifier the controller's original reasoning unless the task truly requires it.

## Verifier role

- the verifier checks for mismatches against the spec
- the verifier does not re-implement the task
- the verifier reports blocker, mismatch, or no issue found
- the verifier does not claim absolute correctness

## De-anchored review packet

When the controller chooses a fresh-context mismatch check, pass only the smallest reviewable `ARTIFACT` and its `CONTRACT`:

- `ARTIFACT`: the relevant diff, decision, proposal, or assertion being checked.
- `CONTRACT`: the observable behavior, constraints, acceptance boundary, or scope the artifact must satisfy.

Omit the controller's claim, reasoning, and journey unless the evidence question genuinely requires them. Ask the verifier to look for contract violations, unstated assumptions, hidden coupling, edge cases, and broken project conventions rather than to approve the artifact. This packet is a method for a bounded verifier, not a requirement to start fresh review for every non-trivial change.

## Reconcile findings

The controller owns the conclusion. Re-read the artifact and contract before classifying each finding:

1. **Contract misread** — the contract was unclear or incomplete; clarify it before deciding whether the finding survives.
2. **Valid and actionable** — the artifact violates the contract and needs a change.
3. **Valid trade-off** — the concern is real, but accepting it is cheaper or safer; record the trade-off and its boundary.
4. **Noise** — the concern does not apply under the supplied contract or project evidence; record why rather than silently ignoring it.

If fresh-context independence is unavailable, do not describe a sequential reread as fresh verification; preserve the independence gap as `UNVERIFIED` or `BLOCKED` when it affects the acceptance claim.

## Controller rules

- reuse implementation evidence when it identifies the final code state, command or observation, and result
- do not rerun the implementer's checks merely to reproduce the same evidence
- run an independent check only when environment independence, stale evidence, a missing acceptance criterion, or a load-bearing assumption requires it
- if a verifier finds a blocker that invalidates later work, fix or re-scope before further fan-out
- do not turn every tiny delegated step into implementer plus verifier by default
