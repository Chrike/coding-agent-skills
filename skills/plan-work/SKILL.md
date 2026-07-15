---
name: plan-work
description: Use when the user asks for planning, an implementation plan, approach comparison, task breakdown, roadmap, step-by-step plan, or splitting a feature/refactor into clear implementation slices before coding, or when a requested implementation has unresolved approach, dependency, sequencing, migration, compatibility, or scope decisions that cannot be safely inferred.
---

# Plan Work

Plan only when planning will reduce risk or clarify execution. Keep ordinary edits in the lightweight development flow.

## First Decision

- If the user asks only to plan, do not implement until they ask.
- If the next safe implementation step is already clear, do not create a plan; task size or file count alone is not a trigger.
- If a requested implementation has unresolved approach, dependency, sequencing, migration, compatibility, or scope decisions that cannot be safely inferred, use this workflow to settle only those decisions.
- If requirements are unclear, ask the smallest question that changes scope, risk, or approach.
- If a decision is non-obvious, compare the smallest useful set of approaches with trade-offs and a recommendation.
- If the work is too large for one pass, split it into vertical slices.

## Planning Loop

1. Inspect the relevant code, docs, commands, or prior notes before committing to a plan.
2. State the goal, constraints, chosen approach, executable steps, dependencies, verification points, risks, and out-of-scope items; compare alternatives only when the decision is genuinely non-obvious.

## Plan Shape

Use a compact plan for normal work. Write a markdown plan for handoff, long-running, or multi-session work only when the user requests it or a durable artifact is needed.

Read [plan-template.md](references/plan-template.md) when producing a durable implementation plan.

Read [vertical-slices.md](references/vertical-slices.md) when splitting a feature, refactor, or PRD into independently useful chunks.

Read [design-questions.md](references/design-questions.md) when the request is still too vague to plan safely.

## Exit To Implementation

- When a request includes implementation, treat planning as a transient internal phase: once the needed decisions are settled, exit to implementation automatically unless user-only input, an irreversible trade-off, or a scope change remains.
- When the user asks only to plan, do not implement until they ask.
- Do not regenerate, expand, or compare a settled plan unless new evidence changes scope, dependencies, risk, or feasibility; a settled plan is execution context, not a reason to plan again.

## Boundaries

Do not automatically create PRDs, specs, ADRs, issues, decision maps, or subagent workflows.

Do not save plans to a project-specific planning path, publish issue tracker items, or require approval gates unless the user asks for that workflow.
