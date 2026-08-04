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

## `frontend-ui-engineering`

- Source: `addyosmani/agent-skills`, skill `frontend-ui-engineering` and its accessibility checklist.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: a framework-neutral UI/a11y behavior baseline for semantic controls, names, keyboard/focus, dynamic and form states, responsive use, project design-system fit, and behavior-specific evidence through a narrow automatic workflow Skill and skill-local checklist.
- Not retained: broad triggers for every UI edit, React/Tailwind/state-library prescriptions, fixed breakpoints or component-size limits, generic visual recipes, blanket WCAG/tool/browser checks, automatic browser/MCP/axe execution, and architecture, testing, or completion ownership.

## `browser-testing-with-devtools`

- Source: `addyosmani/agent-skills`, skill `browser-testing-with-devtools`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: a narrow browser-runtime evidence provider for explicit live DOM, console, network, screenshot, focus, accessibility, or runtime-performance claims; minimum-signal selection; action-specific authorization; secret and untrusted-browser-content boundaries; separate observed data, inference, and gaps reporting; and `BLOCKED`/`UNVERIFIED` handling when the authorized channel or environment is unavailable.
- Not retained: broad triggers for all browser-facing work, Chrome/provider-specific installation or MCP/settings setup, `npx` or server startup, automatic navigation or interaction, universal console/network/screenshot/accessibility/performance gates, credential or storage inspection, and UI, test, debugging, performance, completion, or branch ownership.

## `code-review-and-quality`

- Source: `addyosmani/agent-skills`, skill `code-review-and-quality`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: optional tests-first context reading and a narrow structural-remedy lens, merged into the existing `review-and-finish` template without creating another review owner.
- Not retained: every-change review gates, a second Skill/persona/command, multi-model review loops, fixed size thresholds, automatic remediation or cleanup, and commit, push, merge, PR, publish, or deploy actions.

## `security-and-hardening`

- Source: `addyosmani/agent-skills`, skill `security-and-hardening`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: a framework-neutral threat-boundary method that maps the relevant asset, actor, entry point, trust boundary, security invariant, abuse path, and focused evidence; selects only applicable lenses; and distinguishes observed evidence, assumptions, risks, controls, gaps, and recommendations.
- Not retained: blanket STRIDE/OWASP/header/CORS/rate-limit gates, target agents or personas, commands, hooks, or evals, fixed library or framework settings, requesting/reading/printing real credentials, tokens, cookies, keys, or secrets, exploit or dependency/script execution without action-specific authorization, automatic remediation, completion or readiness judgment, and branch or publication actions.

## `performance-optimization`

- Source: `addyosmani/agent-skills`, skill `performance-optimization`, with comparison evidence from its `performance-checklist` reference and `web-performance-auditor` agent.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: a framework-neutral measure-first method that defines the claim, metric, scope, workload, comparison, and correctness invariant; labels evidence sources; attributes one bottleneck and one change at a time; accounts for run-to-run variance; and reports a correctness-gated keep, revert, or inconclusive recommendation with observed measurements, inference, and gaps separated.
- Not retained: fixed budgets, thresholds, sample counts, time or size limits; Core Web Vitals, Lighthouse, RUM/CrUX, or other fixed web-tooling requirements; target agents or personas, commands, hooks, evals, or fixtures; automatic benchmarks or profiling; monitoring, RUM setup, production load, remediation, code/configuration edits, deployment/publication, or branch actions.

## `git-workflow-and-versioning`

- Source: `addyosmani/agent-skills`, skill `git-workflow-and-versioning`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: commit-craft guidance merged into `finish-branch` after explicit commit authorization: keep a logical, independently reviewable scope where practical, use relevant evidence without universal gates, and write an intent-bearing message.
- Not retained: `Always` activation, automatic commit, fixed line-count or branch policies, mandatory npm/lint/type/Husky gates, reset/cleanup, tag push, feature-flag policy, and any push, merge, PR, deployment, or publication action inferred from commit guidance.

## `ci-cd-and-automation`

- Source: `addyosmani/agent-skills`, skill `ci-cd-and-automation`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: a narrow repository-owned pipeline-definition method that reads actual provider and toolchain facts, defines scoped triggers/jobs/dependencies/artifacts/secret references/failure semantics, and distinguishes definition, local, hosted, required-status, and deployment evidence.
- Not retained: universal lint/type/test/build/security/E2E/bundle gates, GitHub/Node/Prisma/Playwright/Vercel prescriptions, fixed time or threshold budgets, hosted execution, branch protection or auto-merge changes, credential access, network or installation, automatic commit/push/merge, deployment, rollback, or publication.