# File Handoffs

Use this after `agent-workflow` is already active when prompts or reports would become too long for clean controller-to-agent exchange.

## Priority

Use these handoffs in this order:

1. Keep raw long output inside the producing subagent or other local execution context when no other step needs the full text.
2. Use a project-local scratch file only when the controller or another slice must reread or reuse the raw output.
3. Return only condensed findings to the main conversation.

## Good uses

Use project-local files for:

- task briefs with exact requirements and ownership
- reports with findings, evidence, confidence, open issues, changed paths, commands, and recommended next action
- review notes with controller decisions, checkpoints, and unresolved items

## Controller rules

- prefer project-local scratch paths that are easy to remove
- when intermediate context would pollute the active conversation, prefer scratch files for long briefs, scout reports, long reports, or batch verification output
- have the controller read and condense the artifact instead of forwarding it raw
- create durable notes only when the work is long-running, likely to hit context compression, or the user asks
