# Routing Composition Cases

Use this file for multi-skill composition and orchestration ownership. It is maintenance material, not a runtime skill.

## Expected composition

| Case | Expected order or owner |
| --- | --- |
| Unclear bug plus regression coverage | `debug-systematically` then `test-strategy` |
| Implementation with an unresolved architecture boundary and rollout decisions | `design-codebase` then `plan-work`, then implementation |
| Explicit review plus explicit branch finish | `review-and-finish` then `finish-branch` |
| Multi-agent orchestration plus a domain method | `agent-workflow` with the active domain skill |
| Independent failure-path diagnosis | `debug-systematically` with `agent-workflow` |
| Independent TDD adapters | `test-strategy` with `agent-workflow` |
| One focused verifier for one evidence question | direct delegation under the active domain method; not `agent-workflow` |
| Multiple orthogonal verifier scopes requiring integration | active domain method with `agent-workflow` |
| Independent package review | `review-and-finish` with `agent-workflow` |
| Independent architecture options | `design-codebase` with `agent-workflow` |
| A host workflow is being prepared for independent slices | `agent-workflow` method into that workflow; no second layer |
| A host workflow already owns this scope | continue the active workflow; no new orchestration layer |
| A dynamic workflow authorizes one bounded nested controller | workflow remains sole outer owner; controller integrates bounded leaf results |
| A workflow leaf finds a shared or out-of-scope question without nested-controller authorization | return it to the active controller; do not create another tree |
| A later slice needs accepted evidence and ruled-out paths from an earlier slice | pass only the smallest material carry-forward state |
| A later slice needs exact rereading of long producer evidence | prefer producer-local or host state; use transient scratch only when necessary |
| Challenged claims plus handoff state | `reliability-check` then `memory-handoff` |
| Paused task plus explicit durable lesson capture | `memory-handoff` plus `markdown-memory` |
| Settled design plus implementation | settled design or base default behavior context |

## Independent-slice and workflow cases

| Prompt | Expected behavior |
| --- | --- |
| Investigate these independent subsystems in parallel. | `agent-workflow` with non-overlapping owners |
| Run the same inspect-patch-verify pipeline across this batch. | `agent-workflow` repeated pipeline |
| Assign authorization, compatibility, and rollback verification to separate owners. | `review-and-finish` plus `agent-workflow` |
| Diagnose these independent failure paths in parallel. | `debug-systematically` plus `agent-workflow` |
| Use TDD to implement these independent adapters. | `test-strategy` plus `agent-workflow` |
| Review each changed package independently and merge the findings. | `review-and-finish` plus `agent-workflow` |
| Compare these independent architecture options. | `design-codebase` plus `agent-workflow` |
| Parallelize this multi-file bug investigation, but all symptoms share one root cause. | fit-check first; keep one `debug-systematically` or default owner |
| Implement independent write slices, but safe worktree isolation is unavailable. | `agent-workflow` with serialized writes |
| A host multi-agent workflow is being prepared for independent subsystems. | use its method; do not create a sibling layer |
| A host multi-agent workflow for this scope is already running. | continue it; do not start another orchestration layer |
| Run installed `/adaptive-long-horizon` for an explicitly supplied read-only evidence task. | saved workflow is the sole outer owner |

## Safety composition

- `prompts/CLAUDE.fragment.md` remains the universal owner for scope, evidence, side-effect, branch-action, and active orchestration safety defaults.
- `agent-workflow` owns decomposition, assignment, handoff, integration, and stop conditions; it does not replace the active domain method.
- A saved Agent owns only a stable leaf role; the Workflow or Skill owns dynamic state, schema, validation, triage, completion, and delivery decisions.
- A selector is compatibility behavior, not a security boundary. Selector resolution fallback uses the built-in read-only `Explore` role; it does not retry worker or permission failures and does not use an unrestricted generic worker.
