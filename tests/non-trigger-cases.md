# Non-Trigger Cases

Use this file to validate that the current skill suite does not route ordinary work into the wrong workflow.

It is not a runtime skill.
The prompt fragments are authoritative for default behavior, and skill descriptions/bodies are authoritative for routing. This file validates those contracts.

## Heavy Skills Must Not Trigger By Default

These prompt shapes should not trigger the named skills unless the user explicitly asks for that workflow:

| Prompt Shape | Must Not Trigger | Why |
| --- | --- | --- |
| Fix this small TypeScript error. | `agent-workflow`, `issue-workflow`, `decision-map` | ordinary coding should stay light |
| Change this label in a Vue component. | `plan-work`, `design-codebase`, `review-and-finish`, `finish-branch` | small edits should not become process |
| Explain how this service works. | `plan-work`, `design-codebase`, `issue-workflow` | code explanation is not architecture review by default |
| Add this small request parameter to the endpoint. | `issue-workflow`, `decision-map` | small implementation should not become durable workflow |
| Implement this feature. | `agent-workflow` | delegation must stay explicit or approved |
| Implement the approved steps from this existing plan file. | `plan-work`, `decision-map`, `memory-handoff` | existing durable plan should guide execution without reopening adjacent workflows |
| Continue with the changes based on the plan above. | `plan-work`, `reliability-check` | settled planning should guide execution instead of reopening analysis |
| Start implementing the reviewed fix. | `review-and-finish`, `reliability-check` | settled review should not restart before new evidence appears |
| Start implementing the approved plan above. | `plan-work`, `reliability-check` | settled planning should not restart before new evidence appears |
| Start the reviewed fix above. | `review-and-finish`, `reliability-check` | settled review should guide execution instead of reopening adjacent workflows |
| You already have enough context. Stop planning and implement the next step. | `plan-work`, `reliability-check` | sufficient context should lead to execution rather than another planning loop |
| Continue this paused task using the current issue or work-item draft. | `issue-workflow`, `decision-map`, `memory-handoff`, `markdown-memory` | existing tracked state should be reused instead of reopening artifact workflows |
| What is the current goal and why are you doing this? | `reliability-check` | ordinary status questions should not become corrective workflows by default |
| Explain what this old SKILL.md does. | `skill-refactorer` | explanation alone should stay in the default layer unless the user explicitly asks for migration or maintenance |
| This Fable route feels a bit slow. | `effort-calibrator` | generic latency complaints should not auto-route into an explicit effort-calibration workflow |
| Make this cheaper if you can. | `effort-calibrator` | generic cost-cutting should stay in the base flow unless the user explicitly asks for effort calibration |
| What are you doing right now, and what is the next step? | `reliability-check`, `plan-work` | direct status-and-next-step questions should stay in the default layer |
| What actually finished, what failed, and what is still unverified? | `reliability-check`, `plan-work` | evidence-backed status reporting should stay in the default layer rather than becoming a corrective or planning workflow |
| We are still inspecting these files; do not start rewriting yet. | `reliability-check`, `plan-work`, `design-codebase` | stage alignment should stay in the default layer unless the user explicitly asks for corrective reassessment or a new workflow |
| This example is only to clarify the intent, not the implementation direction. | `plan-work`, `design-codebase`, `reliability-check` | clarifying examples should not be turned into task instructions by default |
| We already cancelled that older direction. Continue with the current task only. | `reliability-check`, `decision-map` | settled cancellations should hold without reopening adjacent tracks |
| Handle these remaining prompt-file fixes in one pass. | `plan-work`, `agent-workflow` | ordinary batched execution should not escalate into a new workflow |
| You already have enough context. Make the requested patch now instead of outlining more options. | `plan-work`, `reliability-check` | enough context should lead to execution instead of more planning or corrective reassessment |
| Keep this fix limited to the reported bug; do not refactor nearby code. | `review-and-finish`, `plan-work`, `design-codebase` | scope control for a small fix should stay in the default layer instead of escalating into review, planning, or redesign |
| If you can finish the remaining in-scope edits now, do that; only stop if you need input I have not provided. | `plan-work`, `memory-handoff` | ordinary execution should continue instead of stopping on a self-created checkpoint or handoff |
| Implement this large feature end to end. | `agent-workflow` | implementation size alone should not escalate into a manual delegation workflow |
| Review this finished patch and tell me if it matches the spec. | `agent-workflow` | ordinary completion and review checks should stay in `review-and-finish` unless the user explicitly asks for delegated fresh-context verification |
| Red-team this patch and try to prove it wrong. | `agent-workflow` | adversarial review posture should still stay inside `review-and-finish` unless the user explicitly asks for delegated fresh-context verification |
| Tell me whether this draft is actually ready to send. | `finish-branch`, `agent-workflow` | artifact readiness and PASS/BLOCK-style delivery checks should stay inside `review-and-finish` unless the user explicitly asks for branch actions or delegated verification |

