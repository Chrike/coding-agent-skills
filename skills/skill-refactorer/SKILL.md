---
name: skill-refactorer
description: Use when the user clearly asks to refactor, migrate, rewrite, or clean up an existing prompt, SKILL.md, or CLAUDE fragment while preserving the intended boundary. Keep ordinary implementation, review, and planning in their own flows.
---

# Skill Refactorer

Preserve durable intent while removing outdated procedure text. Requests like “rewrite this SKILL.md,” “clean up this CLAUDE fragment,” or “tighten this prompt boundary” count.

## First Decision

Once the frontmatter trigger is met, keep this skill limited to that prompt/skill maintenance pass: route new-skill design, workflow comparison, or implementation planning to `plan-work`; evidence, source, or read-set challenges to `reliability-check`; and review findings, feedback handling, or completion verification to `review-and-finish`. Ordinary implementation, code refactors, review, and planning remain in their owning workflows.

## What To Preserve

Keep only what still carries durable value in the target:

- live safety boundaries, permission rules, and destructive-action guardrails
- owner preferences that are still genuinely wanted
- routing boundaries or concrete maintenance facts that the target still depends on
- domain facts, file paths, schemas, or other concrete project knowledge
- operational methods, evidence contracts, exit conditions, or integration rules that the host capability does not guarantee

## What To Remove Or Compress

Refactoring targets usually include:

- standing rules already defined elsewhere in always-on instructions
- outdated step sequences whose decisions are already enforced reliably by the current host or another active workflow
- repeated warnings that do not add a new boundary
- frontmatter trigger logic duplicated again in the body
- outdated caveats tied to constraints that no longer apply
- output templates or maintenance rituals that are longer than the intent they protect

## Refactor Pass

1. Separate durable intent, active boundaries, and concrete project facts from outdated procedure text.
2. Check which behaviors are already covered by standing instructions or another workflow instead of repeating them here.
3. Rewrite the target into a shorter durable form that keeps the intent but drops obsolete procedure text.
4. Tighten the frontmatter description so it carries the trigger boundary, and keep the body focused on what to do after activation.
5. Move optional heuristics or extended maintenance guidance into `references/` when they would otherwise bloat the main skill file.

## Output Shape

When reporting the refactor, keep it compact:

- what was preserved
- what was removed or compressed
- what structure or boundary changed

If the rewritten file still feels bloated, re-check whether duplicated default rules or outdated procedure text remain.

Use [compression-checklist.md](references/compression-checklist.md) for extended cleanup heuristics when needed.

## Boundaries

- Do not turn this skill into a default critique workflow for every older file in the repo.
- Do not use this skill to perform ordinary implementation work, code review, or broad planning.
- Do not turn validation notes into live workflow instructions.
- Do not reintroduce standing rules that already belong in always-on instructions.
