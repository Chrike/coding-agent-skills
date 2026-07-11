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
| Plan this refactor. | `plan-work` | explicit planning request |
| Where should this interface live? | `design-codebase` | explicit design question |
| You are hallucinating; reread the files and reassess. | `reliability-check` | explicit corrective reassessment |
| Investigate these independent subsystems in parallel. | `agent-workflow` | multi-agent method for genuinely independent slices |
| Run the same inspect-patch-verify pipeline across this batch of items. | `agent-workflow` | repeated per-item pipeline needs orchestration method |
| Add an independent verifier before we continue. | `agent-workflow` | explicit independent verification coordination |

## Explicit-Intent And Routing-Meta Examples

These prompts hit the skills below only when the user clearly asks for that workflow or asks a routing-meta question.

| Prompt Shape | Expected Routing | Why |
| --- | --- | --- |
| Commit these changes. | `finish-branch` | explicit branch action |
| Push this branch after the checks. | `finish-branch` | explicit branch action |
| Turn this into a PRD. | `issue-workflow` | explicit durable work-item request |
| Break this PRD into issues. | `issue-workflow` | explicit tracker-style decomposition |
| Make a decision map for this vague direction. | `decision-map` | explicit durable decision-tracking request |
| Update the handoff with the latest checkpoint before we compress. | `memory-handoff` | explicit handoff / compression request |
| Resume from the latest checkpoint in the current handoff note. | `memory-handoff` | explicit checkpoint-based resume request |
| Record this repeated mistake as a durable lesson. | `markdown-memory` | explicit durable lesson request |
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
| Ultracode already selected a multi-agent workflow for this scope. | `agent-workflow` method without a second orchestration layer | do not wrap an already-selected dynamic workflow |
