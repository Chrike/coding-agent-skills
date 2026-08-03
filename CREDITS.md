# External Source Credits

## `using-agent-skills`

- Source: `addyosmani/agent-skills`, skill `using-agent-skills`.
- License basis: GNU AGPL v3, following the source repository's `LICENSE`.
- Reference: https://github.com/addyosmani/agent-skills
- Retained in this suite: the idea that skill selection should use the smallest clearly matching workflow and preserve explicit ownership boundaries; surface only material assumptions; and state concrete technical tradeoffs with a workable alternative.
- Not retained: SessionStart injection, a second global meta-router, a mandatory full-lifecycle chain, a universal Definition-of-Done gate, or target-specific sibling handoffs. Those conflict with this suite's lightweight default, maintained routing contract, host-owned boundaries, and action-specific authorization.
