# Routing Contract

Use this file as the maintenance-layer routing contract for the development skill suite.

It is not a runtime skill.
The maintained prompt file is authoritative for always-on default behavior.
Each runtime skill's `description` and `SKILL.md` body are authoritative for that skill's own trigger boundary.
This file is a maintenance contract for checking how those boundaries fit together.

## Source Of Truth

- `prompts/CLAUDE.fragment.md` defines the always-on default behavior layer.
- Each runtime skill's `description` plus `SKILL.md` body defines when that skill should trigger.
- `tests/` validates those boundaries and must not become a second runtime instruction layer.

## Core Routing

| User Need | Layer |
| --- | --- |
| Ordinary coding, code questions, straightforward fixes | Base default behavior |
| Unclear bug, flaky behavior, regression, slow path, repeated failed fix | `debug-systematically` |
| Test design, TDD, mocks, flaky tests caused primarily by test design or timing strategy, regression coverage, or a non-obvious test seam/level/acceptance signal | `test-strategy` |
| Explicit review, feedback, done/fixed/passing check, development-artifact ready/finalize/send gate, or a behaviorally high-risk completed change needing focused readiness evidence before a done claim | `review-and-finish` |
| Explicit bundled `/code-review` | host review workflow |
| Explicit commit, push, merge, PR, discard, or branch wrap-up action | `finish-branch` |
| Explicit planning, roadmap, task breakdown, approach comparison, implementation slices, or a requested implementation with approach/dependency/sequencing/migration/compatibility/scope decisions that cannot be safely inferred | `plan-work` |
| Explicit architecture, seams, interfaces, adapters, domain language, prototypes, or an implementation blocked on a non-obvious architecture/ownership/interface/dependency-boundary decision | `design-codebase` |
| Explicit reassessment of reliability, evidence, stage drift, or stale context | `reliability-check` |
| An explicit request to parallelize, coordinate multiple agents, run parallel scouts, or assign multiple independent verifiers; or two or more independently decomposable work slices, repeated per-item pipeline, scout slices, multiple coordinated verification questions, or genuinely independent high-stakes candidate/review panels requiring integration | `agent-workflow` fit check; actual fan-out only when the fit check passes and the bounded work still benefits from it |
| Explicit PRD, issue draft, tracker-ready work-item, tracker publication/update, or triage workflow from clear natural-language intent | `issue-workflow` |
| Explicit handoff, compression, checkpoint update, or resume-state workflow | `memory-handoff` |
| Explicit project-versioned, shared, or reviewable lesson, correction, or confirmed-approach workflow | `markdown-memory` |
| Explicit prompt or skill maintenance, migration, or stale-scaffolding cleanup workflow | `skill-refactorer` |
| Explicit durable multi-session decision frontier | `decision-map` |

## Expected Composition

For maintenance validation, when more than one skill clearly applies, tests expect the smallest composition listed below:

| Case | Expected order |
| --- | --- |
| Unclear bug plus regression coverage | `debug-systematically` then `test-strategy` |
| Implementation with both an unresolved architecture boundary and migration, compatibility, sequencing, or scope decisions | `design-codebase` then `plan-work`, then implementation (resolve the design boundary before planning dependent rollout work) |
| Explicitly requested review plus explicit branch finish | `review-and-finish` then `finish-branch` |
| Multi-agent orchestration plus domain method | `agent-workflow` fit-check method with the active domain skill; a passing fit check permits but does not guarantee fan-out |
| Independent failure-path diagnosis | `debug-systematically` method with `agent-workflow` |
| Independent TDD adapters | `test-strategy` method with `agent-workflow` |
| One focused verifier for one evidence question | direct delegation under the active domain method; not `agent-workflow` |
| Multiple orthogonal verifier scopes requiring coordinated integration | active domain method with `agent-workflow` |
| Independent package review | `review-and-finish` method with `agent-workflow` |
| Independent architecture options | `design-codebase` method with `agent-workflow` |
| Host multi-agent workflow being prepared for independent slices | `agent-workflow` method into that workflow; no second layer |
| Host multi-agent workflow already running for the same scope | continue the active workflow; do not invoke a new orchestration workflow |
| Explicit installed `/adaptive-long-horizon` command for a bounded read-only evidence task | the saved workflow is the sole outer execution owner for its session-local run; supply `agent-workflow` method contracts into its leaf prompts without starting a sibling controller (`needs-review`: leaf propagation is workflow-internal) |
| Host multi-agent capability available for one coherent bug | domain skill or base default behavior; not `agent-workflow` |
| Challenged claims plus handoff state | `reliability-check` then `memory-handoff` |
| Paused task state plus explicit durable lesson capture | `memory-handoff` plus `markdown-memory` |
| Settled design plus implementation | settled design or base default behavior context |

## Maintenance Use

When evaluating suite-level routing questions such as:

- which workflow should handle this
- whether trigger boundaries still make sense
- whether one skill is overlapping or mis-scoped
- how multiple skills should compose

validate answers against this routing contract, the maintained prompt file, and the individual skill files.
Those answers should stay grounded in the maintained boundaries above.
