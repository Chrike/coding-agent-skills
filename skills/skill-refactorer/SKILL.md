---
name: skill-refactorer
description: Manual-only. Use when the user explicitly asks to refactor, migrate, or clean up an existing prompt, SKILL.md, or CLAUDE fragment to remove outdated procedure text, duplicated standing rules, or outdated trigger boundaries while preserving durable intent. Keep ordinary implementation, review, and planning in their own flows.
disable-model-invocation: true
---

# Skill Refactorer

Preserve durable intent while removing outdated procedure text.

## First Decision

- Use this skill only when the user explicitly asks to maintain or migrate prompt or skill text.
- Do not use it for ordinary code implementation, ordinary refactors, ordinary review, or ordinary planning.
- If the user is designing a new skill, comparing workflow structures, or asking for an implementation plan, use `plan-work` or another actually installed workflow that owns that design work instead.
- If the user is explicitly challenging evidence, source use, or whether the right files were read, use `reliability-check` instead.
- If the user wants review findings or completion verification for code or document changes, use `review-and-finish` instead.

## What To Preserve

Keep only what still carries durable value in the target:

- live safety boundaries, permission rules, and destructive-action guardrails
- owner preferences that are still genuinely wanted
- routing boundaries or concrete maintenance facts that the target still depends on
- domain facts, file paths, schemas, or other concrete project knowledge

## What To Remove Or Compress

Refactoring targets usually include:

- standing rules already defined elsewhere in always-on instructions
- outdated procedure text such as rigid step sequences or repeated reminders
- repeated warnings that do not add a new boundary
- frontmatter trigger logic duplicated again in the body
- outdated caveats tied to constraints that no longer apply
- output templates or maintenance rituals that are longer than the intent they protect

## Refactor Pass

1. Separate durable intent, active boundaries, and concrete project facts from outdated procedure text.
2. Check which behaviors are already covered by standing instructions or another workflow instead of repeating them here.
3. Rewrite the target into a shorter durable form that keeps the intent but drops obsolete procedure text.
4. Tighten the frontmatter description so it carries the trigger boundary, and keep the body focused on what to do after activation.

## Output Shape

When reporting the refactor, keep it compact:

- what was preserved
- what was removed or compressed
- what structure or boundary changed

If the rewritten file still feels bloated, re-check whether duplicated default rules or outdated procedure text remain.

## Boundaries

- Do not turn this skill into a default critique workflow for every older file in the repo.
- Do not use this skill to perform ordinary implementation work, code review, or broad planning.
- Do not turn validation notes into live workflow instructions.
- Do not reintroduce standing rules that already belong in always-on instructions.
