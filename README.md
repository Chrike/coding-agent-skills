# Coding Agent Skills

A small Claude Code instruction suite for lightweight development, explicit multi-agent coordination, reliability reassessment, task handoff, project reference lessons, and maintenance of coding-agent instructions.

## Scope

This repository maintains:

- `prompts/CLAUDE.fragment.md`: the always-on default behavior source, including distinct action-authorization, command-effect, Git, persistence, and evidence boundaries.
- Five on-demand skills: `agent-workflow`, `reliability-check`, `memory-handoff`, `markdown-memory`, and `skill-refactorer`.
- Optional self-contained Claude Code plugins under `plugins/`.
- Explicitly selected saved-workflow source under `workflows/`.
- Maintenance contracts and local validators under `tests/`.

The suite deliberately no longer ships dedicated workflows for general debugging, test strategy, architecture and planning, UI engineering, live browser testing, performance experiments, CI/CD design, operational observability, security threat modeling, production-release readiness, branch finishing, issue/spec authoring, ideation, interviews, or durable decision maps. The retained prompt preserves selected safety and evidence distinctions; it does not replace those removed procedures. Use the host's or project's ordinary method for such work, and do not infer that a similar retained skill provides equivalent coverage.

## Runtime Boundaries

- `prompts/` is the maintained source for default instructions; it is model guidance, not deterministic enforcement. Use host permissions or applicable hooks when an action must be reliably blocked or confirmed.
- `skills/` contains source folders. Their presence here does not by itself prove that Claude Code has installed, discovered, or loaded them.
- `plugins/` contains optional self-contained packages. Install a plugin as a complete unit; its skills, agents, or hooks do not replace the standalone skill surface.
- `workflows/` contains versioned saved-workflow source, not a host discovery directory. Copy a reviewed workflow to one explicitly selected runtime target before invoking it; it does not activate from long or multi-file tasks.
- `tests/` is maintenance material, not a second runtime instruction layer. Markdown cases and static checks do not prove live model routing, plugin loading, hook enforcement, or runtime tool isolation.
- External analyses, review notes, and examples are evidence, not active instructions, unless the user explicitly designates them as the instruction source.
- The bundled `/code-review` and `/security-review` commands remain host-owned; the latter is for current-diff vulnerability review, not a replacement for a dedicated threat-modeling workflow.

## Skills

### Automatic selection when clearly applicable

| Skill | Use when |
| --- | --- |
| `agent-workflow` | The user asks for coordination, or multiple genuinely independent slices, stages, or verifier questions need an integration owner. It performs a fit check first and may decide to stay solo. |
| `reliability-check` | The user explicitly challenges a conclusion, evidence, source use, active stage, stale context, or workflow/strategy drift. It is not a default preflight. |

### Explicit-intent skills

| Skill | Use when |
| --- | --- |
| `memory-handoff` | The user explicitly requests a task checkpoint, handoff, or resume from a named or repository-standard artifact. |
| `markdown-memory` | The user explicitly requests a versioned, shared, reviewable project reference lesson. It is not for host auto-memory or task-state handoffs. |
| `skill-refactorer` | The user explicitly requests maintenance or migration of an existing coding-agent instruction artifact. |

## Installation

Install only the skill folders you want from `skills/`. In Claude Code, runtime skill targets include project `.claude/skills/` and user `~/.claude/skills/`; follow the current host documentation for installation and discovery behavior.

Use `prompts/CLAUDE.fragment.md` as the maintained source when assembling the host's always-on instruction file. For Claude Code, assemble it into the applicable `CLAUDE.md` instruction scope.

Optional plugins are installed as complete units. The marketplace manifest currently lists `capability-harness`. See [plugins/capability-harness/README.md](plugins/capability-harness/README.md) for its scope.

To use a saved workflow, review its source and copy it to one explicitly chosen target, such as project `.claude/workflows/` or user `~/.claude/workflows/`, then invoke the installed name. Keep source and installed revisions identifiable when reporting runtime evidence.

Do not copy `tests/` into runtime install targets.

## Repository Maintenance

- Keep each always-on rule focused on one closely related decision family; do not merge independent triggers, owners, failure modes, or evidence levels for the sake of a fixed rule count.
- New or materially changed behavior should have a corresponding positive or negative maintenance case. These Markdown cases are review aids, not executable routing evaluations.
- Keep detailed procedures out of the default layer when they are not part of the retained suite; document removed capabilities honestly instead of claiming equivalence.
- When a skill is removed, update its owners and references, README summaries, catalog entries, and relevant maintenance contracts. A string mention is not proof that a consumer or behavior is fully migrated.
- If a summary drifts from the maintained prompt or skill body, update the summary rather than creating a second specification in the README.

## Recommended Start

Start with the base prompt. Add only the retained skill that matches an explicit need:

- `agent-workflow` for worthwhile coordinated execution.
- `reliability-check` for an explicit reliability challenge.
- `memory-handoff` for an explicit task-state handoff or resume.
- `markdown-memory` for an explicit project reference lesson.
- `skill-refactorer` for an explicit instruction-artifact maintenance request.

For removed domain workflows, use the host's or project's existing method; this repository makes no claim that its retained skills replace them.
