# Capability Harness

A self-contained Claude Code plugin for project-scoped, decision-first capability amplification. Before a material generation, implementation, or recommendation, it helps the active controller decide whether missing context, current evidence, project inspection, an alternative, an observable check, or an independent evaluation can materially change the result.

The plugin is a bounded control plane. Existing domain Skills keep implementation and repair ownership, and `agent-workflow` keeps multi-agent coordination ownership when it is already active. Plugin components are namespaced, so they do not replace the repository's standalone Skills or user-level agents.

The `references/` directory contains maintainer-facing protocol documentation migrated from the initial harness. It is linked from the Skill and is not loaded as an additional runtime component. `tests/` contains deterministic maintenance tests, while `skills/capability-harness/evals/` contains calibration cases; neither directory launches agents or hooks during normal use.

## Install

For an installation limited to the current project, run from the repository root:

```powershell
claude plugin marketplace add . --scope local
claude plugin install capability-harness@coding-agent-skills --scope local
```

Keep `--scope local` unless you intentionally want the marketplace and plugin available to every Claude Code project for that user. This repository does not install or modify `C:\Users\wang\.claude`.
After installing in an existing Claude Code session, run `/reload-plugins`; alternatively start a new session.

## Local Validation

From the repository root:

```powershell
claude plugin validate .\plugins\capability-harness --strict
$env:PYTHONDONTWRITEBYTECODE = "1"
python -m unittest discover -s .\plugins\capability-harness\tests -v
```

For an explicitly authorized runtime check, load the source for one session with `claude --plugin-dir .\plugins\capability-harness`, then verify the Skill in `/context`, the five `capability-harness:*` agents in the Custom Agents section, and the two scoped hooks in `/hooks`.

Invoke the Skill explicitly with:

```text
/capability-harness:capability-harness <task>
```

## Runtime Behavior

The project-scoped `UserPromptSubmit` hook classifies only candidate signals and injects a pre-action decision reminder. It never launches agents, creates project state, or blocks a final response. `SubagentStop` validates the output contract of a Harness agent that the active controller has already selected.

For open-ended work, `context-scout` is not an automatic mandatory step. It first identifies the concrete decision that evidence could change. If it cannot name one, it returns a direct-route skip; if it can, it performs bounded direct, component, and adjacent WebSearch/WebFetch work and returns a compact Context Pack. The plugin never requires every worker, every search, or a post-hoc review merely because a request is long, visual, or quality-sensitive.

The command hooks require Python 3.9 or later on `PATH`. This repository validates the plugin schema against Claude Code 2.1.220 and runs deterministic Hook tests with Python 3.14.6 on Windows.

The JSON cases under `skills/capability-harness/evals/` are maintenance calibration data, not automated Hook tests and not the `claude plugin eval` early-access format.

## Manual Calibration

Start a fresh session with the project plugin loaded, then submit the same short prompt without adding hidden design details:

```text
生成一只骑自行车的鹈鹕的 SVG
```

The expected first step is a pre-action decision: identify which omitted signal could improve the construction plan and whether bounded discovery can supply it. A Context Pack, render check, or skeptical evaluation is selected only if it can change a named decision. The user prompt remains unchanged.

For a negative control, use:

```text
生成一个 24x24 SVG 红色圆形图标，固定尺寸和颜色，不需要视觉创新。
```

This fully specified task should remain direct unless the user asks for a concrete check. Compare a small number of paired, real tasks with a plugin-disabled session using the identical original prompt. Record the route, the one signal sought, and whether it materially improved the result; do not treat the calibration cases as a catalogue of all task types.