## Review / Branch Split Must Not Collapse

These prompt shapes should keep `review-and-finish` and `finish-branch` separate:

| Prompt Shape | Must Not Trigger | Why |
| --- | --- | --- |
| Review these changes. | `finish-branch` | review should not imply commit/push/merge |
| Can I call this done? | `finish-branch` | completion verification is not branch cleanup |
| Finish this branch. | `review-and-finish` alone | branch-ending actions should not be misrouted as review |
| Commit these changes. | `review-and-finish` alone | explicit side effect should route to manual branch skill |

## Corrective / Meta Skills Must Stay Explicit

These skills should not appear unless the user clearly asks for their layer:

| Skill | Must Not Trigger For | Why |
| --- | --- | --- |
| `reliability-check` | ordinary implementation, ordinary review, ordinary planning | corrective layer should not become universal preflight |
| `reliability-check` | ordinary status questions about current goal or progress | direct state answers should come from the default layer unless the user explicitly flags drift or reassessment |
| `reliability-check` | ordinary stage reminders such as staying in inspection before implementation | preventive stage alignment should come from the default layer unless the user explicitly asks for correction |
| `memory-handoff` | small tasks without compression/resume/handoff | do not turn every task into note-taking |
| `markdown-memory` | small tasks, ordinary implementation, or resume/handoff requests | durable lesson memory should stay explicit and separate from task-state handoff |
| `skill-refactorer` | ordinary implementation refactors, ordinary review, or ordinary planning | prompt and skill maintenance should stay explicit and separate from daily execution workflows |
| `effort-calibrator` | ordinary implementation, generic latency complaints, or generic cost-cutting requests | effort control should stay an explicit calibration workflow rather than a default throttle layer |
| `decision-map` | one-session ambiguity, normal refactors, approach comparison | durable artifacts should stay rare |

## Default Layer Must Not Drift Back Into Skills

These are failure conditions:

- workflow skills start repeating broad default rules that already live in `prompts/`
- `debug-systematically` becomes the default path for obvious one-line fixes
- `test-strategy` makes TDD feel mandatory when the user did not ask for it
- `review-and-finish` starts implying branch actions again
- `finish-branch` starts being treated like an ordinary always-on skill
- ordinary direct status questions stop getting direct answers
- evidence-backed status requests get routed into planning or corrective workflows instead of being answered from current-session evidence
- continuation requests restart planning or review instead of using settled conclusions
- explanation-only requests quietly turn into state-changing edits
- explanation gets used to justify staying in the wrong stage instead of doing the requested next action
- enough context exists but the agent still spends the turn on more planning or option menus
- cancelled or superseded tracks restart without an explicit ask
- ordinary work starts creating duplicate durable artifacts instead of updating the existing tracked state
- completed or paused tracked work is left stale in durable artifacts without a status update
