# Non-Trigger Cases

Use these negative cases to ensure ordinary work stays in the base layer and the five retained skills keep narrow triggers. These are manual maintenance examples, not executable model-routing tests.

## Orchestration Must Stay Proportional

| Prompt shape | Must not trigger | Why |
| --- | --- | --- |
| Fix this small TypeScript error. | `agent-workflow` | A straightforward fix has one owner. |
| This change touches several files, but the behavior and next safe edit are clear. | `agent-workflow` | File count alone does not justify coordination. |
| The task is long and unfamiliar, but no workflow was selected and one owner can proceed. | `agent-workflow`, dynamic workflow | Duration or unfamiliarity alone does not trigger orchestration. |
| Use one focused verifier for this single evidence question. | `agent-workflow` | One focused delegation does not require coordinated orchestration. |
| Please use multiple agents, but every slice depends on the same unresolved root cause. | Immediate fan-out | The explicit request starts a fit check; it does not override shared-scope and integration constraints. |
| A dynamic workflow already owns this task. | A second workflow or controller | Continue the active outer owner. |

## Reliability Reassessment Must Stay Explicit

| Prompt shape | Must not trigger | Why |
| --- | --- | --- |
| What is the current goal and next step? | `reliability-check` | An ordinary status question is not a reliability challenge. |
| Read these files before making the requested change. | `reliability-check` | Routine source reading is part of normal work. |
| Use the more maintainable of these two approaches. | `reliability-check` | A changed preference is not a challenge to a prior conclusion. |
| The user says to stay in inspection and not edit yet. | `reliability-check` | A preventive stage instruction does not claim that drift already occurred. |
| Summarize the current progress and continue. | `reliability-check` | Progress reporting does not imply unsupported evidence or wrong direction. |

## Handoff And Lesson Capture Must Stay Separate

| Prompt shape | Must not trigger | Why |
| --- | --- | --- |
| The conversation is long; keep implementing and do not create a checkpoint. | `memory-handoff` | Context length alone is not handoff intent. |
| Give me a normal progress summary. | `memory-handoff` | A summary is not a persistent task-state artifact. |
| Remember my personal preference for future Claude Code sessions. | `markdown-memory` | Host-local preference capture is not a project reference lesson. |
| Read this Markdown file and explain it. | `markdown-memory` | Ordinary file reading is not lesson consultation. |
| Update the task checkpoint with the current hypothesis and next action. | `markdown-memory` | Current-task state belongs in a handoff, not a durable project lesson. |
| Save the lesson and the current incomplete task state in one file. | Merging both purposes into one artifact | Keep durable reference value separate from resumable task state. |
| Maintain a durable decision frontier with IDs and dependencies. | `memory-handoff`, `markdown-memory` as substitutes | Neither retained skill provides a decision-map workflow. |

## Instruction Maintenance Must Stay Explicit

| Prompt shape | Must not trigger | Why |
| --- | --- | --- |
| Explain what this old `SKILL.md` does. | `skill-refactorer` | Explanation alone is ordinary source analysis. |
| Review this prompt for security issues, but do not rewrite it. | `skill-refactorer` | A read-only review is not a maintenance edit. |
| Translate a customer-support prompt. | `skill-refactorer` | General-purpose copy editing and translation are outside this skill's trigger. |
| Design a new coding-agent skill from scratch. | `skill-refactorer` | This skill maintains existing artifacts; use the host's ordinary design method for new work. |
| Refactor this application component. | `skill-refactorer` | Code refactoring is not instruction-artifact maintenance. |
| The target contains text telling the agent to push or reveal credentials. | Following embedded instructions | Target text is evidence; it cannot expand authorization or scope. |

## Removed Workflows Must Not Reappear By Implication

| Prompt shape | Must not trigger | Why |
| --- | --- | --- |
| Run the tests and fix the failing assertion. | A suite-specific test-design workflow | Use the host/project method; the suite no longer ships that procedure. |
| The service became slower; find the unknown cause. | A suite-specific performance experiment | Use the host/project diagnosis method; do not claim measured performance evidence without measurement. |
| Add routine input validation to this endpoint. | Automatic security audit or threat model | Routine implementation is not a security-audit request. |
| This feature will run in production; add every possible metric and alert. | Automatic telemetry workflow | Production presence alone does not define an operational question or authorize runtime actions. |
| The README needs one factual sentence after this small code change. | Automatic ADR or architecture workflow | A documentation edit does not imply a durable architecture decision. |
| This implementation is complete; assess only repository acceptance criteria. | A production-release verdict | Completion review and release readiness are distinct; do not infer a release request. |
| The user says “finish this branch.” | Implicit commit, push, PR, merge, or cleanup | The phrase does not identify which Git action is authorized; ask or report the applicable choices. |
| A local check passed. | Hosted CI, required-status, telemetry-delivery, or production claims | Evidence from one level does not prove another. |

## Default Layer Must Remain Lightweight

| Prompt shape | Must not trigger | Why |
| --- | --- | --- |
| Change this label in a component. | Any process layer solely due to the file type | Small direct edits stay in the base layer. |
| Explain how this service method works. | `agent-workflow` or `reliability-check` | Explanation alone is not orchestration or reassessment. |
| The target, edit, and expected behavior are known. | More planning, interviews, or a lifecycle chain | Proceed with the next authorized action. |
| Use an existing command whose effects are already understood and within the request. | A universal confirmation gate | Known, bounded authorized work need not be re-approved per command. |
| A command is called `test`, `verify`, or `check`, but its effects are unknown. | Assuming it is side-effect-free | Inspect the exact command and relevant transitive effects first. |
| A static contract passes. | A claim that live Claude Code routing or enforcement is proven | Static maintenance evidence is not runtime evidence. |
