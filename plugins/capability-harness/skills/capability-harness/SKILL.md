---
name: capability-harness
description: Apply a decision-first capability-harness pass to substantive work when a model may miss context, evidence, an observable check, or a materially different alternative. Before generating or modifying, choose the smallest action that can change the result; do not use for routine direct work, fixed pipelines, cosmetic variants, or work already owned by another controller.
---

# Capability Harness

The project-scoped prompt hook supplies candidate signals only. It never launches workers, records hidden reasoning, or blocks completion. This Skill supplies a pre-action decision method; it does not replace the active domain method or make every task a multi-step workflow.

## Capability Decision

Before materially generating, modifying, or recommending, identify:

- the requested outcome and hard constraints;
- the single highest-impact unknown, quality risk, or unsupported assumption;
- the external signal, observation, or alternative that could change the approach or result;
- the smallest action that can obtain that signal, or the reason to proceed directly;
- the permission, data, side-effect, and stop boundary.

Make this decision before implementation. A candidate signal from the prompt hook is not a requirement. Do not search, delegate, or review merely because a tool or worker exists. If no available action can materially change the result, use the direct path and state the intrinsic limitation or remaining uncertainty when material.

## Context Discovery

For an open-ended visual, design, architecture, recommendation, or artifact task, consider `capability-harness:context-scout` only when omitted domain, structural, compositional, or medium-specific context could change a named decision. Give it the original outcome and constraints; do not make the user write the missing checklist into the prompt.

The scout first states whether research can change that decision. It may return a direct-route skip rather than manufacture a Context Pack. When it does research, use its compact evidence and validation cues to guide the active domain method. Do not paste raw search results into the task, copy an existing artifact, or treat the scout as the final evaluator.

## Reference Policy

Read only the references that bear on the current decision:

- [routing policy](../../references/routing-policy.md) before selecting a module;
- [capability contracts](../../references/capability-contracts.md) before writing a leaf-agent brief or interpreting its result;
- [evidence policy](../../references/evidence-policy.md) for WebSearch/WebFetch or repository evidence;
- [evaluation policy](../../references/evaluation-policy.md) when comparing capability choices, candidates, or revisions;
- [failure recovery](../../references/failure-recovery.md) when a tool, agent, source, or decision route fails;
- [architecture](../../references/architecture.md), [design intent](../../references/design-intent.md), and [installation](../../references/installation.md) for plugin boundaries and maintenance.

These references describe the current project plugin. The current agent files and `SubagentStop` minimum headings take precedence over older or external harness examples.

## Module Selection

Use only the module that can change the selected decision:

- `capability-harness:context-scout` for one bounded missing-context question before generation or recommendation;
- `capability-harness:evidence-researcher` for one bounded repository or explicitly authorized current-source question;
- `capability-harness:independent-brancher` for one materially different candidate when anchoring or a real trade-off remains;
- `capability-harness:execution-verifier` for one exact claim with an identified target, permitted effects, and observable acceptance signal;
- `capability-harness:skeptical-evaluator` for actual candidate artifacts or results whose material quality is not settled by deterministic checks.

Each worker is a leaf. Give it one bounded brief, the decision it is meant to inform, actual evidence or artifact scope, constraints, permissions, return contract, and stop condition. Do not launch all workers by default. If another workflow already owns coordination, route any needed module through that controller instead of creating a second orchestration layer.

## Integration

Prefer current repository evidence for repository behavior and official or primary current sources for external claims. Match verification to the requested outcome: source syntax alone does not establish rendered, runtime, interactive, calculated, or user-visible quality. Preserve blocked, failed, stale, and unverified evidence states instead of collapsing them into success.

The active controller and domain Skill own implementation, repair count, acceptance, and final integration. Harness workers return bounded context, evidence, candidates, verification, or evaluation; they do not limit or replace domain-workflow repairs. Preserve the strongest verified result seen so far. Report a selected route and brief reason only when it makes a material decision observable; do not claim global optimality or overall task completion.
