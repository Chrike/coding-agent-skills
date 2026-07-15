---
name: markdown-memory
description: Use when the user clearly asks to record, update, prune, or consult project-governed markdown lessons about repeated mistakes, corrections, or confirmed approaches that must be versioned, shared, reviewable, or otherwise tied to repository history. Keep it separate from host auto memory, handoff state, and decision-frontier planning.
---

# Markdown Memory

Maintain project-governed markdown lessons only when they add future value. Use host auto memory for personal or host-local learnings; it must not by itself trigger a project lesson or become an instruction source. Requests like “record this repository lesson,” “preserve this repeated mistake for review,” or “check the project lesson memory about X” count.

## First Decision

- Use this skill when the user clearly asks to record, update, prune, or consult a project-governed lesson that must be versioned, shared, reviewable, or otherwise tied to repository history.
- Do not create a project lesson merely because the user asks Claude Code to remember a personal preference or host-local learning; use host auto memory for that purpose.
- If the user is preparing for context compression, handing off current task state, or resuming from a handoff, use `memory-handoff` instead.
- If the user is mapping open questions, ticket dependencies, or a decision frontier, use `decision-map` instead.
- If the repo, docs, code comments, or an existing lesson already capture the point clearly, do not create a new lesson.

## What Belongs In Memory

Record only lessons that remain useful across sessions:

- repeated mistakes and their corrections
- confirmed approaches worth reusing under similar conditions
- non-obvious pitfalls that are easy to repeat and are not already written down elsewhere
- updates that narrow, replace, or invalidate an existing lesson
- time- or version-sensitive lessons only when you can anchor them with concrete dates, versions, or exact identifiers

## What Does Not Belong

Do not use this skill for:

- current-task objective, status, changed files, next step, or do-not-do items; those belong in `memory-handoff`
- open design questions, unresolved options, ticket frontiers, or dependency maps; those belong in `decision-map`
- facts already captured clearly in repo docs, code, or stable project instructions
- large source excerpts, turn-by-turn history, or broad meeting notes

## File Shape

Keep the storage simple and markdown-based:

- prefer `memory/lessons/` when the project already uses a project-local memory area
- store one lesson per file
- start each file with a one-sentence summary that makes sense on its own
- make the body answer: what happened, what the correct approach is, and why it matters later
- update an existing lesson instead of creating a near-duplicate

If the project already maintains an index such as `memory/INDEX.md`, update it when lessons change.
Do not create or regenerate an index unless the user asks or the repo already uses one.

## Workflow

1. Search for an existing related lesson before writing a new one.
2. Update the existing lesson when possible; otherwise create one compact new lesson file.
3. Remove or correct lessons that have been disproved or superseded.

## Consult Memory

- Consult lesson files only when the user explicitly asks, or when the current task points to a named lesson or memory artifact.
- Read the index first if one exists; open full lesson files only when they are directly relevant.

## Boundaries

- Do not store secrets, credentials, private data, or unrelated personal information.
- Do not keep conflicting near-duplicate lessons without clearly updating or replacing the old one.
