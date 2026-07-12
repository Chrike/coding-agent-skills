Languages: [English](README.md) | [简体中文](README.zh-CN.md)

# Coding Agent Skills

A lightweight skill suite for Claude Code-assisted development.

The goal is to keep ordinary coding fast while still giving the agent clear workflows for debugging, testing, planning, review, handoff, reliability correction, and delegated work when those workflows are actually needed.

## What This Repository Contains

This repository contains:

- runtime skill source folders under `skills/`
- the maintained always-on instruction prompt under `prompts/`
- maintenance and validation material under `tests/`

The suite is designed around a simple rule:

> Start lightweight. Escalate only when the task, risk, or user request justifies it.

It does not try to turn every coding task into a formal process.

## Capability Boundaries

This suite separates runtime responsibilities by role, not by where an idea originally came from.

- `prompts/` holds the always-on default behavior layer for ordinary development work.
- `skills/` holds named workflow boundaries that should load only when the request clearly needs them.
- Explicit-intent workflows should route from clear natural-language intent rather than requiring users to remember skill names.
- High-risk side effects, durable artifacts, and destructive actions should be guarded inside the owning skill instead of forcing a second runtime router layer.
- `tests/` validates the maintained boundaries and must not become a second runtime instruction layer.
- External analyses, review notes, migration write-ups, and other reference material may inform maintenance decisions, but they do not become active runtime instructions unless the user explicitly designates them as the instruction source.

## Skills

### Automatic Workflow Skills

These can be selected by the agent when the request clearly matches.

| Skill                  | Use when                                                     |
| ---------------------- | ------------------------------------------------------------ |
| `debug-systematically` | Unclear bugs, flaky behavior, regressions, slow paths, repeated failed fixes |
| `test-strategy`        | Test design, TDD, mocks, flaky tests, regression coverage, or a non-obvious test seam/level/acceptance signal |
| `review-and-finish`    | Code review, review feedback, done/fixed/passing verification, PR feedback, or focused readiness evidence for a behaviorally high-risk completed change |
| `plan-work`            | Planning, approach comparison, roadmap, task breakdown, vertical slices, or an implementation with approach/dependency/sequencing/migration/compatibility/scope decisions that cannot be safely inferred |
| `design-codebase`      | Architecture, seams, interfaces, adapters, domain language, prototypes, or an implementation blocked on a non-obvious architecture/ownership/interface/dependency-boundary decision |
| `reliability-check`    | Explicit reassessment for hallucination, guessing, stale context, wrong direction, unsupported confidence, source-vs-memory confusion, or example-vs-task confusion |
| `agent-workflow`       | Multi-agent decomposition, ownership, evidence, verification, and integration method |

### Explicit-Intent Workflow Skills

These skills are for requests that are not ordinary coding flow, but still should route from clear natural-language intent instead of requiring the user to manually invoke a skill by name.

| Skill                | Use when                                                     |
| -------------------- | ------------------------------------------------------------ |
| `finish-branch`      | Explicit commit, push, merge, PR preparation, discard, branch wrap-up |
| `issue-workflow`     | PRDs, issue drafts, tracker-ready work items, triage         |
| `memory-handoff`     | Context compression, handoff, checkpoint updates, resume state |
| `markdown-memory`    | Explicit project-versioned, shared, or reviewable Markdown lessons |
| `skill-refactorer`   | Prompt or skill maintenance, migration, stale-scaffolding cleanup |
| `decision-map`       | Durable multi-session decision maps                          |

## Installation

Install only the runtime skill folders you want from `skills/`.

In this repository, `skills/` and `prompts/` are source directories rather than host runtime paths.

Known host target:

- Claude Code runtime skills: project `.claude/skills/` or user `~/.claude/skills/`

Use `prompts/CLAUDE.fragment.md` as the maintained source for the host's always-on instruction file.
For Claude Code, that means assembling it into `CLAUDE.md`-based instructions.

