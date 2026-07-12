---
name: agent-workflow
description: Use when two or more genuinely independent work slices, a repeated per-item pipeline, divergent scout questions, or multiple coordinated verification questions require multi-agent execution. Defines decomposition, ownership, evidence, verification, and integration contracts across direct subagents, agent teams, and dynamic workflows. Do not use for one focused delegation or verifier, coherent single-owner work, merely because host multi-agent capability is available, or when a workflow for the same scope is already running.
---

# Agent Workflow

Provide the project's multi-agent orchestration method. The host-selected execution substrate may be direct subagents, an agent team, or a dynamic workflow. This skill owns decomposition, ownership, evidence handoff, verification coordination, and integration; it does not own the domain method or the host runtime that launches workers.

## Activation Gate

Use this skill when any of these are true:

- the user explicitly asks to parallelize, scout, or coordinate multiple independent verifiers
- the task has multiple independent questions or write scopes that can make progress without the whole chat history
- the task is a batch of similar items that should run through the same per-item pipeline
- the task is a high-stakes single artifact that justifies multiple independent candidates plus independent reviewers
- verification needs multiple independent evidence questions, verifier owners, staged handoffs, or integration across delegated slices

Stay solo when any of these apply:

- the task is still atomic after a quick read
- the split exists only because the task is long or multi-file
- subtasks share the same files, hidden state, unresolved architecture, or root cause
- every useful slice depends on the same unresolved decision, root cause, or shared design choice, so no slice can make independent progress yet
- clean ownership boundaries or a safe integration path cannot be named
- one focused Explore, Plan, general-purpose delegation, or verifier is enough
- coordination would cost more than the work

An explicit request to parallelize starts this fit check; it does not override the stay-solo conditions. Parallel execution still requires independent ownership, safe write isolation when needed, and a clear integration path.

A dependency between phases is not a reason to avoid orchestration when it can be represented as an explicit staged handoff.

Do not trigger multi-agent work only because intermediate output would be long or host multi-agent capability is available. Prefer host workflow variables, local worker context, or a scratch handoff for long raw output.

One focused Explore, Plan, general-purpose delegation, or verifier is ordinary task execution, not this workflow. Use direct focused verification for one defined evidence question; use this workflow only when verification needs multiple coordinated questions, owners, stages, or integration. Do not wrap an already-selected or already-running dynamic workflow or agent team in another orchestration layer. When a workflow is still being prepared, supply this method into that workflow; when a workflow is already running for the same scope, continue it instead of launching a second orchestration layer.

Hand off to explicit human review when the remaining decision is policy, taste, irreversible product scope, or missing user-only information.

## Decomposition Contract

Before multi-agent execution:

1. State the outcome.
2. Choose one split axis: component, subsystem, artifact, question, failure path, or verification layer.
3. Give every slice one owner and a non-overlapping primary responsibility.
4. Mark dependencies and integration points.
5. Stay single-owner when clean boundaries cannot be named.

Fan-out width follows the number of truly independent subproblems, not a fixed agent count.

## Write-Scope Rules

- Concurrent read-only slices may share a workspace.
- Concurrent write slices require isolated worktrees or equivalent copies.
- If safe isolation is unavailable or not authorized, serialize write slices in the current workspace rather than weaken the isolation rule to preserve parallelism.
- Treat lockfiles, generated output, migrations, repository-wide formatting, git state, shared services, and test databases as shared write scope.

## Controller Contract

Before dispatching:

- State the slices and ownership boundaries.
- Every worker brief must include the goal and expected output, one owner with non-overlapping primary scope, the known evidence, constraints, and excluded scope needed to prevent rediscovery, and a definition of done or applicable acceptance contract.
- For delegable work, state whether the worker is a leaf executor or nested controller and whether further delegation is allowed.
- For work that can write, state the permitted read and write scope, isolation boundary, and any serialization requirement.
- Include the active domain method, compact method capsule, broader references, artifact requirements, inputs, or carry-forward summary only when the slice needs them.
- When using a dynamic workflow, encode the applicable contracts in each `agent()` prompt or structured input. Do not assume main-session skill content is inherited by workflow workers.
- Require every slice to return completed work or a conclusion plus supporting evidence sufficient for integration.
- Include changed paths, checks run, and result summary for coding slices; ranked evidence paths and next probes for scouts; and blockers, artifact pointers, confidence, or recommended next action only when they materially affect integration or exist.
- When later slices depend on earlier results, pass only the smallest carry-forward summary needed.
- Do not forward the controller's whole reasoning, sibling chatter, or long logs unless the next slice truly needs them.

Execution substrate rules:

- Express independent slices as one concurrent phase when the active execution substrate supports safe parallelism.
- Use direct subagents, an agent team, or a dynamic workflow according to the host-selected execution layer.
- Do not create a second orchestration layer when a dynamic workflow has already been selected for the same scope.
- If independent agents are unavailable, do not simulate delegation. Execute the slices sequentially in the controller flow; produce task briefs only when the user asks for them or execution is impossible.

After results return:

1. Read results before trusting them.
2. Check changed paths and shared-contract assumptions for overlap or conflicts.
3. Treat a result as stale when another slice changed a shared contract or dependency it relied on.
4. Integrate deliberately.
5. Ensure the applicable domain method, or the task-specific acceptance contract when no domain method applies, covers the integrated result. Reuse valid per-slice evidence and run only the missing aggregate check.
6. Report the integrated outcome, material evidence, failures, and unresolved gaps. Identify individual owners only when traceability matters.

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
- Put the leaf-or-controller decision in the delegated prompt itself. Before restricting a leaf worker's agent or skill delegation tools, include or preload every domain method and reference the worker must use.
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
