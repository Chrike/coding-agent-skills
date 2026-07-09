---
name: finish-branch
description: Use when the user clearly asks to commit, push, merge, discard, prepare a PR, or otherwise wrap up branch state. Keep review and completion checks in `review-and-finish`.
---

# Finish Branch

Use this when the request clearly names a branch-ending action. Clear natural-language intents like “commit these changes,” “push this branch,” “merge this,” “prepare a PR,” or “discard this work” count.

## First Decision

- If the user asks generally to finish or wrap up a branch, inspect the current branch state and present concise options.
- If the user asks for a specific branch action, perform only that action after focused safety checks.
- If the user is asking for code review or completion verification rather than a branch action, use `review-and-finish` instead.
- Do not infer commit, push, merge, discard, or PR creation from vague readiness or status questions.

## Before Options

1. Inspect git state: branch, status, and relevant diff.
2. Check whether verification is already fresh. If not, run a proportionate project-local check or state the gap.
3. Identify whether the user requested a specific action. If yes, perform only that action after safety checks.

## Options Menu

When the user asks generally to finish a branch, present concise options:

1. Keep branch as-is.
2. Commit locally.
3. Push branch.
4. Create or prepare a PR.
5. Merge locally.
6. Discard work.

Ask which option they want. Do not choose for them.

## Safety Rules

- Do not commit without explicit request and reviewed diff.
- Do not push, merge, force-push, delete, discard, or clean up worktrees without explicit confirmation.
- Require typed confirmation before destructive discard or delete.
- Preserve harness-managed or unknown worktrees.
- Prefer the shell, command style, and project-local checks already used by the repository.
- If tests fail, do not present the work as ready to merge.
