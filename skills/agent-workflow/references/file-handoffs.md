# File Handoffs

Use this after `agent-workflow` is already active when prompts or reports would become too long for clean controller-to-agent exchange.

## Priority

Use these handoffs in this order:

1. Prefer dynamic workflow script variables or other host-managed intermediate state when the active execution substrate already provides them.
2. Keep raw long output inside the producing subagent or other local execution context when no other step needs the full text.
3. Use a project-local ignored scratch file only when the controller or another slice must reread or reuse the raw output.
4. Return only condensed findings to the main conversation.

## Good uses

Use project-local files for:

- task briefs with exact requirements and ownership
- reports with findings, evidence, confidence, open issues, changed paths, commands, and recommended next action
- review notes with controller decisions, checkpoints, and unresolved items

## Controller rules

- use an existing ignored temporary or scratch location when available
- prefer project-local scratch paths that are easy to remove
- do not create tracked documentation merely to exchange transient agent data
- scratch handoffs are not durable project memory
- have the controller read and condense the artifact instead of forwarding it raw
- when another active slice may need exact rereading, carry the supported claim with a pointer to the full evidence, its producer scope, and the relevant code or state version
- dereference the full evidence only when the current decision needs exact detail, the condensed claim is disputed, or the evidence may be stale
- remove transient handoff files after integration unless another active slice still needs them
- do not create a handoff file when the result is already short enough to pass directly
- this pattern owns only transient handoff state
- do not create durable notes here
- when the user asks for a checkpoint, compression-safe handoff, or durable resume state, use `memory-handoff`
