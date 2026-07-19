# Routing Contract

Use this file as the concise maintenance-layer routing map. It is not a runtime skill. Detailed cases are split by owner:

- [Positive routing cases](routing/positive.md)
- [Negative routing cases](routing/negative.md)
- [Composition and orchestration cases](routing/composition.md)
- [Agent role contracts](agents/roles.md)
- [Adaptive Workflow contracts](workflows/adaptive-long-horizon.md)
- [Fresh findings review Workflow contract](workflows/fresh-findings-review.md)
- [Skill ownership checks](skills/role-ownership.md)
- [Memory handoff checks](skills/memory-handoff.md)

## Source of truth

- `prompts/CLAUDE.fragment.md` defines the always-on default behavior layer.
- Each runtime skill's `description` and `SKILL.md` body define that skill's trigger boundary and method.
- Saved Agent files define stable leaf roles only.
- Workflow files define dynamic state, schemas, validators, and orchestration.
- `tests/` validates these boundaries and must not become a second runtime instruction layer.

## Core routing

| User need | Layer |
| --- | --- |
| Ordinary coding, code questions, straightforward fixes | Base default behavior |
| Unclear bug, flaky behavior, regression, slow path, repeated failed fix | `debug-systematically` |
| Test design, TDD, mocks, flaky tests, regression coverage, or a non-obvious test seam/acceptance signal | `test-strategy` |
| Explicit review, feedback, done/fixed/passing check, or focused readiness evidence | `review-and-finish` |
| Explicit bundled `/code-review` | host review workflow |
| Explicit commit, push, merge, PR, discard, or branch wrap-up | `finish-branch` |
| Explicit planning, roadmap, task breakdown, or unresolved sequencing/scope decision | `plan-work` |
| Explicit architecture, seam, interface, adapter, prototype, or ownership boundary | `design-codebase` |
| Explicit reassessment of reliability, evidence, stage drift, or stale context | `reliability-check` |
| Two or more independent slices or coordinated verification questions | `agent-workflow` |
| Explicit PRD, issue draft, tracker-ready work item, or triage | `issue-workflow` |
| Explicit handoff, compression, checkpoint, or resume state | `memory-handoff` |
| Explicit project lesson or confirmed-approach capture | `markdown-memory` |
| Explicit prompt or skill maintenance | `skill-refactorer` |
| Explicit durable multi-session decision frontier | `decision-map` |

## Ownership rule

Route from the smallest explicit intent. Keep `review-and-finish` separate from `finish-branch`, keep the active Workflow as the sole outer orchestration owner, and do not create an Agent or Workflow layer merely because a task is long or multi-file.
