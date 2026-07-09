# Baseline Workloads

Use this only after `effort-calibrator` is already active and the user has not already fixed the answer through explicit constraints.

## Starting points

| Workload shape | Start at |
| --- | --- |
| routine transforms, classification, short rewrite | `low` or `medium` |
| general analysis, writing, most app routes | `high` |
| coding, agentic, or tool-heavy work | `high`, escalating to `xhigh` for harder cases |
| only when evals still show headroom and cost is secondary | `max` |

## Adjustment signals

Lower effort when:

- results are already correct but the response is slower than the work warrants
- interactive latency matters more than marginal quality gains
- the model is over-deliberating before simple actions

Raise effort when:

- first-shot correctness matters more than turnaround
- failures look like shallow reasoning rather than missing information
- the workload benefits from stronger self-verification

## Boundaries

- Do not treat this table as a default policy for all work.
- Do not override direct user constraints on effort, latency, or budget.
- Do not use this note to redesign prompts, switch models, or reroute the task.
