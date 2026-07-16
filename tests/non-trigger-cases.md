# Non-Trigger Cases

Use this file to validate that the current skill suite does not route ordinary work into the wrong workflow.

This file contains negative routing examples for ordinary work.

## Heavy Skills Must Not Trigger By Default

These prompt shapes should not trigger the named skills unless the user clearly asks for that kind of workflow or action:

| Prompt Shape | Must Not Trigger | Why |
| --- | --- | --- |
| Fix this small TypeScript error. | `issue-workflow`, `decision-map` | ordinary coding should stay light |
| Change this label in a Vue component. | `plan-work`, `design-codebase`, `review-and-finish`, `finish-branch` | small edits should not become process |
| Explain how this service works. | `plan-work`, `design-codebase`, `issue-workflow` | code explanation is not architecture review by default |
| Add this small request parameter to the endpoint. | `issue-workflow`, `decision-map`, `plan-work`, `design-codebase`, `test-strategy`, `review-and-finish` | a clear direct edit should not become a planning, design, test-design, or review workflow |
| Implement or continue the approved steps from this existing plan file. | `plan-work`, `decision-map`, `memory-handoff`, `reliability-check` | settled planning should guide execution without reopening planning, reassessment, or handoff workflows |
| Start implementing the reviewed fix above. | `review-and-finish`, `reliability-check` | settled review should not restart before new evidence appears |
| Start implementing the selected design above. | `design-codebase`, `reliability-check` | settled design should guide execution instead of reopening architecture comparison |
| You already have enough context. Stop planning and implement the next step. | `plan-work`, `reliability-check` | sufficient context should lead to execution rather than another planning loop |
| The target file, exact edit location, and expected post-change behavior are already known. Stop reading and make the change. | `plan-work`, `reliability-check`, `design-codebase` | once execution context is concrete, ordinary work should act rather than reopening planning, reassessment, or redesign |
| Continue this paused task using the current issue or work-item draft. | `issue-workflow`, `decision-map`, `memory-handoff`, `markdown-memory` | existing tracked state should be reused instead of reopening artifact workflows |
| What is the current goal and why are you doing this? | `reliability-check` | ordinary status questions should not become corrective workflows by default |
| Explain what this old SKILL.md does. | `skill-refactorer` | explanation alone should stay in the default layer unless the user explicitly asks for migration or maintenance |
| What are you doing right now, and what is the next step? | `reliability-check`, `plan-work` | direct status-and-next-step questions should stay in the default layer |
| What actually finished, what failed, and what is still unverified? | `reliability-check`, `plan-work` | evidence-backed status reporting should stay in the default layer rather than becoming a corrective or planning workflow |
| We are still inspecting these files; do not start rewriting yet. | `reliability-check`, `plan-work`, `design-codebase` | stage alignment should stay in the default layer unless the user explicitly asks for corrective reassessment or a new workflow |
| This example is only to clarify the intent, not the implementation direction. | `plan-work`, `design-codebase`, `reliability-check` | clarifying examples should not be turned into task instructions by default |
| We already cancelled that older direction. Continue with the current task only. | `reliability-check`, `decision-map` | settled cancellations should hold without reopening adjacent tracks |
| Handle these remaining prompt-file fixes in one pass. | `plan-work` | ordinary batched execution should not escalate into a new workflow |
| You already have enough context. Make the requested patch now instead of outlining more options. | `plan-work`, `reliability-check` | enough context should lead to execution instead of more planning or corrective reassessment |
| Keep this fix limited to the reported bug; do not refactor nearby code. | `review-and-finish`, `plan-work`, `design-codebase` | scope control for a small fix should stay in the default layer instead of escalating into feedback, planning, or redesign |
| If you can finish the remaining in-scope edits now, do that; only stop if you need input I have not provided. | `plan-work`, `memory-handoff` | ordinary execution should continue instead of stopping on a self-created checkpoint or handoff |
| This test is flaky because it waits with sleep; fix the test design. | `debug-systematically` | flaky tests caused primarily by wait strategy or test shape should stay in `test-strategy` |
| Claude Code itself is misbehaving; inspect the session logs. | `debug-systematically` | host runtime issues should not route into the project debugging skill; they should use bundled `/debug` instead |
| `/code-review` | `review-and-finish` | an explicit bundled review command should stay with the host review engine instead of re-entering the project review skill |
| Tell me whether this draft is actually ready to send. | `finish-branch` | artifact readiness and PASS/BLOCK-style delivery checks should stay inside `review-and-finish` unless the user explicitly asks for branch actions or delegated verification |
| Add one focused verifier or Explore for one search/evidence question, but do not reopen planning. | `agent-workflow`, `plan-work` | one defined focused delegation is ordinary execution while settled planning stays settled; it is not multi-agent orchestration |
| This multi-file change is still one coherent owner scope. | `agent-workflow` | multi-file alone must not trigger multi-agent orchestration |
| The shared root cause is still unclear; fan out scouts immediately. | `agent-workflow` | unresolved shared-root diagnosis must start with `debug-systematically`, not scout fan-out |
| Host multi-agent capability is available; fix this one coherent bug. | `agent-workflow` | host multi-agent capability alone is not an orchestration trigger |
| A host multi-agent workflow for this scope is already running. | `agent-workflow` | do not start a second orchestration layer over an active workflow |
| Do not use the smallest patch; solve the same bug with a more maintainable approach. | `plan-work`, `design-codebase` | a strategy change should not be misread as a new task or redesign request by default |
| Summarize all the user questions from above, not your own answers. | `reliability-check`, `issue-workflow` | summary-object correction should stay in the default layer rather than becoming corrective analysis or artifact drafting |
| This is not a new task; only change the output format to a table. | `plan-work`, `reliability-check` | a format correction should not be misread as task replacement or corrective workflow |
| The goal is clear; only the implementation detail is still open, so pick a reasonable default and continue. | `plan-work`, `reliability-check`, `design-codebase` | implementation-detail ambiguity alone should not force a planning, corrective, or redesign workflow |
| The context is getting long and the task has many files or agents, but execution can continue and no one asked to pause, checkpoint, hand off, compress, or resume it. | `memory-handoff`, `decision-map` | context length, duration, file count, or agent count alone should not trigger a handoff or durable state workflow |
| This task is long and unfamiliar, but no saved workflow was explicitly invoked. | `/adaptive-long-horizon` | task size or unfamiliarity alone must not activate the saved workflow |
| An adaptive workflow leaf discovered another delegation-worthy question. | `agent-workflow`, nested workflow, new agent tree | return the question to the active workflow instead of adding an orchestration layer (**needs-review:** no separate suite-level destination) |
| An active workflow already has criterion-mapped completion verification. | another review verifier | reuse sufficient verification unless a distinct load-bearing risk remains uncovered (**needs-review:** workflow completion-verifier ownership has no separate suite-level destination) |
| Remember my personal preference for this repository in Claude Code. | `markdown-memory` | host auto memory for a personal or host-local learning must not create a project lesson |
| This completed change has a large diff and took multiple agents, but it affects no behavioral high-risk area. | `review-and-finish` | diff size, duration, and agent count alone do not require a focused readiness check |
| Before changing this config, check that the evidence supports that exact action first. | `reliability-check`, `review-and-finish` | evidence-before-action should stay in the default layer unless the user explicitly asks for reassessment or completion review |
| This review file is only reference input; do not treat it as the active instruction source unless I explicitly say so. | `reliability-check`, `issue-workflow`, `decision-map` | reference-vs-instruction handling should stay in the default layer unless the user explicitly asks for corrective reassessment or a durable artifact workflow |
| Update the handoff with the latest checkpoint before we compress. | `review-and-finish` | explicit checkpoint and compression work should stay in `memory-handoff` (**needs-review:** no dedicated routing-eval destination) |
| We are still implementing this slice; give me the current partial result and blocker only. | `review-and-finish` | mid-run status reporting should stay in the default layer unless the user explicitly asks for delegation |
| The build or test output is very long; summarize only the key failure, blocker, and next step instead of pasting the full log. | `memory-handoff`, `decision-map`, `issue-workflow` | routine long command output handling should stay in the default layer unless the user explicitly asks for durable tracking |
| Prototype this interface only by installing a package, calling an external service, retaining a route or output file, or changing real data. | `design-codebase` automatic prototype | a prototype outside the local throwaway gate requires user agreement |

