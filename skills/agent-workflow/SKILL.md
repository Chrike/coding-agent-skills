---
name: agent-workflow
description: Use when two or more genuinely independent work slices, a repeated per-item pipeline, divergent scout questions, or independent verification require coordinated multi-agent execution. Defines decomposition, ownership, evidence, verification, and integration contracts across direct subagents, agent teams, and dynamic workflows. Do not use for one focused delegation or coherent single-owner work.
---

# Agent Workflow

Provide the project's multi-agent orchestration method. The host-selected execution substrate may be direct subagents, an agent team, or a dynamic workflow. This skill owns decomposition, ownership, evidence, verification, and integration; it does not own the host runtime that launches workers.

## First Decision

Use this skill when any of these are true:

- the user explicitly asks to parallelize, scout, or add an independent verifier
- the task has multiple independent questions or write scopes that can make progress without the whole chat history
- the task is a batch of similar items that should run through the same per-item pipeline
- the task is a high-stakes single artifact that justifies multiple independent candidates plus independent reviewers
- independent verification is needed during execution, not only as an ordinary end-of-task status check

Keep the work in one controller flow when any of these apply:

- the task is still atomic after a quick read
- the split exists only because the task is long or multi-file
- subtasks share the same files, hidden state, unresolved architecture, or root cause
- one subtask depends on an answer another subtask has not produced yet
- clean ownership boundaries or a safe integration path cannot be named
- one focused Explore, Plan, or general-purpose delegation is enough

Do not trigger multi-agent work only because intermediate output would be long. Prefer host workflow variables, local worker context, or a scratch handoff for long raw output.

## Decomposition Contract

Before multi-agent execution:

1. State the outcome.
2. Choose one split axis: component, subsystem, artifact, question, failure path, or verification layer.
3. Give every slice one owner and a non-overlapping primary responsibility.
4. Mark dependencies and integration points.
5. Stay single-owner when clean boundaries cannot be named.

Fan-out width follows the number of truly independent subproblems, not a fixed agent count.

## Delegation Fit

Delegate only when all are true:

1. There are at least two independent work slices or investigations.
2. Each slice has a clear owner: files, module, subsystem, failing test, or question.
3. Each slice can make progress from a focused prompt and project files.
4. The controller can review and integrate the results.

Write-scope rules:

- Concurrent read-only slices may share a workspace.
- Concurrent write slices require isolated worktrees or equivalent copies.
- Treat lockfiles, generated output, migrations, repository-wide formatting, git state, shared services, and test databases as shared write scope.

If failures may share one root cause, the task needs one coherent design decision, or coordination costs more than the work, keep it in one controller flow.

## Controller Contract

Before dispatching:

- State the slices and ownership boundaries.
- Pass only task-local context workers cannot safely infer: goal, inputs, constraints, known evidence, excluded scope, expected output, and definition of done.
- Require every slice to return a compact result: conclusion or completed work, evidence, confidence, open issues, artifact pointer, and recommended next action.
- For coding slices, also require changed paths, checks run, and result summary.
- For scout slices, require ranked evidence paths, concise conclusions, and unresolved blockers.
- When later slices depend on earlier results, pass only the smallest carry-forward summary needed.
- Do not forward the controller's whole reasoning, sibling chatter, or long logs unless the next slice truly needs them.

Execution substrate rules:

- Express independent slices as one concurrent phase when the active execution substrate supports safe parallelism.
- Use direct subagents, an agent team, or a dynamic workflow according to the host-selected execution layer.
- Do not create a second orchestration layer when a dynamic workflow has already been selected for the same scope.
- If independent agents are unavailable, do not simulate delegation. Either produce task briefs for the user to run, or execute the slices sequentially in the controller flow.

After results return:

1. Read results before trusting them.
2. Check changed paths and shared-contract assumptions for overlap or conflicts.
3. Treat a result as stale when another slice changed a shared contract or dependency it relied on.
4. Integrate deliberately.
5. Run focused verification that covers the combined result.
6. Report what each owner did and what was verified.

## Direct Delegation Versus Orchestration

- One focused Explore, Plan, or general-purpose delegation is ordinary task execution, not this workflow.
- Use this skill only when multiple owners, dependencies, integration points, or repeated pipeline stages must be coordinated.
- Do not wrap an already-selected dynamic workflow or agent team in another orchestration layer.

## Method Ownership

- This skill owns only decomposition, assignment, dependency ordering, evidence handoff, verification coordination, and integration.
- The active domain skill owns the debugging, testing, design, review, feedback, or completion method.
- Do not invent a second search, debugging, testing, design, or review procedure beside the active domain method.
- Translate the active domain method into non-overlapping delegated slices instead of running a parallel procedure.

## Single-Owner Execution

- Assign exactly one execution owner to each investigation question, write scope, implementation slice, or focused verification.
- A delegated owner owns the search, reading, modification, and focused checks inside its assigned scope.
- The controller must not repeat the same search or modification while the delegated owner is active.
- Before delegation, perform only the minimum scan needed to define ownership boundaries.
- Pass already-known files, evidence, constraints, and excluded scope into the brief so the owner does not rediscover them.
- After results return, inspect only what is necessary to integrate, resolve a contradiction, or verify a load-bearing claim.
- Do not rerun the entire delegated investigation by default.

Re-check delegated work only when:

- the result lacks evidence required for integration
- two results contradict each other
- relevant code or shared contracts changed after the investigation
- the delegated scope was incomplete
- independent verification was explicitly part of the task

## Nested Delegation And Exit

- Ordinary workers remain leaf executors.
- Workers must not activate `agent-workflow` or spawn additional agents unless they were explicitly assigned as nested controllers with a defined integration boundary.
- Exit after delegated results are integrated and the combined result has focused verification.
- Do not continue spawning agents for ordinary follow-up edits, formatting, or small fixes.
- Re-enter only when a new set of genuinely independent slices or a new delegated verification need appears.

## Specialized Patterns

Use these references when the delegated shape is clear:

- Divergent exploration: [scout-slices.md](references/scout-slices.md)
- Repeated per-item stages: [pipeline-processing.md](references/pipeline-processing.md)
- Separate milestone verifier: [fresh-context-verification.md](references/fresh-context-verification.md)
- High-stakes candidates plus judges: [review-panel.md](references/review-panel.md)
- Long briefs or reports: [file-handoffs.md](references/file-handoffs.md)

## Budget And Escalation

- Stay solo when the task is atomic after a quick read or coordination would cost more than the work.
- Escalate only as far as independence and risk require.
- Hand off to explicit human review when the remaining decision is policy, taste, irreversible product scope, or missing user-only information.

## Optional Isolation

Reuse any isolation already in effect. Introduce additional isolation only when delegated write slices genuinely need it. Use manual `git worktree` only after explicit user approval and project-local safety checks.

## Boundaries

Use the more specific workflow instead when the real task is:

- `plan-work` for deciding what to build
- `debug-systematically` for unclear shared-root failures
- `review-and-finish` for explicit code review, feedback, or completion evidence
- `finish-branch` for explicit commits, PRs, or branch wrap-up
- `memory-handoff` for compression and session resume

This skill handles multi-agent method and integration; it does not upgrade ordinary implementation into a multi-agent workflow.
