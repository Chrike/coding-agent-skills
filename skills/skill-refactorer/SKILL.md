---
name: skill-refactorer
description: Manual-only. Use when the user explicitly asks to refactor, migrate, or audit an existing prompt, SKILL.md, or CLAUDE fragment so it fits the current suite without carrying forward stale scaffolding, duplicated default rules, or outdated trigger boundaries. Keep ordinary implementation, review, and planning in their own flows.
disable-model-invocation: true
---

# Skill Refactorer

Preserve durable intent while removing stale prompt scaffolding.

## First Decision

- Use this skill only when the user explicitly asks to maintain or migrate prompt or skill text.
- Do not use it for ordinary code implementation, ordinary refactors, ordinary review, or ordinary planning.
- If the user is designing a new skill, comparing workflow structures, or asking for an implementation plan, use `plan-work` or another actually installed workflow that owns that design work instead.
- If the user is explicitly challenging evidence, source use, or whether the right files were read, use `reliability-check` instead.
- If the user wants review findings or completion verification for code or document changes, use `review-and-finish` instead.

## What To Preserve

Keep only what still carries real value in the current suite:

- live safety boundaries, permission rules, and destructive-action guardrails
- owner preferences that are still genuinely wanted
- routing or maintenance contracts that the current suite still depends on
- domain facts, file paths, schemas, or other concrete project knowledge

## What To Remove Or Compress

Refactoring targets usually include:

- default-layer rules that already live in `prompts/`
- old capability-compensation scaffolding such as rigid step sequences or repeated reminders
- repeated warnings that do not add a new boundary
- frontmatter trigger logic duplicated again in the body
- stale model-specific caveats that no longer reflect the current suite
- output templates or maintenance rituals that are longer than the intent they protect

## Refactor Pass

1. Read the target prompt or skill before changing it.
2. Separate durable intent, active boundaries, and concrete project facts from stale procedure.
3. Check which behaviors already belong to the default layer, another skill, or maintenance tests instead of repeating them here.
4. Rewrite the target into a shorter maintainer-facing form that keeps the intent but drops obsolete scaffolding.
5. Tighten the frontmatter description so it carries the trigger boundary, and keep the body focused on what to do after activation.

## Output Shape

When reporting the refactor, keep it compact:

- what was preserved
- what was removed or compressed
- what structure or boundary changed

If the rewritten file still feels bloated, re-check whether duplicated default rules or stale scaffolding remain.

## Boundaries

- Do not turn this skill into a default critique workflow for every older file in the repo.
- Do not use this skill to perform ordinary implementation work, code review, or broad planning.
- Do not rewrite tests into a second runtime instruction layer.
- Do not reintroduce standing default rules that already belong in `prompts/`.
