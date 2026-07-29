# Design Intent

## Purpose

Capability Harness is a test-time capability amplifier for models that can complete a task but may miss the domain context, salience, or quality details that a stronger model notices. The primary goal is not to install more agents or to verify only whether a file is syntactically valid.

Given the same terse user request, the project-scoped workflow may discover omitted high-impact context, compress it into an actionable Context Pack, generate with the active domain method, observe the real result, and perform a bounded quality correction.

## Canonical example

For a request such as "generate an SVG of a pelican riding a bicycle", the user prompt should remain short. The harness may discover pelican anatomy, bicycle structure, motion and contact relationships, composition cues, vector craft, and common omissions through direct, component, and adjacent searches. Those details belong in the internal Context Pack, not in a rewritten user prompt.

## Routing intent

- fixed, fully specified, low-consequence work may remain on the direct path;
- open-ended visual, design, architecture, recommendation, and artifact work defaults to bounded context enrichment when omitted details can change quality;
- current or version-specific claims use evidence research;
- real alternative trade-offs use independent branching;
- observable behavior uses execution verification;
- subjective quality uses an evaluator over the actual result;
- no task launches every worker by default.

The context-enrichment decision must not depend only on words such as "search", "reference", "recommend", or "best". A model can omit those words while still needing domain context.

## Non-goals

This plugin does not guarantee parity with a stronger model, global optimality, or perfect visual quality. It does not copy an exact retrieved artifact as a substitute for generation, authorize side effects, or install into a user-wide Claude directory. Text-only retrieval may be insufficient for visual style or layout; multimodal reference access is a later capability, not an assumption.

## Maintenance rules

When reviewing or changing this plugin without the original conversation:

1. Read this file, `architecture.md`, `routing-policy.md`, and `capability-contracts.md` before changing routing or agent roles.
2. Preserve at least one positive case showing that a terse open-ended visual task requests context enrichment and one negative case showing that a fixed trivial task remains direct.
3. Do not reintroduce an explicit-keyword gate for context enrichment merely to reduce search calls. Measure false routes and quality gains in the evaluation data instead.
4. Keep `context-scout` separate from factual evidence research unless the contract and evaluation cases are deliberately redesigned together.
5. Keep the original prompt unchanged in comparisons. Separate production tests, where exact search may be allowed, from diagnostic tests, where only adjacent searches are allowed to prevent retrieval leakage.
6. Update this file and the matching eval cases whenever the intended trade-off changes.

The current plugin Skill, agent files, hooks, and these references are the maintained implementation contract. The initial bundle and review notes are historical inputs, not active instructions.
