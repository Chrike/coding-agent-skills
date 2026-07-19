# Positive Routing Cases

Use this file to pressure-test explicit routing into the smallest applicable layer. It is maintenance material, not a runtime skill; skill descriptions and bodies remain authoritative.

## Default behavior

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
| The existing verification still covers the final code and acceptance criteria. Reuse it instead of rerunning the same check. | Base default behavior |
| If you can complete the remaining in-scope work now, do it. Only stop if you need input that only I can provide. | Base default behavior |
| Do not use the smallest patch; solve the same bug with a more maintainable approach. | Base default behavior |
| Summarize all the user questions from above, not your own answers. | Base default behavior |
| This is not a new task; only change the output format to a table. | Base default behavior |
| The goal is clear; only the implementation detail is still open, so choose a reasonable default and continue. | Base default behavior |
| Before changing this config, check that the current evidence supports that exact action rather than a nearby guess. | Base default behavior |
| The focused test passes, but an acceptance criterion, directly affected contract, or identified behavioral risk remains uncovered. | Base default behavior; complete required verification before stopping |
| The context is getting long, but the task is still executable. Keep going instead of stopping early just to hand off. | Base default behavior |
| This review file is only reference input; do not treat it as the active instruction source unless I explicitly say so. | Base default behavior |

## Explicit skill and workflow intent

| Prompt | Expected routing |
| --- | --- |
| This test is flaky; diagnose it. | `debug-systematically` |
| Claude Code itself is misbehaving; inspect the session logs. | bundled `/debug` |
| Add regression tests for this bug. | `test-strategy` |
| This test depends on sleep and flakes in CI. Fix the wait strategy. | `test-strategy` |
| Implement this change; the correct regression seam and acceptance signal are unclear. | `test-strategy` |
| Review these changes. | `review-and-finish` |
| Review these changes, then commit and push them if the review passes. | `review-and-finish` then `finish-branch` |
| This completed authorization migration needs a focused readiness check before the done claim. | `review-and-finish` |
| `/code-review` | bundled review command |
| Red-team this patch and try to prove it wrong. | `review-and-finish` |
| Address this PR feedback. | `review-and-finish` |
| Tell me whether this draft is actually ready to send. Block it if required criteria are still missing. | `review-and-finish` |
| Add one focused verifier before we continue. | direct focused delegation under the active domain method |
| Independent agents are unavailable; continue this independent investigation. | `agent-workflow` with sequential controller execution |
| Run the installed `/adaptive-long-horizon` command for this explicitly supplied read-only evidence task. | the saved workflow is the sole outer execution owner |
| Run the installed `/fresh-findings-review` command for this explicitly supplied findings-only review. | the saved workflow owns the bounded review pass; `review-and-finish` owns triage, repair, completion, and branch separation |
| Finish this branch. | `finish-branch` |
| Commit these changes. | `finish-branch` |
| Push this branch. | `finish-branch` |
| Draft an issue for this bug. | `issue-workflow` |
| Turn this into a PRD. | `issue-workflow` |
| Break this PRD into issues. | `issue-workflow` |
| Update the handoff before pausing, compressing, or checkpointing. | `memory-handoff` |
| Update the checkpoint before compression while preserving material state. | `memory-handoff` |
| Resume from the latest checkpoint in the current handoff note. | `memory-handoff` |
| Record a repeated mistake or correction as a project-reviewed lesson. | `markdown-memory` |
| Check the project lesson memory for this pitfall. | `markdown-memory` |
| Rewrite or clean up an outdated prompt or skill file without changing its intended boundary. | `skill-refactorer` |
| Make or set up a durable decision map for this vague multi-session direction. | `decision-map` |
| Plan this refactor. | `plan-work` |
| Implement this migration, but a load-bearing compatibility and sequencing decision cannot be safely inferred. | `plan-work` |
| Where should this interface live? | `design-codebase` |
| Implement this integration, but ownership of the dependency boundary is non-obvious. | `design-codebase` |
| You are hallucinating; reread the files and reassess. | `reliability-check` |
| Reread the files once, correct the wrong source, and then continue implementing the settled fix. | `reliability-check` |
| You are drifting; stop and reassess the active stage. | `reliability-check` |

## Shared default smoke cases

| Prompt | Expected behavior |
| --- | --- |
| What does this file say? | Reads the file before making source claims. |
| This example is only to clarify the intent, not the implementation direction. | Uses the example to infer intent without treating it as the task. |
| We are only inspecting; do not rewrite yet. | Stays in inspection. |
| Is this done? | Answers with current verification evidence or the remaining gap. |
| Continue from this issue or work-item draft. | Reads the named artifact first and follows the latest request. |
| You already have enough context. Stop planning and implement the next step. | Leaves preparation and executes the next action. |
| Recommend an approach for integrating this unfamiliar external API. | Reads current authoritative API documentation before behavior-dependent claims. |
| Which product trade-off should we prefer? | Uses evidence to inform the choice without replacing user intent. |
| The decision-relevant external claims are supported and further sources are unlikely to change the recommendation. | Stops researching and proceeds with synthesis or execution. |
