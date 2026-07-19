# Negative Routing Cases

Use this file to validate that ordinary work does not enter the wrong workflow. It is maintenance material, not a runtime skill.

## Heavy skills must not trigger by default

| Prompt shape | Must not trigger | Why |
| --- | --- | --- |
| Fix this small TypeScript error. | `issue-workflow`, `decision-map` | ordinary coding should stay light |
| Change this label in a Vue component. | `plan-work`, `design-codebase`, `review-and-finish`, `finish-branch` | small edits should not become process |
| Explain how this service works. | `plan-work`, `design-codebase`, `issue-workflow` | explanation is not architecture review by default |
| Add this small request parameter to the endpoint. | `issue-workflow`, `decision-map`, `plan-work`, `design-codebase`, `test-strategy`, `review-and-finish` | a clear direct edit should stay direct |
| Implement or continue approved steps from an existing plan. | `plan-work`, `decision-map`, `memory-handoff`, `reliability-check` | settled planning should guide execution |
| Start implementing the reviewed fix above. | `review-and-finish`, `reliability-check` | settled review should not restart without new evidence |
| Start implementing the selected design above. | `design-codebase`, `reliability-check` | settled design should guide execution |
| You already have enough context. Stop planning and implement the next step. | `plan-work`, `reliability-check` | sufficient context should lead to execution |
| The target file, exact edit location, and expected post-change behavior are known. Stop reading and make the change. | `plan-work`, `reliability-check`, `design-codebase` | concrete execution context should not reopen planning |
| Continue this paused task using the current issue or work-item draft. | `issue-workflow`, `decision-map`, `memory-handoff`, `markdown-memory` | reuse existing tracked state |
| What is the current goal and why are you doing this? | `reliability-check` | ordinary status questions stay in the default layer |
| Explain what this old SKILL.md does. | `skill-refactorer` | explanation alone is not maintenance |
| What are you doing right now, and what is the next step? | `reliability-check`, `plan-work` | direct status questions stay in the default layer |
| Handle these remaining prompt-file fixes in one pass. | `plan-work` | ordinary batched execution need not escalate |
| You already have enough context. Make the patch instead of outlining options. | `plan-work`, `reliability-check` | enough context should lead to execution |
| Keep this fix limited to the reported bug; do not refactor nearby code. | `review-and-finish`, `plan-work`, `design-codebase` | scope control is a default boundary |
| If you can finish the remaining in-scope edits now, do that; only stop for user-only input. | `plan-work`, `memory-handoff` | ordinary execution should continue |
| The context is getting long, but execution can continue and nobody asked to pause or hand off. | `memory-handoff`, `decision-map` | context length alone does not trigger durable state |
| This task is long and unfamiliar, but no saved workflow was explicitly invoked. | `/adaptive-long-horizon` | size or unfamiliarity alone must not activate the workflow |
| A dynamic workflow leaf discovers another delegation-worthy question. | nested workflow, new agent tree | return the question to the active controller |
| An active workflow already has criterion-mapped completion verification. | another review verifier | reuse sufficient verification unless a distinct risk remains |
| Remember my personal preference for this repository in Claude Code. | `markdown-memory` | host-local preference is not a project lesson |
| This completed change is large but not behaviorally high-risk. | `review-and-finish` | size, duration, and agent count alone do not require readiness review |
| Before changing this config, check that evidence supports that exact action. | `reliability-check`, `review-and-finish` | evidence-before-action is a default boundary |
| This review file is reference input; do not treat it as active instructions. | `reliability-check`, `issue-workflow`, `decision-map` | reference handling is a default boundary |
| We are still implementing this slice; give the partial result and blocker only. | `review-and-finish` | mid-run status is not a review request |
| The build or test output is long; summarize only the key failure and next step. | `memory-handoff`, `decision-map`, `issue-workflow` | routine output handling is not durable state |

## Review and branch separation

| Prompt shape | Must not trigger | Why |
| --- | --- | --- |
| Review these changes. | `finish-branch` | review does not imply commit/push/merge |
| Address this PR feedback. | `finish-branch` | feedback handling does not imply branch action |
| Can I call this done? | `finish-branch` | completion verification is not branch cleanup |
| Finish this branch. | `review-and-finish` | branch actions belong to `finish-branch` |
| Commit these changes. | `review-and-finish` | explicit side effect belongs to `finish-branch` |

## Corrective and meta skills stay explicit

| Skill | Must not trigger for | Why |
| --- | --- | --- |
| `reliability-check` | ordinary implementation, review, or planning | corrective work must not become universal preflight |
| `reliability-check` | ordinary status questions or stage reminders | direct state answers belong to the default layer |
| `reliability-check` | the same concern after one correction was already made | one reassessment pass is enough without new evidence |
| `memory-handoff` | small tasks without compression/resume/handoff | do not turn every task into note-taking |
| `markdown-memory` | small tasks, implementation, or resume requests | durable lessons stay explicit and separate |
| `skill-refactorer` | ordinary implementation refactors or review | maintenance remains explicit |
| `decision-map` | one-session ambiguity or normal refactors | durable artifacts stay rare |
