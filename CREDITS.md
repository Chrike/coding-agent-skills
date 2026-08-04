# External Source Credits

## `using-agent-skills`

- Source: `addyosmani/agent-skills`, skill `using-agent-skills`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: the idea that skill selection should use the smallest clearly matching workflow and preserve explicit ownership boundaries; surface only material assumptions; and state concrete technical tradeoffs with a workable alternative.
- Not retained: SessionStart injection, a second global meta-router, a mandatory full-lifecycle chain, a universal Definition-of-Done gate, or target-specific sibling handoffs. Those conflict with this suite's lightweight default, maintained routing contract, host-owned boundaries, and action-specific authorization.

## `interview-me`

- Source: `addyosmani/agent-skills`, skill `interview-me`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: explicit pre-planning intent interviews, one focused question at a time with a visible hypothesis, conditional want-versus-should probing, a six-part intent restatement, and explicit confirmation before treating intent as settled.
- Not retained: automatic interviews for every vague request, a universal numeric confidence gate, default `docs/intent/[topic].md`, automatic spec/plan/task generation, or target-specific downstream handoffs. Ordinary requests remain in the base flow and persistence requires an explicit target and request.

## `idea-refine`

- Source: `addyosmani/agent-skills`, skill `idea-refine` and its ideation/evaluation references.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: explicit concept-level divergence and convergence, selective problem-reframing lenses, small materially different alternatives, user-value/feasibility/differentiation evaluation, assumption tiers, MVP/first-experiment thinking, and an explicit Not Doing list.
- Not retained: automatic vague-request triggers, `stress-test my plan` routing, fixed question/variation counts, `/ideate` command assumptions, `docs/ideas` initialization or default persistence, automatic planning/issue/implementation handoffs, and example prose as runtime instructions.

## `spec-driven-development`

- Source: `addyosmani/agent-skills`, skill `spec-driven-development`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: explicit spec-authoring fields for objective, evidence-backed context, material assumptions, behavior/success criteria, boundaries, testing intent, non-goals, and open questions, as a non-tracker draft mode inside `issue-workflow`.
- Not retained: broad automatic triggers, universal review gates, default `SPEC.md`/`tasks/*` paths, automatic PLAN/TASKS/IMPLEMENT handoffs, command execution, commit/PR requirements, and target-specific sibling invocation.

## `api-and-interface-design`

- Source: `addyosmani/agent-skills`, skill `api-and-interface-design`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: a project-fact-first contract lens for consumer-observable inputs, outputs, errors, boundary validation, additive compatibility, and behavioral verification through public seams, as a reference under `design-codebase`.
- Not retained: a second API owner, fixed REST/GraphQL/TypeScript conventions, unconditional internal trust, default pagination or error shapes, automatic migration/consumer updates, command execution, publication, or branch actions.

## `planning-and-task-breakdown`

- Source: `addyosmani/agent-skills`, skill `planning-and-task-breakdown`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: the distinction between a per-step observable `Acceptance criteria` result and the separate `Verification` evidence, added to the existing `plan-work` durable template.
- Not retained: a second Plan owner, default `tasks/*` files, fixed checkpoints or approval gates, file/time thresholds, universal Definition of Done, mandatory dependency graphs, or automatic parallelization and branch actions.

## `incremental-implementation`

- Source: `addyosmani/agent-skills`, skill `incremental-implementation`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: optional contract-first and risk-first slice selection, checking a slice's acceptance evidence before expanding it, and keeping increments narrow and independently revertable in the existing `plan-work` vertical-slice reference.
- Not retained: multi-file or line-count auto-triggers, mandatory per-slice commits, universal test/build/type/lint commands, feature-flag requirements, automatic branch actions, and a second Build execution owner.

## `doubt-driven-development`

- Source: `addyosmani/agent-skills`, skill `doubt-driven-development`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: a de-anchored `ARTIFACT` plus `CONTRACT` packet, adversarial mismatch framing, and bounded reconciliation categories in the existing `agent-workflow` fresh-context reference.
- Not retained: universal fresh review for every non-trivial decision, mandatory cross-model CLI offers, automatic orchestrators, persona nesting, unbounded review loops, or commit/branch actions.

## `context-engineering`

- Source: `addyosmani/agent-skills`, skill `context-engineering`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: explicit context audits, focused context packs, source-backed conflict and gap reporting, and bounded context/rules setup with a read-only default.
- Not retained: automatic new-session or task-switch triggers, fixed token/line thresholds, default rules-file creation, automatic compaction, MCP or external-context setup, command execution, or downstream lifecycle handoffs.
