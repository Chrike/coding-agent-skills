# Expected Routing

Use this file as a compact contract for representative routing decisions across the current suite.

## Ordinary Work Stays In The Default Layer

| Prompt Shape | Expected Routing | Why |
| --- | --- | --- |
| Fix this small TypeScript error. | Base default behavior | ordinary coding should stay lightweight |
| Explain how this service works. | Base default behavior | explanation is not a workflow by itself |
| Implement the approved steps from this existing plan file. | Base default behavior | settled plans should guide execution directly |
| Implement the selected design above. | Base default behavior | settled design choices should guide execution directly |
| Continue this paused task using the current issue or work-item draft. | Base default behavior | existing tracked state should guide execution |
| You already have enough context. Stop planning and implement the next step. | Base default behavior | sufficient context should lead to execution |
| Reuse the evidence from this session if it still covers the current code and decision. | Base default behavior | stage changes alone should not force repeated investigation or verification |
| Use one focused Explore for this single search question. | Base default behavior | one focused delegation is ordinary execution, not multi-agent orchestration |

## Automatic Workflow Examples

| Prompt Shape | Expected Routing | Why |
| --- | --- | --- |
| This test is flaky; diagnose it. | `debug-systematically` | use debugging when the underlying product behavior is still unclear |
| Claude Code itself is misbehaving; inspect the session logs. | bundled `/debug` | host runtime issues should use the host debug command rather than the project debugging skill |
| This test depends on sleep and flakes in CI. Fix the wait strategy. | `test-strategy` | use test-strategy when the primary problem is test timing and wait design |
| Add regression tests for this bug. | `test-strategy` | explicit testing workflow |
| Review these changes. | `review-and-finish` | explicit natural-language review request |
| Address this PR feedback. | `review-and-finish` | explicit review feedback handling |
| Can I call this done? | `review-and-finish` | explicit completion verification |
| This completed cross-service permission migration needs a focused readiness check before the done claim. | `review-and-finish` | a behaviorally high-risk completed change needs focused readiness evidence |
| Plan this refactor. | `plan-work` | explicit planning request |
| Implement this migration; the compatibility and rollout sequence are unresolved. | `plan-work`, then implementation | resolve only the load-bearing plan before coding |
| Where should this interface live? | `design-codebase` | explicit design question |
| Implement this feature; existing patterns do not settle its ownership boundary. | `design-codebase`, then implementation | resolve the non-obvious design decision before coding |
| Use existing local tooling to test one interface hypothesis entirely in memory; install nothing, call no service, leave no files, and clean up in this pass. | `design-codebase` | a safe local throwaway prototype may run without another approval |
| You are hallucinating; reread the files and reassess. | `reliability-check` | explicit corrective reassessment |
| Investigate these independent subsystems in parallel. | `agent-workflow` | multi-agent method for genuinely independent slices |
| Run the same inspect-patch-verify pipeline across this batch of items. | `agent-workflow` | repeated per-item pipeline needs orchestration method |
| Add an independent verifier before we continue. | `agent-workflow` | explicit independent verification coordination |
| Diagnose these independent failure paths in parallel. | `debug-systematically` + `agent-workflow` | domain method plus multi-agent orchestration |
| Use TDD to implement these independent adapters. | `test-strategy` + `agent-workflow` | domain method plus multi-agent orchestration |
| Review each changed package independently and merge the findings. | `review-and-finish` + `agent-workflow` | domain method plus multi-agent orchestration |
| Compare these independent architecture options. | `design-codebase` + `agent-workflow` | domain method plus multi-agent orchestration |

## Explicit-Intent And Routing-Meta Examples

These prompts hit the skills below only when the user clearly asks for that workflow or asks a routing-meta question.

| Prompt Shape | Expected Routing | Why |
| --- | --- | --- |
| Commit these changes. | `finish-branch` | explicit branch action |
| Push this branch after the checks. | `finish-branch` | explicit branch action |
| Turn this into a PRD. | `issue-workflow` | explicit durable work-item request |
| Break this PRD into issues. | `issue-workflow` | explicit tracker-style decomposition |
| Make a decision map for this vague direction. | `decision-map` | explicit durable decision-tracking request |
| Add a prototype ticket to this decision map. | `decision-map`, with user agreement before building the prototype | durable decision-map prototype tickets remain approval-gated |
| Update the handoff with the latest checkpoint before we compress. | `memory-handoff` | explicit handoff / compression request |
| Resume from the latest checkpoint in the current handoff note. | `memory-handoff` | explicit checkpoint-based resume request |
| Record this repeated mistake as a project-reviewed lesson. | `markdown-memory` | explicit project-governed lesson request |
| Rewrite this old SKILL.md for the current suite. | `skill-refactorer` | explicit prompt/skill maintenance request |
| Which workflow should handle this? | routing contract plus prompt and skill descriptions | explicit routing question |
| `/code-review` | bundled review command | explicit bundled review commands should stay with the host review engine |

## Review Split Check

| Prompt Shape | Expected Routing | Why |
| --- | --- | --- |
| Review these changes. | `review-and-finish` | explicit natural-language review request |
| Address this PR feedback. | `review-and-finish` | explicit review feedback handling |
| Can I call this done? | `review-and-finish` | explicit completion verification |
| Finish this branch. | `finish-branch` | explicit branch-ending action |
| Review these changes, then help me finish the branch. | `review-and-finish` then `finish-branch` | review and branch wrap-up remain separate and ordered |
| `/code-review` | bundled review command | explicit bundled review remains host-owned |

## Orchestration Method Check

| Prompt Shape | Expected Routing | Why |
| --- | --- | --- |
| Investigate these independent subsystems in parallel. | `agent-workflow` method plus host-selected execution substrate | project method owns decomposition and integration; host owns launch substrate |
| Use one focused Explore for this single search question. | Base default behavior | one focused delegation must not activate orchestration |
| A host multi-agent workflow is being prepared for these independent subsystems. | `agent-workflow` method supplies that workflow; no second layer | method informs the host workflow while it is still being prepared |
| A host multi-agent workflow for this scope is already running. | continue the active workflow; do not invoke a new orchestration workflow | do not wrap an already-running host workflow |
| Host multi-agent capability is available; fix this one coherent bug. | `debug-systematically` or base flow; `agent-workflow` must not trigger | capability alone is not an orchestration trigger |
