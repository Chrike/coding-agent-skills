# Routing Contract

Use this file as the maintenance-layer routing contract for the development skill suite.

It is not a runtime skill.
The prompt fragments are authoritative for always-on default behavior.
Each runtime skill's `description` and `SKILL.md` body are authoritative for that skill's own trigger boundary.
This file explains how the suite fits together after removing the runtime router layer.

## Source Of Truth

- `prompts/AGENTS.fragment.md` and `prompts/CLAUDE.fragment.md` define the always-on default behavior layer.
- Each runtime skill's `description` plus `SKILL.md` body defines when that skill should trigger.
- `tests/` validates those boundaries and must not become a second runtime instruction layer.

## Core Routing

| User Need | Layer |
| --- | --- |
| Ordinary coding, code questions, straightforward fixes | Base default behavior |
| Unclear bug, flaky behavior, regression, slow path, repeated failed fix | `debug-systematically` |
| Tests, TDD, mocks, flaky tests, regression coverage | `test-strategy` |
| Explicit review, feedback, done/fixed/passing check, or external-facing ready/finalize/send gate | `review-and-finish` |
| Explicit commit, push, merge, PR, discard, or branch wrap-up action | `finish-branch` |
| Explicit planning, roadmap, task breakdown, approach comparison, implementation slices | `plan-work` |
| Explicit architecture, seams, interfaces, adapters, domain language, prototypes | `design-codebase` |
| Explicit reassessment of reliability, evidence, stage drift, or stale context | `reliability-check` |
| Explicit delegated-agent, parallel-slice, or fresh-context-verifier workflow | `agent-workflow` |
| Explicit PRD, issue breakdown, tracker-ready work-item, or triage workflow | `issue-workflow` |
| Explicit handoff, compression, or resume-state workflow | `memory-handoff` |
| Explicit durable lesson, correction, or confirmed-approach memory workflow | `markdown-memory` |
| Explicit prompt or skill maintenance, migration, or stale-scaffolding cleanup workflow | `skill-refactorer` |
| Explicit Claude or Fable effort selection, review, or recalibration workflow | `effort-calibrator` |
| Explicit durable multi-session decision frontier | `decision-map` |

## Composition Order

When more than one skill clearly applies, prefer the smallest composition that resolves uncertainty before action:

| Case | Order |
| --- | --- |
| Unclear bug plus regression coverage | `debug-systematically` then `test-strategy` |
| Architecture question plus implementation plan | `design-codebase` then `plan-work` |
| Review plus branch finish | `review-and-finish` then `finish-branch` |
| Challenged claims plus handoff state | `reliability-check` then `memory-handoff` |
| Paused task state plus explicit durable lesson capture | `memory-handoff` plus `markdown-memory` |
| Planned slices plus delegated workflow | task skill or `plan-work` then `agent-workflow` |

## Meta Review

When a user asks suite-level questions such as:

- which workflow should handle this
- whether trigger boundaries still make sense
- whether one skill is overlapping or mis-scoped
- how multiple skills should compose

answer from this routing contract, the prompt fragments, and the individual skill files.
Do not rely on a runtime router skill for those questions.
