# Design Intent

## Purpose

Capability Harness is a pre-action capability amplifier for models that can complete a task but may fail to surface domain
context, salience, quality details, or useful evidence before acting. Its primary purpose is to turn missing context into a
compact decision brief, not to add agents or repairs after the model has already anchored on a weak result.

Given the same terse user request, the project-scoped workflow may identify a plausible missing signal, obtain bounded
domain context, compress it into plan implications, and then let the active domain method generate or implement. The user
should not need to write a hidden domain checklist into the prompt.

For prompt profiles with a strong pre-action signal, the hook names the default next route rather than leaving every request as an equally weak suggestion. The active controller executes that one route before material work. This is intentionally different from a Stop gate: it does not require every capability, retry a completed result, or turn route candidates into a checklist.

## Illustrative Decision Profile (Non-normative)

For a terse open-ended artifact request, a decision-first pass may identify a missing structural, compositional, interaction,
or medium-specific signal and use direct, component, and adjacent research to inform one named construction decision. If no
plausible bounded context gap exists, it can be skipped. This profile does not create a domain-specific workflow or imply
that every artifact task needs search. It is a communication example, not a routing rule or an automated task test.

## Routing Intent

- fixed, fully specified, low-consequence work may remain direct;
- open-ended or unfamiliar work may make context discovery a strong candidate when missing context can materially improve a named decision;
- current or version-specific claims may use focused evidence research;
- real alternative trade-offs may use independent branching;
- observable claims may use execution verification;
- subjective quality may use an evaluator over an actual result;
- no task launches every worker by default, and no later review replaces pre-action judgment.

The route must not depend only on words such as "search", "reference", "recommend", or "best". Equally, it must not treat a broad task label as proof that every available module is useful.

## Non-Goals

This plugin does not guarantee parity with a stronger model, global optimality, or perfect visual quality. It does not infer an active model's capability boundary from its name or a prompt classifier; optional calibration can show where a model benefits from the route. It does not copy an exact retrieved artifact as a substitute for generation, authorize side effects, or install into a user-wide Claude directory. Text retrieval may expose useful adjacent principles but cannot supply a missing intrinsic capability when no usable external signal exists.

## Maintenance Rules

When reviewing or changing this plugin without the original conversation:

1. Read this file, `architecture.md`, `routing-policy.md`, and `capability-contracts.md` before changing routing or agent roles.
2. Preserve positive and negative calibration cases that test a decision rule, not a catalogue of all task types.
3. Preserve at least one case where a terse open-ended request selects useful context discovery, one where the scout explicitly skips it, and one where a fixed task remains direct.
4. Do not reintroduce a hard Stop gate that converts every candidate signal into a mandatory tool call. A narrow route selected before material work remains distinct from a post-hoc completion gate.
5. Keep `context-scout` separate from factual evidence research unless the contract and evaluation cases are deliberately redesigned together.
6. Keep the original prompt unchanged in comparisons. Separate production tests, where exact search may be allowed, from diagnostic tests, where only adjacent searches are allowed to prevent retrieval leakage.
7. Update this file and matching eval cases whenever the intended decision trade-off changes.

Do not weaken a hook-selected strong route back into a generic candidate reminder without deliberately changing this intent and its calibration cases.

The current plugin Skill, agent files, hooks, and these references are the maintained implementation contract. The initial bundle and review notes are historical inputs, not active instructions.
