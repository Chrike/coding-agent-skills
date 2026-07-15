---
name: memory-handoff
description: Use when the user clearly asks to prepare for context compression, update a handoff or checkpoint, or resume from a checkpoint or named handoff artifact. Keep ordinary task execution out of this flow.
---

# Memory Handoff

Preserve enough state to continue accurately when the user asks for compression, handoff, checkpoint updates, or resume. Requests like “update the handoff before we compress,” “write a checkpoint note,” or “resume from the latest checkpoint” count.

## First Decision

- Activate only for an explicit compression, handoff, checkpoint, or resume request.
- Do not create or update handoff state for ordinary work or context length alone.
- If existing artifacts already capture a detail, link to them instead of duplicating it.

## Artifact Authority

- Use the user-named or repository-standard handoff artifact when one is authoritative.
- When no authoritative persistent artifact exists, return the checkpoint in chat unless the user explicitly requests persistent storage.
- When multiple plausible handoff artifacts exist and none is named, ask which one is authoritative; do not silently choose, merge, or update one.

## Update Memory

When preparing a handoff or checkpoint, write a compact, operational note with:

- current goal and latest user intent
- active constraints and settled decisions
- changed paths and verified evidence
- next highest-value action

Include only when present or material:

- active subagents or delegated work
- blockers or unresolved questions
- last successful checkpoint
- explicit do-not-do items that prevent drift
- current working hypotheses, material failed attempts, and ruled-out causes or alternatives when they constrain the next step

Use bullets when they make the state easier to scan. Avoid narrative session history.

## Resume From Memory

Before acting after a resume:

1. Follow the Artifact Authority rules to select the handoff or memory file.
2. Read any directly referenced planning or review file needed for the current next step.
3. Restore the latest checkpoint first: current goal, constraints, verified facts, any current working hypotheses that remain material, open blockers, material failed attempts, ruled-out causes or alternatives, and the next highest-value action.
4. State the current objective briefly, then continue.

Do not restart audits, re-argue settled decisions, or act on an older plan if the handoff or memory file records a correction.
Do not repopulate the active conversation with narrative session history when the checkpoint already captures the operational state.

## Boundaries

- Do not store secrets, credentials, private data, or unrelated user information.
- Do not copy large source content into handoff notes. Reference paths instead.
