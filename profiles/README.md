# Distribution Profiles

Profiles are non-runtime distribution metadata. They select repository-owned skills and explicit Lab workflow sources for a user-selected host target; they do not change natural-language routing, host policy, provider identity, or outcome evidence.

The manifest is at `profiles/manifest.json`. `quality` is the policy default, not an empirical quality claim. `lab` is explicit-only and carries the frozen adaptive pilot; it is not automatically routed or installed by `fast` or `quality`.

## Explicit installation

The dependency-free installer requires an explicit target root and is dry-run by default:

```text
node scripts/install-profile.js --profile quality --target-root <host-.claude-root>
node scripts/install-profile.js --profile quality --target-root <host-.claude-root> --apply
node scripts/install-profile.js --profile lab --target-root <host-.claude-root> --apply
```

Use `--force` only when intentionally replacing a differing file owned by the selected profile. The installer preflights the complete plan, never deletes or cleans files, and leaves unrelated target files untouched. A differing existing file fails by default.

The target root should be the selected `.claude` runtime root. The installer copies selected skills to `<target-root>/skills/` and an explicit Lab workflow to `<target-root>/workflows/`. It does not write or assemble `CLAUDE.md`; assemble `prompts/CLAUDE.fragment.md` into the host instruction system separately.

The installer never copies `tests/`, `tests/evals/`, `profiles/`, `governance/`, `archive/`, host settings, or the Kernel fragment. It does not prove host enforcement, provider identity, worker isolation, or product outcome benefit.
