---
name: agent-workflow
description: Use when the task clearly requires decompose-first orchestration, independent subproblem fan-out, divergent exploration or scout slices, explicit delegated fresh-context verification during execution, per-item pipeline work, high-stakes multi-candidate review, or an explicit delegation request. Keep ordinary implementation in the default flow.
---

# Agent Workflow

Coordinate delegated agent work only when it saves time or context. Keep ordinary implementation in the lightweight development flow.

## First Decision

Use this skill when any of these are true:

- the user explicitly invokes it, or explicitly asks you to delegate, parallelize, scout, or add an independent verifier
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

High-value patterns:

- at least two truly independent slices can run in parallel and reduce wall-clock time
- a fresh-context verifier can check completed output against the spec without inheriting the controller's assumptions
- a repeated per-item workflow can run as an item pipeline instead of being aggregated into one large controller pass
- a high-stakes single artifact can justify multiple candidates plus independent judges
- the work can be split cleanly enough that delegation reduces coordination noise instead of creating more of it
- dependent slices can be handled in sequence with short carry-forward summaries instead of forcing fake parallelism

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

## Scout / Divergent Exploration

When the problem is still open-ended, dispatch scout slices before implementation:

- split scouts by orthogonal lenses such as failure path, architecture option, source type, or subsystem boundary
- require scouts to rank sources or evidence instead of dumping raw search output
- require scouts to separate source-backed facts, working assumptions, stale or version-sensitive material, unresolved questions, and recommended next probes
- dedupe overlapping findings before escalating into implementation work
- keep scout output to evidence, unresolved questions, and recommended next probes; scouts do not write the final conclusion for the controller
- stop after consecutive dry rounds when new scouts are no longer producing materially new evidence

## Pipeline Processing

When the task is a batch of similar items, run each item through the same small pipeline instead of stuffing the whole batch into one controller thread.

- keep the per-item stages explicit, such as extract -> transform -> verify
- let each item complete or fail independently instead of waiting for a global barrier that is not required by the task
- report item-level outcomes rather than one vague batch summary
- do not silently drop failed verification; keep the failed item visible with its evidence and next action

## Fresh-Context Verification

Use a separate delegated verifier whenever milestone risk or blind-spot cost justifies it, not only at final completion.

- Run a verifier at meaningful milestones or after a small batch of dependent slices before compounding more work on top.
- Give the verifier the specification, changed output, verification scope, and expected report format.
- Do not give the verifier your original reasoning unless the task truly requires it.
- The verifier checks for mismatches against the spec; it does not re-implement the task.
- The verifier reports blocker, mismatch, or no issue found; it does not claim absolute correctness.
- If a verifier finds a blocker that invalidates later work, fix or re-scope before further fan-out.
- Do not turn every tiny delegated step into implementer plus verifier by default.

## Independent Review Panel

Use multiple independent candidates plus independent reviewers only for a high-stakes single artifact where one answer matters more than speed.

- generate multiple independent candidates only when the artifact is important enough to justify the extra cost
- judge candidates against an explicit rubric, not against vibe or familiarity
- synthesize from the strongest candidate after the reviewers score it; do not average incompatible answers into mush
- do not turn ordinary implementation or low-risk review into a default multi-candidate ceremony
- treat any extra reviewer as another lens on possible defects, not as a final arbiter over current code or evidence
- if extra review conflicts with stronger local evidence, verify against the artifact instead of deferring to labels or prestige
- do not gate ordinary delivery on extra reviewer coverage by default

## Budget And Escalation

Scale orchestration to task risk and independence.

- stay solo when the task is atomic after a quick read or when coordination would cost more than the work
- escalate only as far as the task actually needs
- hand off to explicit human review when the remaining decision is policy, taste, irreversible product scope, or missing user-only information

## File Handoffs

Use files when prompts or reports would become long:

- task brief: exact requirements and ownership
- report: findings, evidence, confidence, open issues, changed paths, commands, and recommended next action
- review notes: controller decisions, checkpoints, and unresolved items

When intermediate context would pollute the active conversation, prefer project-local scratch files for long briefs, scout reports, long reports, or batch verification output, then have the controller read and condense them.
Prefer project-local scratch paths that are easy to remove. Create durable notes only when the work is long-running, likely to hit context compression, or the user asks.

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
