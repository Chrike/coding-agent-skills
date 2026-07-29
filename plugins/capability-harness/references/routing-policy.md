# Routing Policy

Choose the next action by the largest unresolved impact, not by a fixed task template.

## Direct path

Answer directly only when all are true:

- the task is low consequence;
- the requested information is stable and familiar;
- no project inspection is needed;
- no material alternative could change the answer;
- no executable check would add meaningful confidence.

## Context enrichment

Use context enrichment before generation or recommendation when the task is open-ended and omitted domain, structural, compositional, interaction, or medium-specific details could materially change quality. This route is based on task shape, not only explicit words such as "search", "reference", or "best".

The context scout should use a bounded sequence:

1. identify likely gaps using the subject, relationships, medium, composition, and common-failure lenses;
2. search one direct reference set;
3. search one or two component or anatomy sets;
4. search one adjacent principle, analogous case, or medium-technique set;
5. compress the result into actionable details, evidence, uncertainty, and validation cues.

Do not paste raw pages into the generation context. Do not copy an exact retrieved artifact. If exact-match retrieval could contaminate a benchmark, use adjacent-only queries in the diagnostic track.

## Acquire

Use external or project acquisition when any condition holds:

- the claim is current, version-specific, product-specific, legal, regulatory, medical, financial, security-sensitive, or otherwise consequential;
- the term, behavior, API, model property, or compatibility detail may have changed;
- the task asks for a recommendation, architecture, design, optimization, or best approach where external alternatives may materially improve quality;
- a key assumption is unsupported by the current conversation or project;
- a direct answer is unavailable but adjacent principles, analogous cases, standards, postmortems, or benchmarks could improve the decision.

Prefer project inspection before generic web guidance when repository facts control the answer. For context enrichment, WebSearch/WebFetch is normally part of the bounded Context Pack; for factual or current claims, use one focused pass with official, primary, or directly applicable sources.

## Branch

Generate 2-4 isolated alternatives when:

- more than one architecture or implementation path is plausible;
- the first viable result is not clearly superior;
- quality, maintainability, safety, performance, cost, or usability require trade-offs;
- the task is open-ended and quality matters more than mere correctness;
- a single chain is likely to anchor prematurely.

Do not branch for trivial facts, deterministic edits, or tasks with one obvious implementation under explicit constraints. A branch must change a load-bearing assumption, architecture, optimization target, or risk posture; cosmetic variants do not count.

## Execute

Execute whenever a result can be observed rather than guessed:

- run tests, compilation, type checks, linters, or static analyzers;
- reproduce the bug;
- render the interface and inspect screenshots or interaction paths;
- benchmark performance or resource use;
- calculate, simulate, or query actual data;
- inspect generated files or runtime responses.

If execution is impossible, state the specific limitation and use the strongest available substitute. Do not claim verification that did not occur.

## Evaluate

Use an independent evaluator when:

- multiple candidates pass hard constraints;
- deterministic checks do not cover an important quality dimension;
- the generator could be anchored to its own solution;
- the task involves architecture, product judgment, UX, writing quality, strategy, or other comparative judgment;
- a revision may introduce regressions.

Do not use an LLM evaluator as the sole authority for a deterministic fact. Observable checks outrank model judgment.

## Escalation budget

Apply a bounded progression:

1. inspect local context;
2. acquire one focused evidence set or run one decisive check;
3. branch into 2-4 independent alternatives if meaningful trade-offs remain;
4. evaluate real outputs;
5. perform one targeted repair;
6. repeat only when a critical check fails or new evidence materially changes the task.

Never increase agent count merely because uncertainty remains. Increase diversity of evidence or verification instead.
