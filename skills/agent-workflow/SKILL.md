---
name: agent-workflow
description: Use when the task clearly requires decompose-first orchestration, independent subproblem fan-out, scout slices, per-item pipelines, explicit delegated fresh-context verification, high-stakes multi-candidate review, or another explicit delegation request. Keep ordinary implementation in the default flow.
---

# Agent Workflow

Coordinate delegated agent work only when it saves time or context. Keep ordinary implementation in the lightweight development flow.

## First Decision

Use this skill when any of these are true:

- the user explicitly asks you to delegate, parallelize, scout, or add an independent verifier
- the task clearly needs decompose-first orchestration across independent subproblems
- the task needs divergent exploration or scout slices that would otherwise pollute the active conversation
- the task is a batch of similar items that should run through the same per-item pipeline instead of being piled into one controller pass
- the task explicitly needs delegated fresh-context verification during execution rather than only an ordinary end-of-task review
- the task is a high-stakes single artifact that justifies multiple independent candidates plus independent reviewers

Keep the work in one controller flow when any of these apply:

- the task is still atomic after a quick read
- the split exists only because the task is long or multi-file
- subtasks share the same files, hidden state, or unresolved architecture
- one subtask depends on an answer another subtask has not produced yet
- the controller cannot define clean ownership boundaries or integrate the results safely

## Decompose-First Task Tree

Before dispatching anything:

1. State the current goal in one sentence.
2. Choose the split axis: component, subsystem, artifact, question, failure path, or verification layer.
3. List the independent subproblems that can make progress without the whole chat history.
4. Mark dependency ordering where one slice must finish before another can start.
5. Mark the integration points where results must come back together.
6. If you cannot name clean boundaries, keep the work in one controller flow.

Do not fan out before the task tree is clear enough that each slice has a real owner and a review path back into the controller.

## Delegation Fit

Delegate when all are true:

1. There are at least two independent work slices or investigations.
2. Each slice has a clear owner: files, module, subsystem, failing test file, or question.
3. Each slice can make progress from a focused prompt and project files, without the whole chat history.
4. Write scopes do not overlap, or the task is read-only.
5. The controller can review and integrate the results.

Before dispatching, do one quick split check:

- Let fan-out width follow the number of truly independent subproblems you can name, not a fixed agent count.
- If failures may share one root cause, the task needs one coherent design decision, or coordination costs more than doing the work, keep it in one controller flow.

## Controller Contract

Before dispatching:

- State the slices and ownership boundaries.
- Include only task-local context, paths, commands, constraints, and expected output.
- Require each brief to include: goal, inputs, definition of done, constraints, and where to write results.
- Require every slice to return a compact result contract: finding or completed slice, evidence, confidence, open issue, artifact pointer, and recommended next action.
- For coding slices, also require changed paths, test commands, and result summary.
- For read-only or scout slices, require ranked evidence paths, concise conclusions, and unresolved questions that still block a decision.
- When sequential slices depend on earlier results, pass forward only the smallest carry-forward summary needed for the next slice.
- Do not forward the controller's whole reasoning, long scratch notes, sibling-agent chatter, or long logs unless the next slice truly needs them.

Launch available independent agents in the same turn, then work only on non-overlapping controller tasks while they run when that controller work is genuinely useful; otherwise wait for results before integrating.

If independent agents are not being used for the work, do not simulate delegation or claim agents were dispatched. Either produce task briefs for the user to run, or execute the slices sequentially in the controller flow.

Do not duplicate delegated work.

After agents return:

1. Read results before trusting them.
2. Check changed paths for overlap or conflicts.
3. Integrate deliberately.
4. Run focused verification that covers the combined result.
5. Report what each agent did and what you verified.

## Specialized Patterns

Use these references when the delegated shape is clear enough that the controller needs a narrower operating pattern:

- Divergent exploration or evidence gathering: read [scout-slices.md](references/scout-slices.md).
- Repeated per-item stages: read [pipeline-processing.md](references/pipeline-processing.md).
- Separate milestone verifier or blind-spot check: read [fresh-context-verification.md](references/fresh-context-verification.md).
- High-stakes multiple candidates plus judges: read [review-panel.md](references/review-panel.md).
- Long briefs, long reports, or scratch artifacts: read [file-handoffs.md](references/file-handoffs.md).

## Budget And Escalation

Scale orchestration to task risk and independence.

- stay solo when the task is atomic after a quick read or when coordination would cost more than the work
- escalate only as far as the task actually needs
- hand off to explicit human review when the remaining decision is policy, taste, irreversible product scope, or missing user-only information

## Optional Isolation

If isolation is needed, reuse any isolation already in effect. Introduce additional isolation only when the delegated slices genuinely need it. Use manual `git worktree` only after explicit user approval and project-local safety checks.

## Boundaries

Use the more specific workflow instead when the real task is:

- `plan-work` for deciding what to build
- `debug-systematically` for unclear shared-root failures
- `review-and-finish` for explicit code review or completion evidence
- `finish-branch` for explicit commits, PRs, or branch wrap-up
- `memory-handoff` for compression and session resume

This skill handles delegation and integration; it does not upgrade ordinary implementation into a multi-agent workflow.
Add review agents only when risk, independence, and user intent justify the cost.
