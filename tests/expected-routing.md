# Expected Routing

Use this file to validate that common prompt shapes route to the right layer or skill.

It is not a runtime skill. This file records expected routing outcomes for common prompt shapes. Default behavior comes from `prompts/CLAUDE.fragment.md`, and skill boundaries come from each skill description and `SKILL.md` body.

## Base Default Behavior

These prompts should stay in the base default behavior layer, not load a heavier workflow skill first:

| Prompt Shape | Expected Routing | Why |
| --- | --- | --- |
| Fix this small TypeScript error. | base default behavior | ordinary narrow implementation |
| Change this label in a Vue component. | base default behavior | direct edit with focused verification |
| Explain how this Spring service method works. | base default behavior | code reading and explanation, not planning |
| Add this small request parameter to the endpoint. | base default behavior | small implementation change |
| Implement this feature. | base default behavior | implementation alone does not trigger a heavy workflow |
| Implement the approved steps from this existing plan file. | base default behavior | execution continues from settled planning |
| Continue this paused task using the current issue or work-item draft. | base default behavior | continuation request stays in ordinary execution |
| Start implementing the approved plan above. | base default behavior | settled planning feeds execution |
| Start the reviewed fix above. | base default behavior | settled review feeds execution |
| Answer what you are doing, then continue the current task. | base default behavior | direct status plus continued execution stays in the default layer |
| We already cancelled that older direction. Continue with the current task only. | base default behavior | continuation stays in the default layer |
| Handle these remaining prompt-file fixes in one pass. | base default behavior | batched continuation stays in ordinary execution |

## Core Workflow Skills

These prompts should route to the named workflow skill:

| Prompt Shape | Expected Routing | Why |
| --- | --- | --- |
| This test is flaky; diagnose it. | `debug-systematically` | diagnosis before patching |
| The API returns wrong data after the refactor. | `debug-systematically` | unclear regression |
| Add regression tests for this bug. | `test-strategy` | test design and proof |
| Use TDD for this feature. | `test-strategy` | explicit testing mode |
| Review these changes. | `review-and-finish` | explicit review request |
| Can I call this done? | `review-and-finish` | explicit completion verification |
| Finish this branch. | `finish-branch` | explicit branch-ending action |
| Commit these changes. | `finish-branch` | explicit side-effect action |
| Plan this refactor. | `plan-work` | explicit planning ask |
| Which approach should we take? | `plan-work` | compare approaches before implementation |
| Where should this interface live? | `design-codebase` | architecture / seam decision |
| This module is hard to test. | `design-codebase` | design question, not just test syntax |
| Break this large task into independent subproblems first, then execute. | `agent-workflow` | decompose-first orchestration |
| Scout three independent paths for this failure before choosing one. | `agent-workflow` | divergent exploration / scout routing |
| Run this as a batch pipeline over each file and verify each item separately. | `agent-workflow` | per-item pipeline workflow |
| This is a high-stakes final artifact; generate multiple candidates and judge them. | `agent-workflow` | judge-panel workflow |
| Add an independent secondary reviewer for this high-risk artifact. | `agent-workflow` | explicit extra review path inside the orchestration workflow |
| Add an independent delegated verifier during implementation so we can catch mismatches before the final review. | `agent-workflow` | explicit delegated fresh-context verification |
| Continue from the approved implementation plan, then split the independent slices and delegate them. | `agent-workflow` | settled planning feeds orchestration without reopening planning |

## Explicit Invocation / Corrective Examples

These prompts hit the skills below only when the user explicitly asks for the workflow or explicitly requests corrective reassessment:

| Prompt Shape | Expected Routing | Why |
| --- | --- | --- |
| Manually invoke `agent-workflow` for frontend and backend slices. | `agent-workflow` | manual delegation workflow |
| Manually invoke `issue-workflow` to turn this into a PRD. | `issue-workflow` | durable work-item request |
| Manually invoke `issue-workflow` to break this PRD into issues. | `issue-workflow` | tracker-style decomposition |
| Manually invoke `decision-map` for this vague direction. | `decision-map` | explicit durable decision-tracking request |
| Manually invoke `memory-handoff` before context compression. | `memory-handoff` | explicit handoff / compression |
| Manually invoke `memory-handoff` to update the current handoff note before we pause. | `memory-handoff` | explicit handoff update request |
| Update the handoff with the latest checkpoint before we compress. | `memory-handoff` | explicit checkpoint update before compression |
| Manually invoke `memory-handoff` to resume from the named handoff file. | `memory-handoff` | explicit resume request |
| Resume from the latest checkpoint in the current handoff note. | `memory-handoff` | explicit checkpoint-based resume request |
| You are hallucinating; reread the files and reassess. | `reliability-check` | explicit corrective reassessment |
| Which workflow should handle this? | routing contract plus prompt and skill descriptions | explicit routing question |

## Review Split Check

| Prompt Shape | Expected Routing | Why |
| --- | --- | --- |
| Review these changes. | `review-and-finish` | explicit review request |
| Finish this branch. | `finish-branch` | explicit branch-ending action |
| Review these changes, then help me finish the branch. | `review-and-finish` then `finish-branch` | review and branch wrap-up remain separate and ordered |
