# Simplify Protected Blocks

An explicit opt-in Claude Code plugin for keeping marked implementation blocks out of a bounded simplify read/edit flow.

## Install

Install this plugin only when the project intentionally wants protected-block behavior. Installing it enables its hooks for that host project; standalone skills and the host `/code-simplify` command remain unchanged.

The hooks require Python 3.9 or later on `PATH`. They use only the Python standard library and do not call a shell, network service, dependency manager, or external tool.

## Mark a block

```js
/* simplify-ignore-start: perf-critical */
const unrolled = computeFastPath(input);
/* simplify-ignore-end */
```

The `Read` hook replaces marked blocks with a hash placeholder while retaining a project-local backup. The `Edit` and `Write` hooks restore the protected blocks before applying the change and filter them again. The `Stop` hook restores active backups.

## Boundaries

- Only regular files inside `CLAUDE_PROJECT_DIR` are eligible.
- Symlinks, paths outside the project root, cache paths, malformed payloads, and unknown hook events are ignored.
- State is stored under `.claude/.simplify-protected-blocks`; add that path to the project ignore policy if the plugin is enabled.
- A missing or moved original is recovered as a sibling `.recovered` file inside the project root; the plugin never writes outside that root.
- A hook failure is fail-open for the host operation. Static source and local tests do not prove the host's event payload, ordering, or runtime isolation.
- This plugin does not authorize code changes, commits, cleanup, deletion, or a `/code-simplify` invocation.

## Recovery

If a session ends without the `Stop` event, start an authorized recovery invocation for this plugin or run its `stop` hook entry with the project root selected. Inspect recovered files before replacing or deleting anything. Do not delete the cache while backup state remains.