## Review / Branch Split Must Not Collapse

These prompt shapes should keep `review-and-finish` and `finish-branch` separate:

| Prompt Shape | Must Not Trigger | Why |
| --- | --- | --- |
| Review these changes. | `finish-branch` | review should not imply commit/push/merge |
| Address this PR feedback. | `finish-branch` | feedback handling should not imply commit/push/merge |
| Can I call this done? | `finish-branch` | completion verification is not branch cleanup |
| Finish this branch. | `review-and-finish` | branch-ending actions should route to `finish-branch`, not review |
| Commit these changes. | `review-and-finish` | explicit side effect should route to `finish-branch`, not completion review |

## Corrective / Meta Skills Must Stay Explicit

These skills should not appear unless the user clearly asks for their layer:

| Skill | Must Not Trigger For | Why |
| --- | --- | --- |
| `reliability-check` | ordinary implementation, ordinary review, ordinary planning | corrective layer should not become universal preflight |
| `reliability-check` | ordinary status questions about current goal or progress | direct state answers should come from the default layer unless the user explicitly flags drift or reassessment |
| `reliability-check` | ordinary stage reminders such as staying in inspection before implementation | preventive stage alignment should come from the default layer unless the user explicitly asks for correction |
| `reliability-check` | the same reliability concern after the correction was already stated once | one reassessment pass should be enough unless the user supplies new evidence |
| `memory-handoff` | small tasks without compression/resume/handoff | do not turn every task into note-taking |
| `markdown-memory` | small tasks, ordinary implementation, or resume/handoff requests | durable lesson memory should stay explicit and separate from task-state handoff |
| `skill-refactorer` | ordinary implementation refactors, ordinary review, or ordinary planning | prompt and skill maintenance should stay explicit and separate from daily execution workflows |
| `decision-map` | one-session ambiguity, normal refactors, approach comparison | durable artifacts should stay rare |

## Default Layer Must Not Drift Back Into Skills

Treat the cases above as failure signals if ordinary work starts routing into skills by default, if settled execution context gets reopened without cause, or if tracked state becomes stale instead of being updated.
