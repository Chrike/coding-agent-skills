# Capability Harness

A self-contained Claude Code plugin for bounded evidence gathering, independent alternatives, observable verification, and skeptical evaluation after the active domain method or direct workflow is established.

The plugin is supplementary. Existing domain Skills keep implementation and repair ownership, and `agent-workflow` keeps multi-agent coordination ownership when it is already active. Plugin components are namespaced, so they do not replace the repository's standalone Skills or user-level agents.

## Install

For an installation limited to the current project, run from the repository root:

```powershell
claude plugin marketplace add . --scope local
claude plugin install capability-harness@coding-agent-skills --scope local
```

Use `--scope user` instead only when you intentionally want the marketplace and plugin available to every Claude Code project for that user.

## Local validation

From the repository root:

```powershell
claude plugin validate .\plugins\capability-harness --strict
$env:PYTHONDONTWRITEBYTECODE = "1"
python -m unittest discover -s .\plugins\capability-harness\tests -v
```

For an explicitly authorized runtime check, load the source for one session with `claude --plugin-dir .\plugins\capability-harness`, then verify the Skill in `/context`, the four `capability-harness:*` agents in the Custom Agents section, and the scoped hook in `/hooks`.

Invoke the Skill explicitly with:

```text
/capability-harness:capability-harness <task>
```

Claude may invoke the Skill automatically from its narrow description. Explicit user instructions and an existing controller remain authoritative; the plugin does not install a per-prompt routing hook.

The command hook requires Python 3.9 or later on `PATH`. This repository validates the plugin schema against Claude Code 2.1.220 and runs deterministic Hook tests with Python 3.14.6 on Windows.

The JSON cases under `skills/capability-harness/evals/` are maintenance evaluation data, not automated Hook tests and not the `claude plugin eval` early-access format.
