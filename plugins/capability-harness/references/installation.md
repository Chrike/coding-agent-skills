# Installation and Operation

## Project-local installation

From the repository root, register the repository marketplace and install only for the current project:

```powershell
claude plugin marketplace add . --scope local
claude plugin install capability-harness@coding-agent-skills --scope local
```

After installing in an existing Claude Code session, run `/reload-plugins`, or start a new session. Keep the local scope unless the user explicitly chooses another scope.

## One-session validation

Load the source without installing it:

```powershell
claude --plugin-dir .\plugins\capability-harness
```

Inside the session, inspect `/context` and `/hooks`, then use the `@` mention typeahead or `claude plugin details` to confirm the Skill, five namespaced agents, and two scoped hooks are discoverable. The fifth agent is `capability-harness:context-scout`.

## Repository validation

The command hooks require a Python 3.9 or later executable named `python` on `PATH`; the Hook configuration invokes that
exact command.

```powershell
claude plugin validate .\plugins\capability-harness --strict
$env:PYTHONDONTWRITEBYTECODE = "1"
python -B -m unittest discover -s .\plugins\capability-harness\tests -v
```

## Invocation

The project-scoped `UserPromptSubmit` hook supplies a stateless selected pre-action route when prompt signals make the next source of evidence clear. Direct and explicitly controller-owned workflow prompts produce no additional hook context. A leading slash alone is not treated as controller ownership; Claude Code's command-expansion lifecycle carries that boundary for actual commands. The hook never launches agents, writes runtime state, or blocks completion; the active controller performs the selected route exactly once before material work, or records its bounded skip or unavailable-evidence outcome. Explicit invocation remains available:

```text
/capability-harness:capability-harness <task>
```

Use `[harness:off]` when the current prompt should bypass the routing hook. This is a per-prompt opt-out, not a global installation change. An explicit source or network constraint in the current prompt suppresses external discovery while leaving relevant local project inspection available.

## Scope boundary

This plugin is intentionally project-scoped. It does not install or modify the user's global Claude Code configuration, does not copy the initial bundle's global installer into the runtime, and does not create user-wide agents or hooks.
