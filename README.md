Languages: [English](README.md) | [简体中文](README.zh-CN.md)

# Coding Agent Skills

A lightweight skill suite for Claude Code and Codex-assisted development.

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
- Manual workflows stay explicit for higher-cost, side-effecting, durable, or lower-frequency actions.
- `tests/` validates the maintained boundaries and must not become a second runtime instruction layer.
- External analyses, review notes, migration write-ups, and other reference material may inform maintenance decisions, but they do not become active runtime instructions unless the user explicitly designates them as the instruction source.

## Skills

### Automatic Workflow Skills

These can be selected by the agent when the request clearly matches.

| Skill                  | Use when                                                     |
| ---------------------- | ------------------------------------------------------------ |
| `debug-systematically` | Unclear bugs, flaky behavior, regressions, slow paths, repeated failed fixes |
| `test-strategy`        | Tests, TDD, mocks, flaky tests, regression coverage          |
| `review-and-finish`    | Code review, review feedback, done/fixed/passing verification, PR feedback |
| `plan-work`            | Explicit planning, approach comparison, roadmap, task breakdown, vertical slices |
| `design-codebase`      | Architecture, seams, interfaces, adapters, domain language, prototypes |
| `reliability-check`    | Explicit reassessment for hallucination, guessing, stale context, wrong direction, unsupported confidence, source-vs-memory confusion, or example-vs-task confusion |
| `agent-workflow`       | Decompose-first orchestration, independent subproblem fan-out, scout/divergent exploration, per-item batch pipelines, fresh-context verification, high-stakes judged delivery, or cross-model review for high-risk artifacts |

### Manual Workflow Skills

These are explicit command workflows for high-cost, side-effecting, durable, or rarely needed actions. They are useful when intentionally invoked, not as everyday automatic routing.

| Skill                | Use when                                                     |
| -------------------- | ------------------------------------------------------------ |
| `finish-branch`      | Explicit commit, push, merge, PR preparation, discard, branch wrap-up |
| `issue-workflow`     | PRDs, issue drafts, tracker-ready work items, triage         |
| `memory-handoff`     | Context compression, handoff, resume state                   |
| `markdown-memory`    | Durable lessons, repeated mistakes, corrections, confirmed approaches |
| `skill-refactorer`   | Prompt or skill maintenance, migration, stale-scaffolding cleanup |
| `effort-calibrator`  | Explicit effort selection, review, and recalibration for supported `output_config.effort` workloads |
| `decision-map`       | Durable multi-session decision maps                          |

## Installation

Install only the runtime skill folders you want from `skills/`.

In this repository, `skills/` and `prompts/` are source directories rather than host runtime paths.

Known host targets:

- Claude Code runtime skills: project `.claude/skills/` or user `~/.claude/skills/`
- Codex always-on instructions: `AGENTS.md`

Use `prompts/CLAUDE.fragment.md` as the maintained source for the host's always-on instruction file.
For Claude Code, that means assembling it into `CLAUDE.md`-based instructions.

Keep `tests/` as maintenance and validation material rather than runtime skills.
Do not copy `tests/` into `.claude/`, `.agents/`, or other runtime install targets.

## Repository Layout

- `skills/` contains runtime skill source folders for this repository.
- `skills.sh.json` controls skills.sh page grouping only; it does not affect runtime behavior or skill routing.
- `prompts/` contains the maintained default-behavior prompt source for host instruction files.
- `tests/` contains routing and boundary checks used to maintain the suite.
- external reference skills are comparison input only; they are not runtime install targets and should be evaluated before any maintenance or runtime-boundary decision.
- Manual workflow skills include `agents/openai.yaml` to disable implicit Codex invocation.
- If summary text drifts from the maintained prompt file or skill bodies, update the summaries instead of creating a second spec in the README.

## Capability Map

The current runtime surface is organized as follows:

- `prompts/CLAUDE.fragment.md` defines the always-on default behavior layer.
- `debug-systematically`, `test-strategy`, and `review-and-finish` cover core coding execution workflows.
- `plan-work` and `design-codebase` cover explicit planning and architecture decisions.
- `reliability-check` and `memory-handoff` handle corrective reassessment and resume-state continuity.
- `agent-workflow` covers delegated orchestration, scout work, per-item pipelines, and fresh-context verification.
- `finish-branch`, `issue-workflow`, `markdown-memory`, `skill-refactorer`, `effort-calibrator`, and `decision-map` stay explicit because they are side-effecting, durable, maintenance-oriented, or lower-frequency workflows.

## Current Runtime Role Mapping

The current maintained runtime roles land as follows:

- Reporting and summary discipline lives in `prompts/CLAUDE.fragment.md`.
- Execution-flow defaults and act-when-ready behavior live in the maintained prompt file.
- Default scope control and change-discipline rules live in the maintained prompt file.
- Delegated orchestration lives in `skills/agent-workflow/SKILL.md`.
- Durable markdown lessons live in `skills/markdown-memory/SKILL.md`.
- Prompt and skill maintenance cleanup lives in `skills/skill-refactorer/SKILL.md`.
- Effort selection and recalibration live in `skills/effort-calibrator/SKILL.md`.
- External reference material remains comparison input for maintenance decisions; it is not part of the current runtime install surface.

## Recommended Start

Start with the smallest set that matches your actual workflow.

### Core Automatic Set

1. Base always-on behavior assembled from `prompts/CLAUDE.fragment.md` into your host instruction file
2. `debug-systematically`
3. `test-strategy`
4. `review-and-finish`

### Optional Automatic Skills

Add these if you regularly ask for explicit planning, design, reassessment, or orchestration:

- `plan-work`
- `design-codebase`
- `reliability-check`
- `agent-workflow`

### Optional Manual Workflows

Add these only if you want explicit command workflows for heavier actions:

- `finish-branch`
- `issue-workflow`
- `memory-handoff`
- `markdown-memory`
- `skill-refactorer`
- `effort-calibrator`
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
