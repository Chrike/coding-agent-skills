# Decision-First Routing Policy

Choose the next action by the largest unresolved impact, not by a task label, keyword, or fixed workflow. The unit of routing is a model-task decision: the same request may need external help for one model and not for another.

## Pre-Action Test

Before the first material generation, implementation, or recommendation, answer four questions:

1. What specific decision could improve the result most?
2. What missing signal or domain context makes that decision fragile?
3. Which available action can obtain that signal, and how will the active controller use it?
4. Is the action bounded, permitted, and proportionate to the uncertainty?

If a route cannot answer all four, it is not selected. Unselected candidate signals from `UserPromptSubmit` are prompts to consider a route, not mandatory actions. A named strong pre-action route is different: execute that one route before material work, subject to its bounded skip or evidence-unavailable outcome. Keep the decision compact; do not turn it into a generic task taxonomy.

## Strong Pre-Action Routes

The prompt hook has a deliberately narrow role: it names a route only when a prompt has a strong, safe signal. A selected route is an instruction to obtain that one signal before material work, not a request for a later compliance review:

- inspect local project facts before generic guidance when repository context can control the answer;
- obtain one focused evidence finding for a current or consequential external fact;
- obtain one Pre-action Decision Brief for open-ended or unfamiliar work where omitted domain context can materially improve a named construction or selection decision.

The hook does not claim to understand every task or launch a worker itself. The active controller executes the selected route. `context-scout` may return its direct-route skip when it cannot identify a plausible bounded context gap. Fixed, low-ambiguity work remains direct, and a user may opt out with `[harness:off]`. An explicit source or network constraint in the current prompt suppresses external discovery while still permitting relevant local project inspection; this is not a default project policy.

## Direct Path

Proceed directly when the task is low consequence, adequately specified, and no available evidence, observation, or independent alternative can materially change the result. Direct does not mean unverified: perform a check when the user explicitly requests one or when a concrete claim needs observation. For the prompt hook, the direct path is silent and emits no additional context.

## Context Discovery

Use `context-scout` before generation or recommendation when omitted domain, structural, compositional, interaction, or medium-specific information may materially improve a named decision. The scout states the decision and missing context, then searches when the gap is plausible and bounded; it does not need to prove in advance that the search will improve the final result. If no bounded source can supply useful task context, it returns a direct-route skip.

When selected, use a bounded direct, component, adjacent-principle, or medium-technique pass. Return only a compact Brief with evidence, applicability, transfer assumptions, and plan implications. Do not copy exact reference artifacts or inflate the prompt with raw pages.

## Evidence Acquisition

Use repository inspection when local code, configuration, history, or conventions control the answer. Use focused external evidence for current, version-specific, product-specific, legal, regulatory, medical, financial, security-sensitive, or otherwise consequential claims. Prefer project evidence before generic web guidance when project facts decide the issue.

## Alternatives, Observation, and Evaluation

Generate an independent alternative only when a different load-bearing assumption, architecture, optimization target, or risk posture remains plausible. Execute whenever a concrete claim can be observed through tests, compilation, rendering, benchmarking, calculation, simulation, or direct inspection. Use an independent evaluator only after actual candidates and observable evidence leave a material quality question unresolved.

Do not use an LLM evaluator as the sole authority for deterministic facts. Observable evidence outranks model judgment.

## Capability Limits

If the missing ability is intrinsic and no permitted tool can provide a useful signal, do not simulate confidence with more retrieval or agents. Use a suitable specialist model or domain tool when available, ask for a missing user-owned choice, or state the remaining limitation. Search can add domain detail; it does not automatically create spatial reasoning, perception, taste, or a missing execution environment.

## Escalation Budget

Start with one selected action. Take a second action only when the first produced evidence that changed the decision or exposed a new high-impact uncertainty. Never increase agent count merely because uncertainty remains. Change the evidence type, seek an observable signal, or stop with a disclosed limitation.
