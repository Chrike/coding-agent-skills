---
name: plan-work
description: Use when the user asks for planning, an implementation plan, approach comparison, task breakdown, roadmap, step-by-step plan, or splitting a feature/refactor into clear implementation slices before coding, or when a requested implementation has unresolved approach, dependency, sequencing, migration, compatibility, or scope decisions that cannot be safely inferred.
---

# Plan Work

Plan only when planning will reduce risk or clarify execution. Keep ordinary edits in the lightweight development flow.

## First Decision

- If the user asks only to plan, do not implement until they ask.
- If the task is a small obvious edit or the next safe implementation step is already clear, do not create a plan.
- A task being large, medium-complexity, or multi-file is not by itself a planning trigger.
- If a requested implementation has unresolved approach, dependency, sequencing, migration, compatibility, or scope decisions that cannot be safely inferred, use this workflow to settle only those decisions.
- If requirements are unclear, ask the smallest question that changes scope, risk, or approach.
- If a decision is non-obvious, compare the smallest useful set of approaches with trade-offs and a recommendation.
- If the work is too large for one pass, split it into vertical slices.

## Planning Loop

1. Inspect the relevant code, docs, commands, or prior notes before committing to a plan.
2. State the goal in one sentence.
3. Name constraints that affect the implementation: platform, existing patterns, dependencies, performance, data migration, compatibility, or user workflow.
4. Choose an approach. For meaningful alternatives, explain why the chosen option fits best.
5. Break work into executable steps with likely files, verification points, and dependencies.
6. Call out risks, unknowns, and out-of-scope items.

## Plan Shape

For normal project work, use a compact plan in chat. For handoff, long-running, or multi-session work, write a markdown plan only if the user requests a file or the work needs a durable artifact.

Read [plan-template.md](references/plan-template.md) when producing a durable implementation plan.

Read [vertical-slices.md](references/vertical-slices.md) when splitting a feature, refactor, or PRD into independently useful chunks.

Read [design-questions.md](references/design-questions.md) when the request is still too vague to plan safely.

## Exit To Implementation

- When a request includes implementation, treat planning as a transient internal phase: once the needed decisions are settled, exit to implementation automatically unless user-only input, an irreversible trade-off, or a scope change remains.
- When the user asks only to plan, do not implement until they ask.
- Do not regenerate, expand, or compare the settled plan unless new evidence changes scope, dependencies, risk, or feasibility.
- Treat the settled plan as execution context, not as a reason to plan again.

## Boundaries

Do not automatically create PRDs, specs, ADRs, issues, decision maps, or subagent workflows.

Do not save plans to a project-specific planning path, publish issue tracker items, or require approval gates unless the user asks for that workflow.
