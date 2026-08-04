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
- Retained in this suite: a framework-neutral UI/a11y behavior baseline for semantic controls, names, page-shell and skip-path structure, keyboard/focus, dynamic and form states, responsive use, motion/text-size use, project design-system fit, and behavior-specific evidence through a narrow automatic workflow Skill and skill-local checklist.
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

- Source: `addyosmani/agent-skills`, skill `security-and-hardening` and comparison agent `security-auditor`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: a framework-neutral threat-boundary method that maps the relevant asset, actor, entry point, trust boundary, security invariant, abuse path, and focused evidence; selects only applicable lenses; and uses concrete, conditional prompts for resource scope, untrusted sinks, integrations, sensitive data, and AI/tool permissions.
- Not retained: blanket STRIDE/OWASP/header/CORS/rate-limit gates, a standalone persona or fixed audit output, target commands/hooks/evals, fixed library or framework settings, requesting/reading/printing real credentials, tokens, cookies, keys, or secrets, exploit or dependency/script execution without action-specific authorization, automatic remediation, completion or readiness judgment, and branch or publication actions.

## `security-checklist`

- Source: `addyosmani/agent-skills`, reference `security-checklist.md`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: a conditional threat, access/input, integration/data, automation/dependency, and evidence prompt set under `security-and-hardening`.
- Not retained: universal OWASP/STRIDE, fixed headers/CORS/rate-limit/severity thresholds, secret-scanning commands, install or audit execution, pre-commit or release gates, code examples as requirements, and automatic remediation or branch actions.

## `performance-optimization`

- Source: `addyosmani/agent-skills`, skill `performance-optimization`, with comparison evidence from its `performance-checklist` reference and `web-performance-auditor` agent.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: a framework-neutral measure-first method that defines the claim, metric, scope, workload, comparison, and correctness invariant; labels evidence sources; supports source-only versus artifact-backed web audits with metric honesty and framework identification; attributes one bottleneck and one change at a time; accounts for run-to-run variance; and reports a correctness-gated keep, revert, or inconclusive recommendation with observed measurements, inference, and gaps separated.
- Not retained: fixed budgets, thresholds, sample counts, time or size limits; Core Web Vitals, Lighthouse, RUM/CrUX, or other fixed web-tooling requirements; target agents or personas, commands, hooks, evals, or fixtures; automatic benchmarks or profiling; monitoring, RUM setup, production load, remediation, code/configuration edits, deployment/publication, or branch actions.

## `performance-checklist`

- Source: `addyosmani/agent-skills`, reference `performance-checklist.md`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: a conditional loading/resource, rendering/input, data/backend, and correctness/evidence prompt set under `performance-optimization`.
- Not retained: fixed Core Web Vitals or response targets, bundle budgets, framework recipes, Lighthouse/DevTools/CrUX commands, profiling or dependency installation, production load, monitoring/RUM, and release or branch gates.

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

## `deprecation-and-migration`

- Source: `addyosmani/agent-skills`, skill `deprecation-and-migration`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: an on-demand `plan-work` reference for consumer inventory, replacement or no-replacement decisions, notification and compatibility windows, exception ownership, usage-gated removal criteria, and conditional expand/contract planning.
- Not retained: a second migration owner, compulsory deadlines, universal feature flags or adapters, claims that additive changes are always safe, automatic down migrations, notices, traffic changes, backfills, deployment, deletion, or branch actions.

## `documentation-and-adrs`

- Source: `addyosmani/agent-skills`, skill `documentation-and-adrs`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: a compact ADR convention-discovery and lifecycle lens in `design-codebase`: inspect location, format, numbering, headings, status, and tooling; preserve prior records; and supersede with a linked successor when a selected decision changes.
- Not retained: a second documentation owner, automatic README/API/comment/changelog or ADR writes, a guessed `docs/decisions/` path, universal documentation checklists, automatic cleanup, or publication and branch actions.

## `observability-and-instrumentation`

- Source: `addyosmani/agent-skills`, skill `observability-and-instrumentation`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: a question-driven telemetry owner for minimum useful structured logs, metrics, traces, or alerts; project-conforming schema and context; bounded cardinality; data minimization; and separate definition, static, local, runtime, and operational-response evidence.
- Not retained: triggers for every production feature or I/O PR, mandatory RED/USE/full tracing/alert checklists, fixed vendor or dependency choices, automatic dashboards or monitoring, test traffic, failure injection, remote alert actions, unbounded labels, sensitive payload logging, deployment, or branch actions.

## `observability-checklist`

- Source: `addyosmani/agent-skills`, reference `observability-checklist.md`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: conditional prompts for structured events and correlation, bounded distributions and queue signals, relevant trace propagation, and symptom-based alert/dashboard questions under `observability-and-instrumentation`.
- Not retained: mandatory RED/USE/full tracing, fixed labels or thresholds, vendor/bootstrap requirements, dashboard or alert publication, test traffic, failure injection, production access, pre-launch gates, or branch actions.

## `shipping-and-launch`

- Source: `addyosmani/agent-skills`, skill `shipping-and-launch`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: a concrete-release readiness owner with a release packet, criterion-level `VERIFIED`/`FAILED / BLOCKER`/`UNVERIFIED` evidence, separate repository and production claims, project-specific rollout/rollback semantics, and explicit action owners.
- Not retained: universal launch checklists, fixed rollout percentages or time windows, fixed thresholds or Web metrics, mandatory feature flags, fixed persona fan-out, sequential-as-parallel claims, automatic deploy/flag/migration/rollback/notification/monitoring, or branch and publication actions.

## `orchestration-patterns` and `docs/agents.md`

- Source: `addyosmani/agent-skills`, references `orchestration-patterns.md` and `docs/agents.md`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: host/persona relationship guidance under `agent-workflow`: direct ownership first, no router or persona-to-persona calls, reuse of fitting host capabilities, and explicit separation between subagent reports, teammate communication, and observed host support.
- Not retained: target-specific `/ship` fan-out, command/persona wiring, fixed lifecycle orchestration, Agent Teams setup claims, manifest-based proof of discovery or fresh context, nested controllers, or a second orchestration owner.

## `code-simplification` protected-block hook

- Source: `addyosmani/agent-skills`, the `simplify-ignore` hook and its protected-block guidance.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: an explicit opt-in, current-owned plugin with project-root and symlink boundaries, standard-library Python hooks, bounded backup/restore state, and fail-open behavior for unknown payloads or host events.
- Not retained: automatic installation, target Bash/jq dependencies, network or shell execution, unbounded in-place filtering, target command ownership, external-path recovery, or claims that static/local checks prove host hook ordering or runtime isolation.

## `evals` and validation framework

- Source: `addyosmani/agent-skills`, `evals/README.md`, `run-evals.js`, `validate-skills.js`, `skill-lint.js`, and `run-evals-test.js`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: a three-tier evidence distinction, current-owned deterministic structure/routing checks, explicit plugin-local tests, pairwise owner cases, and `UNVERIFIED` handling for host/model/browser/runtime claims, documented in `tests/eval-contract.md` and implemented by `tests/validate_suite.py` and `tests/check_routing_contract.py` with focused tests.
- Not retained: a second runtime router, universal rank or similarity gates, target headless Claude executors, automatic fixture Git workspaces, browser/network/dependency execution, external graders, persistent eval results, CI integration, or target prompt-shaped corpus instructions.
