# Agent Role Index

Detailed contracts are split by stable role:

- [Investigator](investigator.md)
- [Verifier](verifier.md)
- [Findings reviewer](reviewer.md)

These checks maintain independent project Agent boundaries. They are not runtime instructions and do not decide routing.

Saved Agent selection is host/version-dependent. Read-only Workflows use the built-in `Explore` role when saved-Agent resolution fails; they do not fall back to an unrestricted generic worker. Selector availability is not a security boundary; host permissions and explicit tool restrictions remain authoritative.
