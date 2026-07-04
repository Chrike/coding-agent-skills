# Trigger Matrix

Use this file to pressure-test whether the active development workflow split still behaves as intended.

It is not a runtime skill.
The prompt fragments are authoritative for default behavior, and skill descriptions/bodies are authoritative for routing. This file validates those contracts.

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

## Manual Workflow Cases

| Prompt | Expected routing |
| --- | --- |
| Manually invoke `agent-workflow` for frontend and backend slices. | `agent-workflow` |
| Manually invoke `agent-workflow` for two independent slices plus a fresh-context verifier. | `agent-workflow` |
| Use `agent-workflow` to split this into independent subproblems first, then parallelize only the truly independent ones. | `agent-workflow` |
| Manually invoke `issue-workflow` to turn this into a PRD. | `issue-workflow` |
| Manually invoke `decision-map` for this vague multi-session direction. | `decision-map` |
| Manually invoke `memory-handoff` to prepare for context compression. | `memory-handoff` |
| Manually invoke `markdown-memory` to record the lesson from this repeated review mistake. | `markdown-memory` |
| Before we pause, update the handoff and also record this repeated mistake as a lesson. | `memory-handoff` plus `markdown-memory` |
| Manually invoke `skill-refactorer` to rewrite this old SKILL.md for the current suite. | `skill-refactorer` |
| Use `skill-refactorer` to refactor this outdated CLAUDE fragment without changing task scope. | `skill-refactorer` |
| Manually invoke `effort-calibrator` for this Claude batch route. | `effort-calibrator` |
| Use `effort-calibrator` to review whether this Fable coding workload should stay at `xhigh`. | `effort-calibrator` |

## Shared Default Rule Smoke Cases

These validate prompt-fragment behavior without restating the prompt layer.

| Prompt | Expected behavior |
| --- | --- |
| What does this file say? | Read the file before claiming. |
| These two similarly named files may not mean the same thing. Decide only after reading them. | Read current content instead of inferring from filenames or memory. |
| Here is another model's review; apply it. | Treat it as reference input and verify before changing code. |
| This example is only to clarify the intent, not the implementation direction. | Use it to understand intent without turning the example itself into requested work. |
| We are only inspecting; do not rewrite yet. | Stay in inspection mode. |
| Is this done? | Name verification evidence or state the gap. |
| What are you doing right now, and what is the next step? | Answer directly from current verified state, then continue with the requested stage. |
| What did you actually finish, what failed, and what is still unverified? | Report outcome first and keep done, failed, skipped, and unverified claims aligned with current-session evidence. |
| Summarize this finished work for someone who did not watch the run. | Open with the outcome in plain language instead of internal shorthand or working-note references. |
| Do not give me arrow-chain notes or working shorthand; explain the result in full sentences. | Use reader-facing summary language rather than working-note shorthand. |
| Continue from this handoff file. | Read the named artifact first and follow the latest user request. |
| We already reviewed this. Continue with the next step. | Move to the next requested action instead of repeating the review. |
| Start the changes based on the conclusion above. | Use the settled conclusion and begin the requested action. |
| Implement the approved plan above. | Use the approved plan as execution context instead of reopening planning. |
| Start the reviewed fix above. | Use the reviewed conclusion as execution context instead of reopening review. |
| You already have enough context. Stop planning and implement the next step. | Leave the preparation loop and execute the requested next action. |
| I only want your diagnosis of this deploy regression and the next action you recommend. Do not change anything yet. | Investigate and report findings without making state-changing edits. |
| We already cancelled the runtime-support track. Continue with prompt refactor only. | Keep the cancelled direction closed unless the user reopens it. |
| Handle these three prompt-file follow-ups in one pass. | Keep going through the requested batch until it is complete or blocked. |

## Maintenance / Meta Cases

| Prompt | Expected routing |
| --- | --- |
| Which workflow should handle this? | Answer from `routing-contract.md` and the skill descriptions |
| Review the trigger boundaries. | Use `routing-contract.md` plus the trigger and non-trigger tests |

## Failure Signals

- ordinary coding requires `agent-workflow`
- manual-only workflows trigger from ordinary natural-language prompts
- ordinary coding becomes planning or review chatter
- filenames or old summaries substitute for current source reads
- settled review or planning conclusions are re-opened without new evidence, contradiction, or a new request
- "continue", "start", or "execute" after a completed analysis still loops back into repeated summary
- the agent answers a direct status or stage question indirectly and resumes old analysis instead
- examples used for clarification get misread as implementation instructions
- approved plans or reviewed fixes fail to guide execution directly
- the agent stays in planning or review loops after enough context exists to execute
- cancelled directions get revived without an explicit user request
- a requested batch is broken into unnecessary stop-and-wait cycles
- the base default behavior layer drifts apart from the workflow skills that assume it
- default behavior rules start creeping back into workflow skills unnecessarily
- completion claims appear without evidence
- duplicate durable artifacts are created for the same tracked work
- tracked work stays falsely in progress after completion, pause, or mainline switch
- output shifts toward long process narration instead of code or findings
