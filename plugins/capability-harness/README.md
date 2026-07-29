# Capability Harness

A self-contained Claude Code plugin for project-scoped task routing, context enrichment, bounded evidence gathering, independent alternatives, observable verification, and skeptical evaluation.

The plugin is a bounded control plane. Existing domain Skills keep implementation and repair ownership, and `agent-workflow` keeps multi-agent coordination ownership when it is already active. Plugin components are namespaced, so they do not replace the repository's standalone Skills or user-level agents.

The `references/` directory contains maintainer-facing protocol documentation migrated from the initial harness. It is linked from the Skill and is not loaded as an additional runtime component. `tests/` contains deterministic maintenance tests, while `skills/capability-harness/evals/` contains evaluation cases; neither directory launches agents or hooks during normal use.

## Install

For an installation limited to the current project, run from the repository root:

```powershell
claude plugin marketplace add . --scope local
claude plugin install capability-harness@coding-agent-skills --scope local
```

Keep `--scope local` unless you intentionally want the marketplace and plugin available to every Claude Code project for that user. This repository does not install or modify `C:\Users\wang\.claude`.
After installing in an existing Claude Code session, run `/reload-plugins`; alternatively start a new session.

## Local validation

From the repository root:

```powershell
claude plugin validate .\plugins\capability-harness --strict
$env:PYTHONDONTWRITEBYTECODE = "1"
python -m unittest discover -s .\plugins\capability-harness\tests -v
```

For an explicitly authorized runtime check, load the source for one session with `claude --plugin-dir .\plugins\capability-harness`, then verify the Skill in `/context`, the five `capability-harness:*` agents in the Custom Agents section, and the scoped hook in `/hooks`.

Invoke the Skill explicitly with:

```text
/capability-harness:capability-harness <task>
```

The project-scoped `UserPromptSubmit` hook classifies the prompt and injects routing context; it never launches agents by itself. Open-ended visual, design, architecture, recommendation, and generated-artifact tasks are routed to a bounded `context-scout` Context Pack before generation when implicit details may materially affect quality. The scout uses direct, component, and adjacent WebSearch/WebFetch questions; it does not copy a reference artifact. The `Stop` hook performs at most one completion challenge for substantive turns, and `SubagentStop` validates recognized leaf-agent contracts. Explicit user instructions and an existing controller remain authoritative.

Runtime state is written only under the active project's `.claude/capability-harness/state/` directory. It records classification, required checks, bounded stop results, and any reported `Route`/`Harness`/`Reason` fields. Add that directory to the project's ignore rules when using the plugin; the repository ignores it by default.

The migrated installation reference is project-scoped by design. The initial bundle's global installer and any deployment into `C:\Users\wang\.claude` are intentionally excluded from this plugin.

The command hooks require Python 3.9 or later on `PATH`. This repository validates the plugin schema against Claude Code 2.1.220 and runs deterministic Hook tests with Python 3.14.6 on Windows.

The JSON cases under `skills/capability-harness/evals/` are maintenance evaluation data, not automated Hook tests and not the `claude plugin eval` early-access format.

## Manual context-enrichment check

Start a fresh session with the project plugin loaded, then submit the same short prompt without adding design details:

```text
生成一只骑自行车的鹈鹕的 SVG
```

For an open-ended artifact, the expected sequence is a `capability-harness:context-scout` call, direct/component/adjacent WebSearch or WebFetch work, a compact Context Pack, actual SVG generation, rendered observation, and a skeptical evaluation of the rendered artifact. The user prompt should remain unchanged; the missing details belong in the Context Pack.

For a negative control, use:

```text
生成一个 24x24 SVG 红色圆形图标，固定尺寸和颜色，不需要视觉创新。
```

This fully specified task should not require context enrichment or WebSearch. Compare the first prompt with a separate plugin-disabled session using the identical original text; judge the rendered artifacts, not only XML validity. Keep exact-query retrieval and adjacent-only retrieval as separate comparisons when measuring capability gains.
