---
name: memory-handoff
description: Use when the user clearly asks to prepare for context compression, update a handoff or checkpoint, or resume from a checkpoint or named handoff artifact. Keep ordinary task execution out of this flow.
---

# Memory Handoff

Preserve enough state to continue accurately when the user asks for compression, handoff, checkpoint updates, or resume. Requests like “update the handoff before we compress,” “write a checkpoint note,” or “resume from the latest checkpoint” count.

## First Decision

- If the user clearly asks to compress context, update a handoff or checkpoint, or resume from one, use this skill.
- If the task is ordinary coding and no handoff or resume intent is present, do not use this skill.
- Do not create or update handoff notes just because the conversation is long.
- If existing artifacts already capture a detail, link to them instead of duplicating it.

## Artifact Authority

- Use the user-named or repository-standard handoff artifact when one is authoritative.
- When no authoritative persistent artifact exists, return the checkpoint in chat unless the user explicitly requests persistent storage.
- When multiple plausible handoff artifacts exist and none is named, ask which one is authoritative; do not silently choose, merge, or update one.

## Update Memory

When preparing a handoff in an existing or explicitly requested artifact, write a compact handoff note with:

- current goal and latest user intent
- active constraints and settled decisions
- changed paths and verified evidence
- next highest-value action

Include only when present or material:

- active subagents or delegated work
- blockers or unresolved questions
- last successful checkpoint
- explicit do-not-do items that prevent drift

## Resume From Memory

Before acting after a resume:

1. Follow the Artifact Authority rules to select the handoff or memory file.
2. Read any directly referenced planning or review file needed for the current next step.
3. Restore the latest checkpoint first: current goal, constraints, verified facts, open blockers, ruled-out causes, and next highest-value action.
4. State the current objective briefly, then continue.

Do not restart audits, re-argue settled decisions, or act on an older plan if the handoff or memory file records a correction.
Do not repopulate the active conversation with narrative session history when the checkpoint already captures the operational state.

## Handoff Shape

Keep handoffs short and operational:

- what the project is trying to accomplish
- what has already been decided
- what was changed
- what remains unclear
- what to do next
- what not to do

Use bullet lists when they make state easier to scan. Avoid narrative session history.

## Boundaries

- Do not store secrets, credentials, private data, or unrelated user information.
- Do not copy large source content into handoff notes. Reference paths instead.
- Do not make memory updates a default step for ordinary tasks. Use them at explicit compression, handoff, checkpoint, or resume moments during long-running work, or when the user asks.
