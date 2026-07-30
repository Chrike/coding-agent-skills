# Decision-First Routing Policy

Choose the next action by the largest unresolved impact, not by a task label, keyword, or fixed workflow. The unit of routing is a model-task decision: the same request may need external help for one model and not for another.

## Pre-Action Test

Before the first material generation, implementation, or recommendation, answer four questions:

1. What specific decision could change the result most?
2. What missing signal prevents that decision from being well supported?
3. Which available action can obtain that signal, and how would its result change the approach?
4. Is that expected gain greater than the action's cost, latency, noise, and risk?

If a route cannot answer all four, it is not selected. Candidate signals from `UserPromptSubmit` are prompts to consider a route, not mandatory actions. Keep the decision compact; do not turn it into a generic task taxonomy.

## Direct Path

Proceed directly when the task is low consequence, adequately specified, and no available evidence, observation, or independent alternative can materially change the result. Direct does not mean unverified: perform a check when the user explicitly requests one or when a concrete claim needs observation.

## Context Discovery

Use `context-scout` before generation or recommendation when omitted domain, structural, compositional, interaction, or medium-specific information can change a named decision. The scout must first explain what its discovery could change. If it cannot, it returns a direct-route skip instead of searching.

When selected, use a bounded direct, component, adjacent-principle, or medium-technique pass. Keep only evidence that maps to the decision, hard constraints, a real risk, or a validation cue. Do not copy exact reference artifacts or inflate the prompt with raw pages.

## Evidence Acquisition

Use repository inspection when local code, configuration, history, or conventions control the answer. Use focused external evidence for current, version-specific, product-specific, legal, regulatory, medical, financial, security-sensitive, or otherwise consequential claims. Prefer project evidence before generic web guidance when project facts decide the issue.

## Alternatives, Observation, and Evaluation

Generate an independent alternative only when a different load-bearing assumption, architecture, optimization target, or risk posture remains plausible. Execute whenever a concrete claim can be observed through tests, compilation, rendering, benchmarking, calculation, simulation, or direct inspection. Use an independent evaluator only after actual candidates and observable evidence leave a material quality question unresolved.

Do not use an LLM evaluator as the sole authority for deterministic facts. Observable evidence outranks model judgment.

## Capability Limits

If the missing ability is intrinsic and no permitted tool can provide a useful signal, do not simulate confidence with more retrieval or agents. Use a suitable specialist model or domain tool when available, ask for a missing user-owned choice, or state the remaining limitation. Search can add domain detail; it does not automatically create spatial reasoning, perception, taste, or a missing execution environment.

## Escalation Budget

Start with one selected action. Take a second action only when the first produced evidence that changed the decision or exposed a new high-impact uncertainty. Never increase agent count merely because uncertainty remains. Change the evidence type, seek an observable signal, or stop with a disclosed limitation.
