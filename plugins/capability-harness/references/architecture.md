# Architecture

## Objective

Increase effective system capability without changing model weights by externalizing five functions that a model may perform unreliably: context discovery, information acquisition, alternative generation, observable verification, and independent evaluation.

The harness is a bounded control protocol. It is not a promise that every task needs a worker, a web search, or a second opinion.

## Control plane and capability plane

The control plane is the project Skill and its lifecycle hooks. It extracts a task contract, records routing metadata, and applies bounded completion checks. The capability plane contains repository inspection, current-source retrieval, leaf agents, deterministic commands, and domain-specific tools.

The active domain Skill remains responsible for implementation, repair, and final acceptance. If another controller already owns a workflow, the harness supplies evidence to that controller instead of creating a second orchestration layer.

## Project plugin mapping

The current project plugin maps the protocol to these components:

- `skills/capability-harness/SKILL.md` — method capsule and module-selection rules;
- `agents/context-scout.md` — bounded discovery of omitted domain and quality context;
- `agents/evidence-researcher.md` — bounded repository or explicitly authorized current-source evidence;
- `agents/independent-brancher.md` — one materially different candidate;
- `agents/execution-verifier.md` — one bounded observable check;
- `agents/skeptical-evaluator.md` — independent judgment over supplied artifacts or results;
- `hooks/hooks.json` — `UserPromptSubmit`, `SubagentStop`, and `Stop` lifecycle hooks;
- `hooks/*.py` and `hooks/lib/common.py` — routing, contract, and project-state mechanics;
- `references/` — design and operating guidance for maintainers, not an additional runtime component;
- `tests/` and `skills/capability-harness/evals/` — development and maintenance data, not automatic task workers.

## State machine

1. **INTAKE** — extract the objective, hard constraints, project facts, quality-sensitive decisions, unknowns, and available checks.
2. **GAP MAP** — identify omitted domain, structural, compositional, medium-specific, or project context that could change quality.
3. **CONTEXT DISCOVERY** — use the smallest bounded direct, component, and adjacent evidence pass to build a Context Pack when needed.
4. **ROUTE** — choose the single highest-value next capability module or a small independent set.
5. **ACQUIRE** — obtain external or project evidence for factual or current claims.
6. **BRANCH** — produce materially distinct alternatives in isolation.
7. **EXECUTE** — test or observe actual behavior.
8. **EVALUATE** — compare real outputs independently.
9. **INTEGRATE** — update the current-best result and unresolved-risk register.
10. **REPAIR** — make a targeted change against a confirmed defect.
11. **FINALIZE** — stop only after bounded completion checks.

Transitions are evidence-driven, but the controller must not require the user to name an implicit context gap. A module must not run merely because it exists, and the hooks do not launch all workers automatically.

## Deployment boundary

This repository owns a project-scoped plugin under `plugins/capability-harness/`. The supported installation is local to the current project, or a one-session `claude --plugin-dir` load for validation. Runtime state is written under the active project at `.claude/capability-harness/state/`.

The initial bundle's global installer and global `~/.claude` deployment model are intentionally not part of this plugin. Nothing in this plugin should modify `C:\Users\wang\.claude` or install a user-wide agent, Skill, hook, or instruction block.

## Reliability boundaries

The harness can improve effective performance when useful context, evidence, observable checks, independent alternatives, or explicit quality criteria exist. It is weakest when quality depends on tacit taste, unprecedented insight, private missing information, visual references unavailable to the toolchain, or a judge that shares the generator's blind spots. Preserve uncertainty instead of converting a bounded pass into a global optimality claim.
