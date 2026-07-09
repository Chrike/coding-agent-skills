# Expected Routing

Use this file as a compact contract for representative routing decisions across the current suite.

## Ordinary Work Stays In The Default Layer

| Prompt Shape | Expected Routing | Why |
| --- | --- | --- |
| Fix this small TypeScript error. | Base default behavior | ordinary coding should stay lightweight |
| Explain how this service works. | Base default behavior | explanation is not a workflow by itself |
| Implement the approved steps from this existing plan file. | Base default behavior | settled plans should guide execution directly |
| Continue this paused task using the current issue or work-item draft. | Base default behavior | existing tracked state should guide execution |
| You already have enough context. Stop planning and implement the next step. | Base default behavior | sufficient context should lead to execution |

## Automatic Workflow Examples

| Prompt Shape | Expected Routing | Why |
| --- | --- | --- |
| This test is flaky; diagnose it. | `debug-systematically` | explicit unclear-bug diagnosis |
| Add regression tests for this bug. | `test-strategy` | explicit testing workflow |
| Review these changes. | `review-and-finish` | explicit review request |
| Plan this refactor. | `plan-work` | explicit planning request |
| Where should this interface live? | `design-codebase` | explicit design question |
| You are hallucinating; reread the files and reassess. | `reliability-check` | explicit corrective reassessment |
| Break this into independent subproblems first, then parallelize only the real slices. | `agent-workflow` | explicit orchestration request |

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
| Review whether this coding workload should stay at the current effort level. | `effort-calibrator` | explicit effort-calibration request |
| Which workflow should handle this? | routing contract plus prompt and skill descriptions | explicit routing question |

## Review Split Check

| Prompt Shape | Expected Routing | Why |
| --- | --- | --- |
| Review these changes. | `review-and-finish` | explicit review request |
| Finish this branch. | `finish-branch` | explicit branch-ending action |
| Review these changes, then help me finish the branch. | `review-and-finish` then `finish-branch` | review and branch wrap-up remain separate and ordered |
