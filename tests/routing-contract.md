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
| Tests, TDD, mocks, flaky tests caused primarily by test design or timing strategy, regression coverage | `test-strategy` |
| Explicit review, feedback, done/fixed/passing check, or development-artifact ready/finalize/send gate | `review-and-finish` |
| Explicit commit, push, merge, PR, discard, or branch wrap-up action | `finish-branch` |
| Explicit planning, roadmap, task breakdown, approach comparison, implementation slices | `plan-work` |
| Explicit architecture, seams, interfaces, adapters, domain language, prototypes | `design-codebase` |
| Explicit reassessment of reliability, evidence, stage drift, or stale context | `reliability-check` |
| Decompose-first orchestration, scout/divergent exploration, per-item batch pipeline, fresh-context verifier workflow, high-stakes judged delivery, or explicit delegated-agent work | `agent-workflow` |
| Explicit PRD, issue draft, tracker-ready work-item, or triage workflow from clear natural-language intent | `issue-workflow` |
| Explicit handoff, compression, or resume-state workflow | `memory-handoff` |
| Explicit checkpoint update or resume-from-checkpoint workflow | `memory-handoff` |
| Explicit durable lesson, correction, or confirmed-approach memory workflow | `markdown-memory` |
| Explicit prompt or skill maintenance, migration, or stale-scaffolding cleanup workflow | `skill-refactorer` |
| Explicit durable multi-session decision frontier | `decision-map` |

## Expected Composition

For maintenance validation, when more than one skill clearly applies, tests expect the smallest composition listed below:

| Case | Expected order |
| --- | --- |
| Unclear bug plus regression coverage | `debug-systematically` then `test-strategy` |
| Architecture question plus implementation plan | `design-codebase` then `plan-work` |
| Review plus branch finish | `review-and-finish` then `finish-branch` |
| Challenged claims plus handoff state | `reliability-check` then `memory-handoff` |
| Paused task state plus explicit durable lesson capture | `memory-handoff` plus `markdown-memory` |
| Planned slices plus delegated workflow | settled plan or base default behavior context, then `agent-workflow` |
| Settled design plus implementation | settled design or base default behavior context |

## Maintenance Use

When evaluating suite-level routing questions such as:

- which workflow should handle this
- whether trigger boundaries still make sense
- whether one skill is overlapping or mis-scoped
- how multiple skills should compose

validate answers against this routing contract, the maintained prompt file, and the individual skill files.
Those answers should stay grounded in the maintained boundaries above.
