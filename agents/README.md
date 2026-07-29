# Agent Sources

This directory contains versioned Claude Code custom-agent source for this repository. It is not a host discovery directory and does not activate agents by itself.

Install only reviewed agents that match the intended workflow:

- project: `<project>/.claude/agents/`
- user: `~/.claude/agents/`

The agents in `capability-harness/` are optional leaf execution roles. They do not define top-level task routing, replace an active domain method, own integration, or create a second orchestration layer. A controller must assign one bounded question or verification scope and provide the relevant method, evidence, constraints, permissions, and acceptance contract.

The repository source directory `agents/`, the Claude Code runtime directory `.claude/agents/`, and `.agents/` are different paths with different roles. Install only reviewed agent Markdown files; do not copy unrelated skills, hooks, or settings as part of agent installation. The runtime selector is the frontmatter `name` shown below; `capability-harness/` is only a source organization directory and is not part of the agent name.

| Agent | Bounded role |
| --- | --- |
| `harness-evidence-researcher` | Gather repository or explicitly authorized current primary-source evidence for one material uncertainty. |
| `harness-independent-brancher` | Produce one materially independent alternative without anchoring on a preferred candidate. |
| `harness-execution-verifier` | Run one authorized, bounded observable verification against an identified artifact or environment. |
| `harness-skeptical-evaluator` | Evaluate actual candidates or results against supplied constraints and evidence. |

All four agents are leaf workers and omit delegation tools. They also omit file-editing tools. `harness-execution-verifier` retains shell execution, which is not a technical read-only sandbox: the controller must resolve command effects and authorization before assignment, and the agent must report unavailable unsafe checks as unverified.

Installing these files does not install a `capability-harness` skill or enable hooks. Selection and integration remain with the active workflow, including `agent-workflow` when multiple independent slices need coordination. See `skills/agent-workflow/references/capability-harness.md` for that composition method.

On Claude Code 2.1.198 or later, `/agents` no longer lists or manages discovered profiles. If the target `agents` directory did not exist when the current session started, restart Claude Code before testing discovery. Static source checks do not prove runtime discovery or model selection behavior. See the current [Claude Code subagents documentation](https://code.claude.com/docs/en/sub-agents).

## Supported invocation mode

These profiles are controller-owned leaf roles. Use them only through a host-supported leaf-delegation path that preserves one outer controller, such as an explicit profile selection or an active workflow. Do not install one as the project default agent or use it as the main Claude Code session through `--agent`; these profiles do not own routing, integration, permissions, recovery, user interaction, or final completion decisions. If a reusable main-session agent is needed, define a separate controller profile rather than expanding a leaf profile.

## Discovery and collision checks

A natural-language request alone is not a deterministic discovery test: the model may decline to delegate or select another applicable profile. In a target Claude Code environment:

1. Use the host's documented explicit profile-selection mechanism, such as an `@agent-<name>` mention when that form is supported.
2. Run one bounded, harmless task for each installed `harness-*` profile, without file edits, network access, or other external side effects.
3. Confirm the selected profile's frontmatter name, tool list, and bounded leaf behavior from runtime evidence rather than source files alone.
4. Check the host scopes that apply to the installation, including managed or organization-provided profiles, CLI-supplied profiles, project and user agent directories, and plugins, for duplicate frontmatter names.
5. Use any current host-documented diagnostic command for discovery or shadowing when available.

The frontmatter `name`, not the source subdirectory, identifies a profile. Do not install duplicate definitions with the same name in one scope, and do not claim which definition wins without evidence from the target host. A repository checkout can document this procedure but cannot prove discovery, tool enforcement, model selection, restart behavior, or scope precedence by itself.
