# Evaluation Policy

## Evaluation order

1. reject candidates that violate hard constraints;
2. compare observable verification results;
3. compare directly applicable evidence;
4. compare quality dimensions derived from the user's goal;
5. expose unresolved preference trade-offs instead of inventing a universal optimum.

## Quality dimensions

Derive only dimensions relevant to the task. Common dimensions include correctness, completeness, maintainability, performance, security, usability, accessibility, coherence, clarity, originality, operational risk, reversibility, and total complexity.

Do not reward extra features, verbosity, abstraction, or visual decoration unless they advance the objective.

## Capability-Decision Evaluation

Keep the original user prompt unchanged. Evaluate the decision itself before judging a generated artifact:

- direct generation without the harness;
- a pre-action decision that selects no augmentation;
- a pre-action decision that selects one bounded capability action;
- a stronger-model result only as an upper baseline, not as hidden prompt content.

Each calibration case tests one decision rule, such as whether current evidence, local inspection, context discovery, observable execution, or an independent alternative can materially alter the result. It is not a taxonomy of all possible tasks. Run the same cases separately for each model whose behavior matters; the Hook does not infer model-specific thresholds at runtime. Use a production track when exact task search is allowed and a diagnostic track that forbids exact-match retrieval. The diagnostic track measures whether discovery changes a decision rather than copying an existing answer. Evaluate the actual rendered or executed artifact against the original hard constraints and any plan implications that the selected capability returned. Evaluation is optional and is not a prerequisite for a search-based Decision Brief.

## Judge controls

- keep the evaluator isolated from the generator's internal justification;
- present candidate artifacts in neutral labels;
- randomize or reverse candidate order when practical;
- require evidence for each high-impact criticism;
- distinguish confirmed defects, plausible risks, and personal preference;
- use at least two independent judgments only when subjective stakes justify the cost;
- when judgments conflict, inspect the criteria and evidence instead of majority voting automatically.

## Preserve-best acceptance rule

A revision replaces the current best only if all are true:

- no hard constraint regresses;
- no critical observable check regresses;
- at least one confirmed high-impact defect improves;
- no more severe new defect appears;
- the comparison uses the same relevant criteria.

Otherwise retain or restore the previous best. The evaluator is advisory; the controller owns integration.

## Completion rule

Finalize when:

- all hard constraints pass;
- available critical checks have run;
- important claims are supported or explicitly uncertain;
- no unresolved high-impact conflict remains;
- another capability call is unlikely to change an important decision or result.
