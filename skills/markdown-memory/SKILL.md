---
name: markdown-memory
description: Use when the user clearly asks to record, update, prune, or consult durable lessons about repeated mistakes, corrections, or confirmed approaches that are not already captured well elsewhere. Keep it separate from handoff state and decision-frontier planning.
---

# Markdown Memory

Maintain durable markdown lessons only when they add future value without turning normal work into note-taking. Requests like “record this lesson,” “remember this repeated mistake,” or “check the lesson memory about X” count.

## First Decision

- Use this skill when the user clearly asks to record, update, prune, or consult lesson memory.
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

1. Confirm that the request is really about durable lessons rather than handoff state or decision tracking.
2. Search for an existing related lesson before writing a new one.
3. Update the existing lesson when possible; otherwise create one compact new lesson file.
4. Remove or correct lessons that have been disproved or superseded.

## Consult Memory

- Consult lesson files only when the user explicitly asks, or when the current task points to a named lesson or memory artifact.
- Read the index first if one exists; open full lesson files only when they are directly relevant.
- Treat lesson memory as a supporting input, not a replacement for the latest user request or current source reads.

## Boundaries

- Do not store secrets, credentials, private data, or unrelated personal information.
- Do not make memory maintenance a default step for ordinary tasks.
- Do not keep conflicting near-duplicate lessons without clearly updating or replacing the old one.
