# Trigger Matrix

Use this file to pressure-test whether the active development workflow split still behaves as intended.

It is not a runtime skill.
The maintained prompt file is authoritative for default behavior, and skill descriptions/bodies are authoritative for routing. This file validates those contracts.

## Default Behavior Cases

| Prompt | Expected routing |
| --- | --- |
| Fix this small TypeScript error. | Base default behavior |
| Change this label in a Vue component. | Base default behavior |
| Explain how this Spring service method works. | Base default behavior |
| Add this small request parameter to the endpoint. | Base default behavior |
| Implement the approved steps from this existing plan file. | Base default behavior |
| Continue this paused task using the current issue or work-item draft. | Base default behavior |
| What is the current goal and why are you doing this? | Base default behavior |
| We are still inspecting these files; do not start rewriting yet. | Base default behavior |
| You have enough context now. Make the requested code change instead of giving me another plan. | Base default behavior |
| Fix only the reported bug. Do not clean up neighboring code or add helper layers. | Base default behavior |
| What did you actually finish, what failed, and what is still unverified? | Base default behavior |
| If you can complete the remaining in-scope work now, do it. Only stop if you need input that only I can provide. | Base default behavior |
| Do not use the smallest patch; solve the same bug with a more maintainable approach. | Base default behavior |
| Summarize all the user questions from above, not your own answers. | Base default behavior |
| This is not a new task; only change the output format to a table. | Base default behavior |
| The goal is clear; only the implementation detail is still open, so choose a reasonable default and continue. | Base default behavior |
| Before changing this config, check that the current evidence supports that exact action rather than a nearby guess. | Base default behavior |
| The context is getting long, but the task is still executable. Keep going instead of stopping early just to hand off. | Base default behavior |

## Workflow Skill Cases

| Prompt | Expected routing |
| --- | --- |
| This test is flaky; diagnose it. | `debug-systematically` |
| Add regression tests for this bug. | `test-strategy` |
| Review these changes. | `review-and-finish` |
| Red-team this patch and try to prove it wrong. | `review-and-finish` |
| Tell me whether this draft is actually ready to send. Block it if required criteria are still missing. | `review-and-finish` |
| Finish this branch. | `finish-branch` |
| Plan this refactor. | `plan-work` |
| Where should this interface live? | `design-codebase` |
| You are hallucinating; reread the files and reassess. | `reliability-check` |
| You are drifting; stop and reassess the active stage. | `reliability-check` |
| Break this into independent subproblems first, then parallelize only the real slices. | `agent-workflow` |
| Scout multiple independent explanations for this failure before implementing. | `agent-workflow` |
| Run this batch as per-item extract/transform/verify instead of one big pass. | `agent-workflow` |
| This is a high-stakes final artifact; use multiple candidates plus judges. | `agent-workflow` |
| Add a cross-model reviewer for this high-risk artifact. | `agent-workflow` |
| Add an independent delegated verifier during implementation and report mismatches before we continue. | `agent-workflow` |
| The plan is already approved; now split the independent slices and delegate the real ones. | `agent-workflow` |

## Manual Workflow Cases

| Prompt | Expected routing |
| --- | --- |
| Manually invoke `issue-workflow` to turn this into a PRD. | `issue-workflow` |
| Manually invoke `decision-map` for this vague multi-session direction. | `decision-map` |
| Manually invoke `memory-handoff` to prepare for context compression. | `memory-handoff` |
| Update the handoff with the latest checkpoint before we compress. | `memory-handoff` |
| Resume from the latest checkpoint in the current handoff note. | `memory-handoff` |
| Manually invoke `markdown-memory` to record the lesson from this repeated review mistake. | `markdown-memory` |
| Before we pause, update the handoff and also record this repeated mistake as a lesson. | `memory-handoff` plus `markdown-memory` |
| Manually invoke `skill-refactorer` to rewrite this old SKILL.md for the current suite. | `skill-refactorer` |
| Use `skill-refactorer` to refactor this outdated CLAUDE fragment without changing task scope. | `skill-refactorer` |
| Manually invoke `effort-calibrator` for this batch route. | `effort-calibrator` |
| Use `effort-calibrator` to review whether this coding workload should stay at the current effort level. | `effort-calibrator` |

## Shared Default Rule Smoke Cases

These are representative checks that default-layer handling still happens in the right place.

| Prompt | Expected behavior |
| --- | --- |
| What does this file say? | Reads the file before making source claims. |
| This example is only to clarify the intent, not the implementation direction. | Uses the example to infer intent without treating it as the task. |
| We are only inspecting; do not rewrite yet. | Stays in inspection. |
| Is this done? | Answers with current verification evidence or the remaining gap. |
| Continue from this issue or work-item draft. | Reads the named artifact first and follows the latest request. |
| You already have enough context. Stop planning and implement the next step. | Leaves preparation and executes the next action. |

## Maintenance / Meta Cases

| Prompt | Expected routing |
| --- | --- |
| Which workflow should handle this? | Routes from `routing-contract.md` and the skill descriptions without inventing a new router layer. |
| Review the trigger boundaries. | Checks the routing contract and the trigger tests rather than inventing new trigger rules. |

## Failure Signals

- ordinary coding requires `agent-workflow`
- orchestration triggers from vague size alone instead of a clearer split, scout, pipeline, verification, or high-stakes shape
- durable manual-only workflows trigger from ordinary natural-language prompts
- approved plans or reviewed fixes fail to guide execution directly
- the base default behavior layer drifts apart from the workflow skills that assume it
