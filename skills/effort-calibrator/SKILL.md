---
name: effort-calibrator
description: Manual-only. Use when the user explicitly invokes this skill to choose, review, or recalibrate Claude or Fable `output_config.effort` settings for a concrete route, workload, eval result, latency target, or token budget. Keep ordinary implementation, generic cost-cutting, and default model behavior in the base flow.
disable-model-invocation: true
---

# Effort Calibrator

Choose or review effort settings only when the user explicitly wants an effort decision.

## First Decision

- Use this skill only when the user explicitly asks to choose, review, or recalibrate effort.
- Do not use it for ordinary implementation, ordinary review, or ordinary planning.
- Do not turn a generic complaint about cost or latency into an automatic effort change.
- Keep model selection, prompt design, and task routing in their own workflows; this skill only handles effort decisions.

## Canonical Effort Levels

For the Claude or Fable workloads this skill is meant to calibrate, use the current supported effort levels:

- `low`
- `medium`
- `high`
- `xhigh`
- `max`

Apply the setting through `output_config.effort`.

## Baseline Recommendations

Start from workload shape, not from habit:

| Workload | Start at |
| --- | --- |
| routine transforms, classification, short rewrite | `low` or `medium` |
| general analysis, writing, most app routes | `high` |
| coding, agentic, or tool-heavy work | `high`, escalating to `xhigh` for harder cases |
| only when evals still show headroom and cost is secondary | `max` |

## Review Existing Setting

Before recommending a change, identify:

- the current route or task shape
- the current effort setting
- whether the problem is latency, token cost, shallow reasoning, or over-deliberation
- whether there are evals, failure examples, or observed regressions

## Adjustment Signals

Lower effort when:

- results are already correct but the response is slower than the work warrants
- interactive latency matters more than marginal quality gains
- the model is over-deliberating before simple actions

Raise effort when:

- first-shot correctness matters more than turnaround
- failures look like shallow reasoning rather than missing information
- the workload benefits from stronger self-verification

## Recommendation Output

Keep the recommendation short and concrete:

- current setting
- recommended setting
- why
- what to verify next

## Boundaries

- Do not turn effort calibration into a default throttle policy for all work.
- Do not recommend `max` without workload-specific evidence.
- Do not use this skill to redesign prompts, pick a different model, or reroute the task into another workflow.
