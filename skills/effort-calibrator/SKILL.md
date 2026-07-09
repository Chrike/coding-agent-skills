---
name: effort-calibrator
description: Use when the user clearly asks to choose, review, or recalibrate `output_config.effort` for a specific route, workload, latency target, eval result, or token budget. Keep ordinary implementation and generic cost or latency complaints in the base flow.
---

# Effort Calibrator

Choose or review effort settings only when the user clearly asks for an effort decision. Requests like “what effort should this workload use,” “review whether this should stay at the current effort,” or “recalibrate effort for this batch” count.

## First Decision

- Use this skill only when the user clearly asks to choose, review, or recalibrate effort.
- Do not use it for ordinary implementation, ordinary review, or ordinary planning.
- Do not turn a generic complaint about cost or latency into an automatic effort change.
- Keep model selection, prompt design, and task routing in their own workflows; this skill only handles effort decisions.

## Canonical Effort Levels

For the workloads this skill is meant to calibrate, use the current supported effort levels:

- `low`
- `medium`
- `high`
- `xhigh`
- `max`

Apply the setting through `output_config.effort`.

## Review Existing Setting

Before recommending a change, identify:

- the current route or task shape
- the current effort setting
- whether the problem is latency, token cost, shallow reasoning, or over-deliberation
- whether there are evals, failure examples, or observed regressions

## Recommendation Output

Keep the recommendation short and concrete:

- current setting
- recommended setting
- why
- what to verify next

Use [baseline-workloads.md](references/baseline-workloads.md) for example workload-to-effort starting points when the direct request does not already fix the answer.

## Boundaries

- Do not turn effort calibration into a default throttle policy for all work.
- Do not recommend `max` without workload-specific evidence.
- Do not use this skill to redesign prompts, pick a different model, or reroute the task into another workflow.
