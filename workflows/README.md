# Workflow Sources

This directory contains versioned Claude Code saved-workflow source for this repository. It is not a Claude Code discovery directory and does not activate a workflow by itself.

To run a reviewed workflow, use Claude Code 2.1.154 or later with dynamic workflows enabled, then copy its source to one explicitly chosen runtime target:

- project: `<project>/.claude/workflows/`
- user: `~/.claude/workflows/`

Project workflows override same-named user workflows. In nested projects, the closest same-named workflow takes precedence. Keep the source revision and installed copy identifiable before treating a runtime result as evidence for this repository.

## `adaptive-long-horizon`

`adaptive-long-horizon.js` is an explicit, read-only pilot for bounded multi-round evidence work. It is for a task that needs a session-local orientation, evidence questions, and controlled follow-up, not for ordinary long or multi-file work.

Invoke the installed copy as `/adaptive-long-horizon` with structured input containing:

- `task` — the concrete question to investigate
- `acceptanceCriteria` — the evidence needed for a supported conclusion
- optional `targetPaths` — repository-relative paths that bound cited evidence lexically
- optional `domainMethod` — a compact active debugging, design, testing, review, or research method capsule
- optional `limits` — tighter `maxRounds` or `maxAgents` within the pilot caps; `maxAgents` counts investigator and completion-verifier calls and must be at least 2

Investigators return **candidate evidence**. Candidate evidence is provisional, session-local evidence with controller-assigned IDs and investigator provenance. A separate fresh-context verifier returns **verified evidence** only by referencing candidate IDs whose path, version, and location still match. Blocked results expose candidate evidence as candidate evidence; they do not imply that it was verified.

The workflow retains only material session-local carry-forward state: the active hypothesis, failed or ruled-out paths, unresolved contradictions (which must be explicitly cleared), completed scopes, and candidate-supported criteria. It does not create durable reasoning history or cross-session recovery state.

The workflow is deliberately limited to:

- session-local script state; it is not cross-session recovery or durable memory
- read-only flat leaf investigations and a flat leaf completion verifier
- no nested delegation, writes, commits, pushes, external publication, or automatic routing
- one evidence question per round, with a hard total investigator/verifier budget and a blocker after repeated inspectable non-progress
- a separate fresh-context verifier before any completion result is returned

`targetPaths` is a cited-evidence boundary, not a host-level file-read sandbox. The controller normalizes returned paths as repository-relative lexical paths and blocks citations outside the supplied targets; it cannot prove which files the host worker actually read. Evidence versions must be repository-visible exact identifiers when available, or `current unversioned working tree` with an exact `symbol: ...`, `section: ...`, or `lines:N-M` location. Candidate evidence with unsupported version or location formats is blocked.

The script cannot read files, run commands, or verify results directly; its leaf agents return structured evidence for integration. This pilot permits only repository-file reads and excludes build, test, install, formatter, generator, migration, and shell commands because those may write caches or other state. These are pilot operating constraints, not proof that the installed host has technically denied worker write or delegation tools. A live pilot must verify the effective worker tool configuration before claiming technical enforcement. It reuses the maintained default and orchestration contracts instead of redefining them:

- [`prompts/CLAUDE.fragment.md`](../prompts/CLAUDE.fragment.md) for lightweight defaults and sole execution ownership
- [`skills/agent-workflow/SKILL.md`](../skills/agent-workflow/SKILL.md) for worker briefs, integration, and leaf boundaries
- [`skills/memory-handoff/SKILL.md`](../skills/memory-handoff/SKILL.md) for explicit cross-session checkpoint or resume state
- [`skills/decision-map/SKILL.md`](../skills/decision-map/SKILL.md) for explicit durable decision frontiers

## Pilot boundary

This source is not a general workflow platform. Do not add an installer, global deployment, write-enabled execution, concurrent writes, nested controllers, persistent state, automatic task routing, or model-specific benchmark machinery until a live Claude Code pilot demonstrates a measurable benefit over the existing `agent-workflow` method.
