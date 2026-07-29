# Runtime State Schema

The project hooks maintain per-session state under the active project's `.claude/capability-harness/state/` directory. This is operational metadata, not a chain-of-thought record.

```json
{
  "schema_version": 1,
  "session_id": "string",
  "cwd": "absolute path",
  "prompt": "user prompt",
  "prompt_hash": "sha256",
  "started_at": "ISO-8601 UTC",
  "transcript_path": "absolute path",
  "transcript_offset": 0,
  "classification": {
    "substantive": true,
    "current_or_version_specific": false,
    "implementation": true,
    "visual_or_artifact": false,
    "quality_sensitive": true,
    "external_guidance": false,
    "fully_specified": false,
    "context_enrichment": false,
    "project_dependent": true,
    "high_consequence": false
  },
  "requirements": {
    "external_or_project_evidence": true,
    "project_inspection": true,
    "observable_check": true,
    "independent_branch_or_evaluation": true,
    "context_enrichment": false,
    "focused_web_guidance": false
  },
  "route": "",
  "harness": "",
  "route_reason": "",
  "stop_blocks": 0,
  "last_stop_reason": "",
  "updated_at": "ISO-8601 UTC"
}
```

`UserPromptSubmit` creates the state, `Stop` updates bounded completion evidence and any reported route fields, and old state files are pruned automatically after seven days. The prompt is retained for routing diagnostics; do not add hidden reasoning, credentials, or unrelated transcript content to the state.
