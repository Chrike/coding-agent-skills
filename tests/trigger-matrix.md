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
| This review file is only reference input; do not treat it as the active instruction source unless I explicitly say so. | Base default behavior |

## Workflow Skill Cases

| Prompt | Expected routing |
| --- | --- |
| This test is flaky; diagnose it. | `debug-systematically` |
| Add regression tests for this bug. | `test-strategy` |
| Implement this change; the correct regression seam and acceptance signal are unclear. | `test-strategy` |
| Review these changes. | `review-and-finish` |
| This completed cross-service permission migration needs a focused readiness check before the done claim. | `review-and-finish` |
| This completed permission migration is ready; verify the final claim before calling it done. | `review-and-finish` |
| `/code-review` | bundled review command |
| Red-team this patch and try to prove it wrong. | `review-and-finish` |
| Address this PR feedback. | `review-and-finish` |
| Tell me whether this draft is actually ready to send. Block it if required criteria are still missing. | `review-and-finish` |
| Investigate these independent subsystems in parallel. | `agent-workflow` |
| Run the same inspect-patch-verify pipeline across this batch of items. | `agent-workflow` |
| Add an independent verifier before we continue. | `agent-workflow` |
| Verify the integrated result independently against its untested rollback path. | `agent-workflow` with a distinct verification evidence question |
| Diagnose these independent failure paths in parallel. | `debug-systematically` + `agent-workflow` |
| Use TDD to implement these independent adapters. | `test-strategy` + `agent-workflow` |
| Review each changed package independently and merge the findings. | `review-and-finish` + `agent-workflow` |
| Compare these independent architecture options. | `design-codebase` + `agent-workflow` |
| Parallelize this multi-file bug investigation, but all symptoms share one root cause. | `agent-workflow` fit check, then `debug-systematically` or base default behavior under one owner |
| Implement independent write slices, but safe worktree isolation is unavailable. | `agent-workflow` with serialized writes |
| Assess these review comments only; do not change code. | `review-and-finish` assessment without implementation |
| Independent agents are unavailable; continue this independent investigation. | `agent-workflow` with sequential controller execution |
| Ultracode is preparing a workflow for these independent subsystems. | `agent-workflow` method for that workflow |
| A workflow for this scope is already running. | continue active workflow; no new orchestration layer |
| Ultracode is enabled; fix this one coherent bug. | `debug-systematically` or base default behavior |
| Finish this branch. | `finish-branch` |
| Commit these changes. | `finish-branch` |
| Push this branch. | `finish-branch` |
| Draft an issue for this bug. | `issue-workflow` |
| Turn this into a PRD. | `issue-workflow` |
| Break this PRD into issues. | `issue-workflow` |
| Update the handoff with the latest checkpoint before we compress. | `memory-handoff` |
| Resume from the latest checkpoint in the current handoff note. | `memory-handoff` |
| Record this repeated mistake as a lesson. | `markdown-memory` |
| Check the lesson memory for this pitfall. | `markdown-memory` |
| Rewrite this old SKILL.md for the current suite. | `skill-refactorer` |
| Tighten this outdated CLAUDE fragment without changing task scope. | `skill-refactorer` |
| Make a decision map for this vague multi-session direction. | `decision-map` |
| Track the open decision frontier for this long-running direction. | `decision-map` |
| Plan this refactor. | `plan-work` |
| Where should this interface live? | `design-codebase` |
| You are hallucinating; reread the files and reassess. | `reliability-check` |
| Reread the files once, correct the wrong source, and then continue implementing the settled fix. | `reliability-check` |
| You are drifting; stop and reassess the active stage. | `reliability-check` |

## Explicit-Intent Workflow Cases

| Prompt | Expected routing |
| --- | --- |
| Prepare a PR for this branch. | `finish-branch` |
| Triage this issue report and give me a tracker-ready draft. | `issue-workflow` |
| Update the handoff before we pause. | `memory-handoff` |
| Remember this correction as a durable lesson. | `markdown-memory` |
| Clean up this outdated prompt file without changing its intended boundary. | `skill-refactorer` |
| Set up a durable decision map for this unresolved direction. | `decision-map` |

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
| The target file, exact edit location, and expected post-change behavior are already known. Stop reading and make the change. | Leaves broad reading and executes the edit or a focused pre-edit step. |

## Maintenance / Meta Cases

| Prompt | Expected routing |
| --- | --- |
| Which workflow should handle this? | Routes from `routing-contract.md` and the skill descriptions without inventing a new router layer. |
| Review the trigger boundaries. | Checks the routing contract and the trigger tests rather than inventing new trigger rules. |

## Failure Signals

- ordinary coding should stay in the base default behavior layer
- orchestration triggers from vague size alone instead of a clearer split, scout, pipeline, verification, or high-stakes shape
- explicit-intent workflows trigger from ordinary natural-language prompts that do not actually ask for branch actions, durable artifacts, maintenance, or calibration work
- approved plans or reviewed fixes fail to guide execution directly
- the base default behavior layer drifts apart from the workflow skills that assume it
