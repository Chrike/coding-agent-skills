---
name: memory-handoff
description: Use when the user clearly asks to prepare for context compression, update a handoff or checkpoint, or resume from a checkpoint or named handoff artifact. Keep ordinary task execution out of this flow.
---

# Memory Handoff

Preserve enough state to continue accurately when the user asks for compression, handoff, checkpoint updates, or resume. Requests like “update the handoff before we compress,” “write a checkpoint note,” or “resume from the latest checkpoint” count.

## First Decision

- If the user asks to compress context, update the named handoff file or existing project handoff note with the latest checkpoint before they compress.
- If the user clearly asks to update the latest checkpoint or resume from a checkpoint, use this skill.
- If resuming from a checkpoint after compression, use this skill.
- If the task is ordinary coding and no handoff or resume intent is present, do not use this skill.
- Do not create or update handoff notes just because the conversation is long.
- If existing artifacts already capture a detail, link to them instead of duplicating it.

## Update Memory

When preparing a handoff, write a compact project-local handoff note that includes:

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

Prefer the existing handoff note or user-named handoff or memory file when one exists.

## Resume From Memory

Before acting after a resume:

1. Read the handoff or memory file the user names. If none is named, use the existing handoff note only when there is a single obvious candidate; otherwise state the candidate before relying on it.
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
