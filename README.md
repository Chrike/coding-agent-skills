Languages: [English](README.md) | [简体中文](README.zh-CN.md)

# Coding Agent Skills

A lightweight skill suite for Claude Code and Codex-assisted development.

The goal is to keep ordinary coding fast while still giving the agent clear workflows for debugging, testing, planning, review, handoff, reliability correction, and delegated work when those workflows are actually needed.

## What This Repository Contains

This repository contains:

- runtime skill source folders under `skills/`
- source fragments for always-on instructions under `prompts/`
- maintenance and validation material under `tests/`

The suite is designed around a simple rule:

> Start lightweight. Escalate only when the task, risk, or user request justifies it.

It does not try to turn every coding task into a formal process.

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

### Manual Workflow Skills

These are explicit command workflows for high-cost, side-effecting, durable, or rarely needed actions. They are useful when intentionally invoked, not as everyday automatic routing.

| Skill                | Use when                                                     |
| -------------------- | ------------------------------------------------------------ |
| `finish-branch`      | Explicit commit, push, merge, PR preparation, discard, branch wrap-up |
| `agent-workflow`     | Explicit subagents, parallel slices, fresh-context verification, delegated integration |
| `issue-workflow`     | PRDs, issue drafts, tracker-ready work items, triage         |
| `memory-handoff`     | Context compression, handoff, resume state                   |
| `markdown-memory`    | Durable lessons, repeated mistakes, corrections, confirmed approaches |
| `skill-refactorer`   | Prompt or skill maintenance, migration, stale-scaffolding cleanup |
| `effort-calibrator`  | Explicit effort selection, review, and recalibration for Claude or Fable workloads |
| `decision-map`       | Durable multi-session decision maps                          |

## Installation

Install only the runtime skill folders you want from `skills/`.

In this repository, `skills/` and `prompts/` are source directories rather than host runtime paths.

Known host targets:

- Claude Code runtime skills: project `.claude/skills/` or user `~/.claude/skills/`
- Codex always-on instructions: `AGENTS.md`

Use `prompts/` as source material when assembling your host's always-on instruction file. For Claude Code, that means `CLAUDE.md`-based instructions; for Codex, that means `AGENTS.md`.

Keep `tests/` as maintenance and validation material rather than runtime skills.
Do not copy `tests/` into `.claude/`, `.agents/`, or other runtime install targets.

## Repository Layout

- `skills/` contains runtime skill source folders for this repository.
- `skills.sh.json` controls skills.sh page grouping only; it does not affect runtime behavior or skill routing.
- `prompts/` contains source fragments for always-on default behavior in host instruction files.
- `tests/` contains routing and boundary checks used to maintain the suite.
- external reference skills are comparison input only; they are not runtime install targets and should be evaluated before any absorption decision.
- Manual workflow skills include `agents/openai.yaml` to disable implicit Codex invocation.
- If summary text drifts from the prompt fragments or skill bodies, update the summaries instead of creating a second spec in the README.

## Current Absorption Map

The current ten-capability absorption lands as follows:

- `grounded-progress` and `regrounding-summary` land in `prompts/CLAUDE.fragment.md` and `prompts/AGENTS.fragment.md` as reporting and summary discipline.
- `autonomous-continuation` and `act-when-ready` land in the prompt fragments as execution-flow defaults.
- `scope-guard` and `no-gold-plating` land in the prompt fragments as default scope and change-discipline rules.
- `subagent-orchestration` lands in `skills/agent-workflow/SKILL.md`.
- `markdown-memory` lands in `skills/markdown-memory/SKILL.md`.
- `skill-refactorer` lands in `skills/skill-refactorer/SKILL.md`.
- `effort-calibrator` lands in `skills/effort-calibrator/SKILL.md`.
- external reference material remains comparison input for absorption decisions; it is not part of the current runtime install surface.

## Recommended Start

Start with the smallest set that matches your actual workflow.

### Core Automatic Set

1. Base always-on behavior assembled from `prompts/` into your host instruction file
2. `debug-systematically`
3. `test-strategy`
4. `review-and-finish`

### Optional Automatic Skills

Add these if you regularly ask for explicit planning, design, or reassessment:

- `plan-work`
- `design-codebase`
- `reliability-check`

### Optional Manual Workflows

Add these only if you want explicit command workflows for heavier actions:

- `finish-branch`
- `agent-workflow`
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
