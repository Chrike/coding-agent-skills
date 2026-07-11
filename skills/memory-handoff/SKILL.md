---
name: memory-handoff
description: Use when the user clearly asks to prepare for context compression, update a handoff or checkpoint, or resume from a checkpoint or named handoff artifact. Keep ordinary task execution out of this flow.
---

# Memory Handoff

Preserve enough state to continue accurately when the user asks for compression, handoff, checkpoint updates, or resume. Requests like “update the handoff before we compress,” “write a checkpoint note,” or “resume from the latest checkpoint” count.

## First Decision

- If the user asks to compress context, update the named handoff file or repository-standard handoff note with the latest checkpoint before they compress. When no named or repository-standard artifact exists, return a compact checkpoint in chat unless the user explicitly asks to create or update a persistent file. When multiple plausible handoff artifacts exist and none is named, ask which one is authoritative; do not silently choose, merge, or update one.
- If the user clearly asks to update the latest checkpoint or resume from a checkpoint, use this skill.
- If resuming from a checkpoint after compression, use this skill.
- If the task is ordinary coding and no handoff or resume intent is present, do not use this skill.
- Do not create or update handoff notes just because the conversation is long.
- If existing artifacts already capture a detail, link to them instead of duplicating it.

## Update Memory

When preparing a handoff in an existing or explicitly requested artifact, write a compact handoff note that includes:

1. Current goal in one sentence.
2. Latest user intent, including corrections or changed priorities.
3. Active constraints that still affect execution.
4. Decisions already made.
5. Verified facts or evidence worth carrying forward.
6. Files changed or created, with paths.
7. Active subagents or delegated work, if any.
8. Open blockers or unresolved questions.
9. Last successful checkpoint.
10. Next highest-value action.
11. Explicit do-not-do items that prevent drift.

Prefer the user-named or repository-standard handoff or memory file when one is authoritative. When neither exists, return the checkpoint in chat unless the user explicitly requests persistent storage. When multiple plausible artifacts exist, ask which one is authoritative rather than silently choosing, merging, or updating one.

## Resume From Memory

Before acting after a resume:

1. Read the handoff or memory file the user names. If none is named, use an existing handoff only when there is a single obvious candidate. When multiple plausible candidates exist, ask which artifact is authoritative; do not silently choose, merge, or update one.
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
- Do not make memory updates a default step for ordinary tasks. Use them at compression points, handoffs, long-running work, or when the user asks.
