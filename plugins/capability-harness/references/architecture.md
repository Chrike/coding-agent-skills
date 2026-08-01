# Architecture

## Objective

Increase effective system capability without changing model weights by making a better decision before the first material action. The harness externalizes context discovery, information acquisition, alternative generation, observable verification, and independent evaluation only when one of them can supply a bounded signal or plan input that improves the next decision.

The harness is not a promise that every task needs search, a worker, a review, or a repair loop. It cannot create an intrinsic capability that no available tool, source, observation, or specialist can supply.

## Control Plane and Capability Plane

The control plane is the project Skill and its lightweight hooks. `UserPromptSubmit` names one strong pre-action route when prompt signals make the next evidence source clear, then the active controller executes that route once before material work; direct and explicitly controller-owned workflow prompts receive no injected context. A leading slash alone is not treated as controller ownership. `SubagentStop` validates the return schema of a selected leaf worker. Neither hook launches a worker, writes runtime state, or blocks a substantive turn for failing to call a particular tool; an unavailable selected route is reported through its bounded skip or unavailable-evidence outcome.

The capability plane contains repository inspection, current-source retrieval, leaf agents, deterministic commands, renderers, and domain-specific tools. The active domain Skill remains responsible for implementation, repair, and final acceptance. If another controller already owns a workflow, the harness supplies evidence to that controller instead of creating a second orchestration layer.

## Project Plugin Mapping

- `skills/capability-harness/SKILL.md` — decision-first method capsule and module-selection rules;
- `agents/context-scout.md` — bounded assessment and discovery of omitted context that can change one decision;
- `agents/evidence-researcher.md` — bounded repository or explicitly authorized current-source evidence;
- `agents/independent-brancher.md` — one materially different candidate;
- `agents/execution-verifier.md` — one bounded observable check; command execution requires an exact controller brief and remains subject to host permissions;
- `agents/skeptical-evaluator.md` — independent judgment over supplied artifacts or results;
- `hooks/hooks.json` — `UserPromptSubmit` and `SubagentStop` hooks;
- `hooks/*.py` and `hooks/lib/common.py` — candidate-signal and leaf-contract mechanics;
- `references/` — maintainer guidance, not another runtime instruction layer;
- `tests/` and `skills/capability-harness/evals/` — maintenance and calibration data, not automatic task workers.

## Decision-First State Machine

1. **INTAKE** — extract the objective, hard constraints, project facts, available checks, and boundaries.
2. **DECIDE** — name the highest-impact unknown or quality risk; identify the missing context or signal that could improve the plan; select the direct path when no useful bounded action exists.
3. **DISCOVER OR ACQUIRE** — obtain only the selected bounded context or evidence and compress it into plan implications.
4. **ROUTE** — choose the single highest-value next capability module, if one remains useful.
5. **EXECUTE** — implement, render, test, calculate, or otherwise observe the real result through the active domain method.
6. **EVALUATE** — compare actual results independently only when deterministic checks leave a material quality question.
7. **INTEGRATE** — update the current-best result and disclose unresolved risks.
8. **REPAIR** — make a targeted change only against a confirmed defect.
9. **FINALIZE** — stop when another capability call is unlikely to alter an important decision or result.

The important transition is from **DECIDE** to the first material action. Later review is useful for confirmed defects, but it should not substitute for deciding what information or observation would have improved the original approach.

## Deployment Boundary

This repository owns a project-scoped plugin under `plugins/capability-harness/`. The supported installation is local to the current project, or a one-session `claude --plugin-dir` load for validation. It does not write per-session routing state and does not modify the user's global Claude Code configuration.

## Reliability Boundaries

The harness can improve effective performance when useful context, evidence, observable checks, independent alternatives, or explicit quality criteria exist. The current Hook does not identify the active model or measure its true capability boundary; it detects only a narrow set of model-agnostic strong routes, while the active controller retains the contextual decision. Use calibration cases to learn where a particular model benefits. The harness is weakest when quality depends on tacit taste, unprecedented insight, private missing information, unavailable perception, or a judge that shares the generator's blind spots. Preserve uncertainty instead of turning an unavailable capability into an artificial Decision Brief or a global-optimality claim.
