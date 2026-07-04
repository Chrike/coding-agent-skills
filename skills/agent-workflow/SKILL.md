---
name: agent-workflow
description: Manual-only. Use only when the user explicitly invokes this skill for subagents, parallel slices, fresh-context verification, or reducing main-window coordination noise through clearly bounded delegated work. Keep ordinary implementation in the default flow.
disable-model-invocation: true
---

# Agent Workflow

Coordinate delegated agent work only when it saves time or context. Keep ordinary implementation in the lightweight development flow.

## First Decision

- Do not use this skill for ordinary code edits, straightforward bugs, normal planning, or normal review.
- Do not delegate just because a task is large or multi-file.
- Use this skill only when the user explicitly invokes it, or explicitly asks you to delegate, parallelize, or add an independent verifier.
- Once this skill is active, you may continue using it after the user approves delegation for independent slices you identified.
- If a task is still atomic after a quick read of the work, keep it in one controller flow.
- Only fan out after you can name the independent subproblems or slices clearly enough to hand them off.
- If tasks share the same files, hidden state, or uncertain architecture, keep the work in one controller flow until the boundary is clear.

## Delegation Fit

Delegate when all are true:

1. There are at least two independent work slices or investigations.
2. Each slice has a clear owner: files, module, subsystem, failing test file, or question.
3. Each slice can make progress from a focused prompt and project files, without the whole chat history.
4. Write scopes do not overlap, or the task is read-only.
5. The controller can review and integrate the results.

Before dispatching, do one quick split check:

- If the task is still one atomic unit, do not fan out.
- If the split only exists because the task is long, do not fan out.
- If one subtask needs the unresolved answer from another, keep them sequential until that dependency is removed.
- Let fan-out width follow the number of truly independent subproblems you can name, not a fixed agent count.

Do not delegate when failures may share one root cause, the task needs one coherent design decision, or coordinating agents costs more than doing the work.

High-value patterns:

- at least two truly independent slices can run in parallel and reduce wall-clock time
- a fresh-context verifier can check completed output against the spec without inheriting the controller's assumptions
- the work can be split cleanly enough that delegation reduces coordination noise instead of creating more of it
- dependent slices can be handled in sequence with short carry-forward summaries instead of forcing fake parallelism

## Controller Contract

Before dispatching:

- State the slices and ownership boundaries.
- Include only task-local context, paths, commands, constraints, and expected output.
- Require each brief to include: goal, inputs, definition of done, constraints, and where to write results.
- Tell agents they are not alone in the codebase and must not revert unrelated changes.
- For coding slices, require changed paths, test commands, and result summary.
- For read-only slices, require evidence paths and concise conclusions.
- When sequential slices depend on earlier results, pass forward only the smallest carry-forward summary needed for the next slice.
- Do not forward the controller's whole reasoning, long scratch notes, or sibling-agent chatter unless the next slice truly needs it.

If the environment provides actual delegated-agent runtime support, launch independent agents in the same turn, then work only on non-overlapping controller tasks while they run when that controller work is genuinely useful; otherwise wait for results before integrating.

If no actual delegated-agent runtime support exists, do not simulate delegation or claim agents were dispatched. Either produce task briefs for the user to run, or execute the slices sequentially in the controller flow.

Do not duplicate delegated work.

After agents return:

1. Read results before trusting them.
2. Check changed paths for overlap or conflicts.
3. Integrate deliberately.
4. Run focused verification that covers the combined result.
5. Report what each agent did and what you verified.

## Fresh-Context Verification

Use a separate verifier only when acceptance risk or blind-spot cost justifies it.

- Give the verifier the specification, changed output, verification scope, and expected report format.
- Do not give the verifier your original reasoning unless the task truly requires it.
- The verifier checks for mismatches against the spec; it does not re-implement the task.
- Do not turn every delegated run into implementer plus verifier by default.

## File Handoffs

Use files when prompts or reports would become long:

- task brief: exact requirements and ownership
- report: findings, changed paths, commands, results, concerns
- review notes: controller decisions and unresolved items

When intermediate context would pollute the main window, prefer project-local scratch files for long briefs, long reports, or batch verification output, then have the controller read and condense them.
Prefer project-local scratch paths that are easy to remove. Do not create durable ledgers unless the work is long-running, likely to hit context compression, or the user asks.

## Optional Isolation

Do not create worktrees, branches, commits, pushes, or dependency installs by default.

If isolation is needed, first detect whether the current agent/runtime already provides it. Prefer built-in isolation features when available. Use manual `git worktree` only after explicit user approval and project-local safety checks.

## Boundaries

This skill does not replace:

- `plan-work` for deciding what to build
- `debug-systematically` for unclear shared-root failures
- `review-and-finish` for explicit code review or completion evidence
- `finish-branch` for explicit commits, PRs, or branch wrap-up
- `memory-handoff` for compression and session resume

This skill handles delegation and integration; it does not upgrade ordinary implementation into a multi-agent workflow. If the user is simply asking to implement, fix, explain, or continue an approved path, stay in the default flow or the more specific skill.
Do not force every delegated task through implementer plus reviewer plus final branch review. Add review agents only when risk, independence, and user intent justify the cost.
