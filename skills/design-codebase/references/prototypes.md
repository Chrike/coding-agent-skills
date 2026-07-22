# Prototypes

Build a prototype only when a design question needs runnable feedback. Prototype code is temporary and exists to answer one question.

## Automatic Local Prototype Gate

Build the smallest local throwaway experiment needed to answer one concrete design question without another approval only when all of these are true:

- it is the fastest discriminating method for one concrete design question
- it uses only the repository's existing language, runner, and installed tooling
- before execution, the exact command and an effect inventory for its relevant transitive effects have been inspected and recorded: project scripts, package scripts, task definitions, lifecycle hooks, test setup, child processes, environment or configuration loading, and runner-created output paths are accounted for
- it adds no dependency, runtime, framework, configuration, or package installation
- it makes no network call, external-service access, external mutation, paid-resource use, or destructive data action
- it does not read, propagate, print, or persist credentials, tokens, private keys, or other sensitive environment values
- every file, directory, process, cache, log, coverage output, and other state it creates is temporary, attributable to this pass, and fully removable in the same pass
- before execution, it records a run-specific inventory of expected paths, processes, and outputs and verifies that the targets are fresh and not user-controlled
- it creates no persistent project state or durable artifact
- it stays within the requested scope and uses a unique target under a verified workspace location; it never overwrites, truncates, reuses, or deletes a pre-existing or user-controlled path

Existing project commands and executable repository scripts are not safe merely because they are already present. If the command's transitive effects, ownership, cleanup, sensitive-value handling, or workspace isolation cannot be verified, or if any effect is opaque, propose the prototype and obtain agreement before running it.

## Logic Prototype

Use for business logic, state transitions, or data shape.

- State the question at the top of the prototype.
- Use the project's existing language and task runner.
- Keep state in memory unless persistence is the question.
- Keep the core experiment easy to inspect; introduce a reusable interface only when reuse or interface shape is the question being tested. Keep terminal/browser shell throwaway.
- Surface the full relevant state after each action.
- Provide one project-local command to run it.

## UI Prototype

Use when the question is visual structure or interaction shape.

- Prefer an isolated local page or route copy for automatic experiments. Variants inside an existing page or route require the approval and tracked-file boundary below.
- Use `?variant=` or the project's equivalent to switch options.
- Create the smallest number of variants needed to answer the design question. Use multiple variants only when they represent materially different unresolved directions.
- Reuse local fixtures or already-approved read-only data paths when useful. Real network or external-service access is approval-required under the gate above, even when the path is read-only, and real mutations remain out of scope.
- Keep automatic UI experiments out of tracked application files and existing shared routes. Only use an isolated copy with a fresh owned path when it can be fully reverted without overwriting concurrent or pre-existing work; otherwise obtain agreement first.
- Remove losing variants and any switcher from the isolated prototype copy when a direction is chosen. Do not remove or rewrite variants in an existing route or tracked application file as part of automatic cleanup. Do not fold a validated decision into tracked production code as part of an automatic prototype; treat that as a separate, explicitly authorized implementation action.

## Cleanup Safety

- Remove only files, directories, processes, and outputs created by the current prototype pass and recorded as its owned artifacts.
- Never delete, truncate, reset, overwrite, or restore a pre-existing or user-controlled file as part of cleanup, including tracked, untracked, ignored, cache, or shared paths.
- Do not use broad cleanup commands such as recursive deletion against a shared or user-controlled path, `git reset --hard`, or `git checkout -- .`.
- Stop or close prototype-created processes and handles before cleanup when the tooling permits it; do not leave a server, watcher, child process, or open output running as if the prototype were fully removed.
- If cleanup fails, the process is interrupted, or ownership cannot be established, stop claiming that the prototype left no persistent state and report the exact residual paths, processes, and workspace changes. Do not rerun automatically; obtain agreement or restore a verified clean boundary first.
- Before repeating a prototype, use a fresh run-specific namespace and verify that no stale artifact, cache, process, or output from an earlier pass will be reused as current evidence.

When the question is answered, capture only the answer and why it mattered. Delete the prototype when it is isolated and owned by the current pass; folding a validated decision into real code is a separate implementation action and requires its own authorization.

Do not add tests, production polish, broad abstractions, new runtimes, or persistent infrastructure to a prototype unless that is the specific question being tested.
