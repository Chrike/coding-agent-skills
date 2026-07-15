# Lab Experiment Sources

This directory contains versioned source for explicit, non-default experiments. It is not a Claude Code discovery directory and does not activate a workflow by itself.

## `adaptive-long-horizon`

`experiments/workflows/adaptive-long-horizon.js` is a frozen, explicit, read-only pilot for bounded multi-round evidence work. It is not a default skill, automatic router, host sandbox, outcome runner, or lifecycle controller.

To run a reviewed copy, explicitly copy the source to one selected host target:

- project: `<project>/.claude/workflows/`
- user: `~/.claude/workflows/`

Invoke the installed copy as `/adaptive-long-horizon` with structured input containing:

- `task` — the concrete question to investigate;
- `acceptanceCriteria` — the evidence needed for a supported conclusion;
- optional repository-relative `targetPaths` for cited evidence;
- optional `domainMethod` and bounded `limits`.

The pilot remains:

- explicit-only, session-local, and bounded by rounds and agent budget;
- read-only with flat leaf investigations and a separate completion verifier;
- without writes, commits, pushes, external publication, persistent state, automatic routing, or nested delegation.

`targetPaths` is only a lexical cited-evidence boundary, not a host sandbox. The source cannot prove which files the host worker read or technically deny tools. A live pilot must verify the effective host worker configuration before claiming technical enforcement.

The pilot reuses `prompts/CLAUDE.fragment.md`, `skills/agent-workflow/SKILL.md`, `skills/memory-handoff/SKILL.md`, and `skills/decision-map/SKILL.md`; it does not redefine those contracts. This frozen Lab placement is structural organization, not evidence that adaptive improves outcomes or qualifies for lifecycle promotion.

Do not add global deployment, write-enabled execution, concurrent writes, nested controllers, persistent state, automatic task routing, or model-specific benchmark machinery. The repository installer is only an explicit, dry-run-by-default copy tool; do not create a second installer or treat it as host enforcement.