Keep `tests/` as maintenance and validation material rather than runtime skills.
Do not copy `tests/` into `.claude/`, `.agents/`, or other runtime install targets.

### Recommended Host Skill Visibility

When this full skill suite is installed and a host multi-agent workflow is the primary execution substrate, prefer host-local Claude Code settings that keep overlapping bundled skills user-invocable only:

```json
{
  "skillOverrides": {
    "batch": "user-invocable-only",
    "code-review": "user-invocable-only",
    "simplify": "user-invocable-only",
    "loop": "user-invocable-only"
  }
}
```

`user-invocable-only` hides those skills from automatic selection while still leaving them available from the `/` menu. Keep `/debug` at its host default so Claude Code runtime issues stay with the bundled debug flow, while project product debugging stays in `debug-systematically`.

This is a recommended host configuration for the full suite, not a repository-enforced setting for every install.

## Repository Layout

- `skills/` contains runtime skill source folders for this repository.
- `skills.sh.json` controls skills.sh page grouping only; it does not affect runtime behavior or skill routing.
- `prompts/` contains the maintained default-behavior prompt source for host instruction files.
- `tests/` contains routing and boundary checks used to maintain the suite.
- external reference skills are comparison input only; they are not runtime install targets and should be evaluated before any maintenance or runtime-boundary decision.
- If summary text drifts from the maintained prompt file or skill bodies, update the summaries instead of creating a second spec in the README.

## Capability Map

The current runtime surface is organized as follows:

- `prompts/CLAUDE.fragment.md` defines the always-on default behavior layer.
- `debug-systematically`, `test-strategy`, and `review-and-finish` cover core coding execution workflows.
- `agent-workflow` covers multi-agent orchestration method when independent slices need coordinated execution.
- `plan-work` and `design-codebase` cover explicit planning and architecture decisions, plus implementation requests with unresolved load-bearing planning or design decisions.
- `reliability-check` and `memory-handoff` handle corrective reassessment and resume-state continuity.
- `finish-branch`, `issue-workflow`, `markdown-memory`, `skill-refactorer`, and `decision-map` cover explicit-intent requests for branch actions, durable artifacts, and maintenance work.

## Current Runtime Role Mapping

The current maintained runtime roles land as follows:

- Reporting and summary discipline lives in `prompts/CLAUDE.fragment.md`.
- Execution-flow defaults and act-when-ready behavior live in the maintained prompt file.
- Default scope control and change-discipline rules live in the maintained prompt file.
- Explicit project-versioned, shared, or reviewable markdown lessons live in `skills/markdown-memory/SKILL.md`; host auto memory remains host-managed context for personal or local learnings.
- Prompt and skill maintenance cleanup lives in `skills/skill-refactorer/SKILL.md`.
- External reference material remains comparison input for maintenance decisions; it is not part of the current runtime install surface.

## Recommended Start

Start with the smallest set that matches your actual workflow.

### Core Automatic Set

1. Base always-on behavior assembled from `prompts/CLAUDE.fragment.md` into your host instruction file
2. `debug-systematically`
3. `test-strategy`
4. `review-and-finish`

### Optional Automatic Skills

Add these if you regularly ask for explicit planning, design, reassessment, or multi-agent orchestration:

- `plan-work`
- `design-codebase`
- `reliability-check`
- `agent-workflow`

### Optional Explicit-Intent Workflows

Add these if you want natural-language routing for branch actions, durable artifacts, maintenance, or calibration work without requiring users to remember skill names:

- `finish-branch`
- `issue-workflow`
- `memory-handoff`
- `markdown-memory`
- `skill-refactorer`
- `decision-map`

## Customization

Keep changes small.

Good changes:

- tighten a trigger
- remove workflows you do not use
- clarify when to stop
- add a reference for a repeated real failure
- turn repeated failures into durable behavior rules only when they belong in the always-on layer; keep concrete regression cases in `tests/`

Avoid changes that make every task slower.
