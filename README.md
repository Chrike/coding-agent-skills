Languages: [English](README.md) | [简体中文](README.zh-CN.md)

# Coding Agent Skills

A lightweight skill suite for Claude Code-assisted development.

The goal is to keep ordinary coding fast while still giving the agent clear workflows for debugging, testing, planning, review, handoff, reliability correction, and delegated work when those workflows are actually needed.

## What This Repository Contains

This repository contains:

- runtime skill source folders under `skills/`
- optional Claude Code leaf-agent profile source under `agents/`
- the maintained always-on instruction prompt under `prompts/`
- explicit opt-in saved-workflow source under `workflows/`
- maintenance and validation material under `tests/`

The suite is designed around a simple rule:

> Start lightweight. Escalate only when the task, risk, or user request justifies it.

It does not try to turn every coding task into a formal process.

## Capability Boundaries

This suite separates runtime responsibilities by role, not by where an idea originally came from.

- `prompts/` holds the always-on default behavior layer for ordinary development work.
- `skills/` holds named workflow boundaries that should load only when the request clearly needs them.
- `agents/` holds optional leaf execution-role source. Installed agents accept bounded assignments; they do not define top-level routing, replace an active domain method, or own integration.
- `workflows/` holds explicit opt-in saved-workflow source; it is not a host discovery directory and does not participate in ordinary skill routing.
- Explicit-intent workflows should route from clear natural-language intent rather than requiring users to remember skill names.
- High-risk side effects, durable artifacts, and destructive actions should be guarded inside the owning skill instead of forcing a second runtime router layer.
- `tests/` validates the maintained boundaries and must not become a second runtime instruction layer.
- External analyses, review notes, migration write-ups, and other reference material may inform maintenance decisions, but they do not become active runtime instructions unless the user explicitly designates them as the instruction source.
- The bundled `/code-review` command remains host-owned; it should not re-enter the project review skill as a second review path.
- The maintained prompt is model guidance, not deterministic enforcement. Use host permissions or `PreToolUse` hooks when an action must be reliably blocked or confirmed.

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
| `agent-workflow`       | Coordinated multi-agent decomposition, evidence, verification, and integration for independent slices |

### Explicit-Intent Workflow Skills

These skills are for requests that are not ordinary coding flow, but still should route from clear natural-language intent instead of requiring the user to manually invoke a skill by name.

| Skill                | Use when                                                     |
| -------------------- | ------------------------------------------------------------ |
| `finish-branch`      | Explicit commit, branch push, current-branch PR preparation or creation, local branch or named remote PR merge, scoped Git working-tree discard, named branch deletion, named worktree removal, or branch wrap-up choice |
| `issue-workflow`     | PRDs, issue drafts, tracker-ready work items, tracker publication/update, triage |
| `memory-handoff`     | Context compression, handoff, checkpoint updates, resume state |
| `markdown-memory`    | Explicit project-versioned, shared, or reviewable Markdown reference lessons; not automatically loaded `CLAUDE.md` or `.claude/rules/` instructions |
| `skill-refactorer`   | Coding-agent prompt or skill maintenance, migration, stale-scaffolding cleanup |
| `decision-map`       | Durable multi-session decision maps                          |

## Optional Agent Profiles

These Claude Code custom agents are optional execution roles, not skills or an automatic pipeline.

| Agent | Use when assigned one bounded scope |
| --- | --- |
| `harness-evidence-researcher` | Gather repository or authorized current primary-source evidence for one material uncertainty. |
| `harness-independent-brancher` | Produce one materially independent alternative without anchoring on a preferred candidate. |
| `harness-execution-verifier` | Run one authorized, bounded observable check against an identified artifact or environment. |
| `harness-skeptical-evaluator` | Evaluate actual candidates or results against supplied constraints and evidence. |

One focused role can be delegated directly under the active domain method. Multiple independent roles that need coordinated integration must first pass the `agent-workflow` fit check. Installing all four does not make all four mandatory.

## Installation

Install only the runtime skill folders and optional agent profiles you need.

In this repository, `skills/`, `agents/`, `prompts/`, and `workflows/` are source directories rather than host runtime paths.

Known host targets:

- Claude Code runtime skills: project `.claude/skills/` or user `~/.claude/skills/`
- Claude Code custom agents: project `.claude/agents/` or user `~/.claude/agents/`
- Claude Code saved workflows: project `.claude/workflows/` or user `~/.claude/workflows/`

Copy only reviewed agent Markdown files from `agents/` to one selected agent target and preserve their namespaced filenames. Follow the current runtime discovery check in [agents/README.md](agents/README.md); do not treat `/agents` as a discovery list on Claude Code 2.1.198 or later. Installing these profiles does not install a `capability-harness` skill or enable hooks.

Saved workflows are opt-in: copy a reviewed source file to one explicitly chosen target and invoke its installed name. They do not replace skill routing or activate from ordinary long or multi-file work.

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
- `agents/` contains optional Claude Code leaf-agent profile source; it is distinct from the host runtime path `.claude/agents/` and from `.agents/`.
- `skills.sh.json` controls skills.sh page grouping only; it does not affect runtime behavior or skill routing.
- `prompts/` contains the maintained default-behavior prompt source for host instruction files.
- `workflows/` contains explicit saved-workflow source; copy a reviewed file to `.claude/workflows/` or `~/.claude/workflows/` before invoking it.
- `tests/` contains routing and boundary checks used to maintain the suite.
- external reference skills are comparison input only; they are not runtime install targets and should be evaluated before any maintenance or runtime-boundary decision.
- Runtime prompt maintenance should keep one closely related decision family per rule where practical, preserve a matching positive or negative regression case for new behavior, keep explanatory text out of the runtime layer, avoid duplicating procedures already owned by a Skill, and record whether removed text was merged, moved to an owning Skill or maintenance document, or found to have no independent behavior value. These are maintenance checks, not runtime instructions.
- If summary text drifts from the maintained prompt file or skill bodies, update the summaries instead of creating a second spec in the README.

## Capability Map

The current runtime surface is organized as follows:

- `prompts/CLAUDE.fragment.md` defines the always-on default behavior layer.
- `debug-systematically`, `test-strategy`, and `review-and-finish` cover core coding execution workflows.
- `agent-workflow` covers multi-agent orchestration method when independent slices need coordinated execution.
- `agents/` supplies optional namespaced leaf roles for evidence, independent alternatives, observable verification, and skeptical evaluation; the current controller and domain method retain ownership.
- `workflows/` contains explicit saved-workflow source for bounded, session-local programmatic execution pilots; it is not ordinary skill routing.
- `plan-work` and `design-codebase` cover explicit planning and architecture decisions, plus implementation requests with unresolved load-bearing planning or design decisions.
- `reliability-check` and `memory-handoff` handle corrective reassessment and resume-state continuity.
- `finish-branch`, `issue-workflow`, `markdown-memory`, `skill-refactorer`, and `decision-map` cover explicit-intent requests for branch actions, durable artifacts, and maintenance work.

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

### Optional Agent Profiles

Install reviewed profiles from `agents/` only when reusable bounded leaf roles improve your workflow. Start with the smallest useful subset; agent availability alone is not a reason to delegate or fan out.

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
