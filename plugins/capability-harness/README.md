# Capability Harness

A self-contained Claude Code plugin for bounded evidence gathering, independent alternatives, observable verification, and skeptical evaluation.

The plugin is additive. Existing domain Skills keep method ownership, and `agent-workflow` keeps multi-agent coordination ownership when it is already active. Plugin components are namespaced, so they do not replace the repository's standalone Skills or user-level agents.

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
claude --plugin-dir .\plugins\capability-harness
```

Inside Claude Code, verify the Skill in `/context`, verify the four `capability-harness:*` agents in the Custom Agents section, and inspect the plugin hooks with `/hooks`.

Invoke the Skill explicitly with:

```text
/capability-harness:capability-harness <task>
```

Append `[harness:off]` to a prompt to suppress the per-prompt routing reminder for that turn.

The command hooks require Python 3 on `PATH`. This repository tests the plugin against Claude Code 2.1.220 on Windows before publishing it through the repository marketplace.
