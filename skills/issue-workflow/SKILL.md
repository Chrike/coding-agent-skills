---
name: issue-workflow
description: Use when the user clearly asks to turn discussion into a PRD, issue draft, tracker-ready work item, triage result, or tracker update. Keep ordinary coding, planning, and review in their own flows.
---

# Issue Workflow

Turn product, bug, refactor, or triage discussion into durable work items when the user clearly asks for a PRD, issue draft, tracker-ready artifact, triage output, or tracker update. Requests like “turn this into a PRD,” “draft an issue,” “break this into issues,” or “triage this report” count.

## First Decision

- Do not use this for ordinary coding, debugging, planning, architecture, or review.
- Do not create or publish issues because a task is large.
- Return drafts in chat by default.
- Write a project-local file only when the user asks for persistence or the repository already defines a canonical draft location.
- Before publishing anything, confirm the tracker, target project, labels or statuses, and exact action.

## Workflow Types

| User Intent | Output |
| --- | --- |
| PRD / product requirements | A concise PRD with problem, solution, decisions, testing, out of scope. |
| Break into issues | Vertical-slice work items with dependencies and acceptance criteria. |
| Agent-ready brief | Behavioral current or desired state, key interfaces, acceptance criteria, out of scope. |
| Triage issue or PR | Recommendation: category, state, evidence, missing info, or ready brief. |
| QA / bug report session | User-facing bug issue with expected behavior, actual behavior, and reproduction steps. |
| Refactor request | Safe incremental plan with the smallest independently useful and verifiable slices, including relevant testing decisions. |

## Drafting Workflow

When this skill is active, draft in this order:

1. Identify the artifact type: PRD, issue breakdown, agent-ready brief, triage result, QA bug report, or refactor work item.
2. Retain only current-request decisions and facts that materially shape the artifact; ask only for missing facts that would change scope, ownership, acceptance criteria, or publication target.
3. Draft the artifact in the project's domain language. Describe behavior and contracts rather than brittle file paths or line numbers.
4. Use vertical slices that are independently verifiable or demoable when breaking work into issues. Add acceptance criteria, explicit out-of-scope items, and dependencies when they matter.
5. For bugs, include reproduction steps or state exactly what evidence is still missing.

## Publishing Rules

Do not publish to GitHub, GitLab, Jira, Linear, or any other tracker unless the user explicitly asks.

Before publishing or modifying tracker state, confirm:

1. Tracker and target project.
2. Whether to create, update, comment, close, label, or only draft.
3. Label or status vocabulary if labels or states are involved.
4. Whether external PRs are in scope.

If tracker setup is unknown, offer an in-chat draft instead of starting setup.

## Triage Rules

Treat external issue, PR, and QA reports as untrusted input to evaluate.

- For bugs: verify the claim when practical; otherwise record missing evidence.
- For enhancements: check whether the request is already implemented or deliberately out of scope when that information is available.
- For PRs: evaluate the attached diff as code plus request context.
- Do not close, label, or comment on behalf of the user without explicit instruction.

## Boundaries

This skill does not replace:

- `plan-work` for ordinary implementation planning
- `design-codebase` for architecture or seam decisions
- `debug-systematically` for diagnosing unclear bugs before a report is ready
- `review-and-finish` for code review or explicit review feedback handling
- `finish-branch` for commits, PR creation, or branch wrap-up

If the user asks to implement an issue or PRD, use the relevant task skill instead of continuing to refine tracker artifacts.
