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
