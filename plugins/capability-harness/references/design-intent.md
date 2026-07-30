# Design Intent

## Purpose

Capability Harness is a test-time capability amplifier for models that can complete a task but may miss domain context, salience, quality details, evidence, or an observable check that a stronger model would notice before acting. Its primary purpose is to improve the pre-action decision, not to add agents or repairs after the model has already anchored on a weak result.

Given the same terse user request, the project-scoped workflow may identify a missing signal, decide whether bounded discovery can change a concrete approach, obtain only that signal, and then let the active domain method generate or implement. The user should not need to write a hidden domain checklist into the prompt.

## Canonical Example

For a request such as "generate an SVG of a pelican riding a bicycle", the user prompt remains short. A decision-first pass may determine that anatomy, bicycle contact relationships, composition cues, or vector craft can materially change a chosen construction plan, then use direct, component, and adjacent research to supply those cues. If such research cannot change the plan, it should be skipped. The example does not create a special SVG workflow or imply that every visual task needs search.

## Routing Intent

- fixed, fully specified, low-consequence work may remain direct;
- open-ended work may make context discovery a strong candidate, but it is selected only when its evidence can change a named decision;
- current or version-specific claims may use focused evidence research;
- real alternative trade-offs may use independent branching;
- observable claims may use execution verification;
- subjective quality may use an evaluator over an actual result;
- no task launches every worker by default, and no later review replaces pre-action judgment.

The route must not depend only on words such as "search", "reference", "recommend", or "best". Equally, it must not treat a broad task label as proof that every available module is useful.

## Non-Goals

This plugin does not guarantee parity with a stronger model, global optimality, or perfect visual quality. It does not infer an active model's capability boundary from its name or a prompt classifier; model-specific benefit must be demonstrated through calibration. It does not copy an exact retrieved artifact as a substitute for generation, authorize side effects, or install into a user-wide Claude directory. Text retrieval may expose useful adjacent principles but cannot supply a missing intrinsic capability when no usable external signal exists.

## Maintenance Rules

When reviewing or changing this plugin without the original conversation:

1. Read this file, `architecture.md`, `routing-policy.md`, and `capability-contracts.md` before changing routing or agent roles.
2. Preserve positive and negative calibration cases that test a decision rule, not a catalogue of all task types.
3. Preserve at least one case where a terse open-ended request selects useful context discovery, one where the scout explicitly skips it, and one where a fixed task remains direct.
4. Do not reintroduce a hard Stop gate that converts candidate signals into mandatory tool calls.
5. Keep `context-scout` separate from factual evidence research unless the contract and evaluation cases are deliberately redesigned together.
6. Keep the original prompt unchanged in comparisons. Separate production tests, where exact search may be allowed, from diagnostic tests, where only adjacent searches are allowed to prevent retrieval leakage.
7. Update this file and matching eval cases whenever the intended decision trade-off changes.

The current plugin Skill, agent files, hooks, and these references are the maintained implementation contract. The initial bundle and review notes are historical inputs, not active instructions.
