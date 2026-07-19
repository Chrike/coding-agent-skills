# Memory Handoff Contracts

These checks maintain the explicit handoff skill boundary. They are not runtime instructions and do not replace `skills/memory-handoff/SKILL.md`.

## Positive cases

- Update the handoff before pausing, compressing, or checkpointing → `memory-handoff`.
- Update the checkpoint before compression while preserving material hypothesis, failed attempts, ruled-out causes, and the next highest-value action → `memory-handoff`.
- Resume from the latest checkpoint in the current handoff note → `memory-handoff`.

## Ownership boundary

The handoff skill owns cross-session state and recovery content. Adaptive Workflow variables remain session-local and do not provide cross-session resume. Ordinary long output, task duration, file count, and agent count alone do not trigger this skill.
