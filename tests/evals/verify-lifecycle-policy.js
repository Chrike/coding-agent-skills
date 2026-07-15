'use strict';

const fs = require('node:fs');
const path = require('node:path');

const repoRoot = path.resolve(__dirname, '..', '..');
const policyPath = path.join(repoRoot, 'governance', 'lifecycle-policy.json');
const archivePath = path.join(repoRoot, 'archive', 'README.md');
const failures = [];
const EXPECTED_ADVISORY = [
  'blocked',
  'candidate-for-human-review',
  'inconclusive',
  'retain-current',
];
const EXPECTED_PREREQUISITES = [
  'real-product-task-specification',
  'independent-pre-frozen-acceptance-oracle',
  'immutable-task-harness',
  'verifiable-host-provider-tool-policy-contract',
  'fresh-session-context-workspace-isolation',
  'provenance-and-attempt-metadata',
  'provider-backed-telemetry',
  'pinned-pricing-source-and-version',
];

function fail(message) {
  failures.push(message);
}

function sameSet(actual, expected, label) {
  const left = Array.isArray(actual) ? [...new Set(actual)].sort() : null;
  const right = [...expected].sort();
  if (!left || actual.length !== expected.length || JSON.stringify(left) !== JSON.stringify(right)) {
    fail(`${label} must contain exactly ${right.join(', ')}`);
  }
}

let policy;
try {
  policy = JSON.parse(fs.readFileSync(policyPath, 'utf8'));
} catch (error) {
  fail(`policy: ${error.message}`);
}

if (policy) {
  if (policy.$schema !== 'coding-agent-skills-lifecycle-policy-v1' || policy.schema_version !== 'lifecycle-policy-v1') {
    fail('policy schema is invalid');
  }
  if (policy.status !== 'blocked-awaiting-product-task-and-harness') {
    fail('policy must remain blocked until the real task and harness exist');
  }
  if (policy.runtime_installable !== false || policy.outcome_claims !== 'none' || policy.automatic_lifecycle_actions !== false) {
    fail('policy must remain non-runtime, outcome-free, and non-automatic');
  }
  sameSet(policy.allowed_advisory_statuses, EXPECTED_ADVISORY, 'allowed advisory statuses');
  sameSet(policy.required_recovery_prerequisites, EXPECTED_PREREQUISITES, 'required recovery prerequisites');
  const future = policy.first_future_execution;
  if (future?.scenario_count !== 1 || future?.provider_count !== 1 || future?.host_count !== 1
    || JSON.stringify(future.comparison) !== JSON.stringify(['base-only', 'baseline', 'candidate'])
    || future.mode !== 'advisory-only-smoke-proof' || future.lifecycle_action !== 'none') {
    fail('first future execution must remain one scenario/provider/host advisory-only smoke proof');
  }
  if (policy.maintainer_review_required !== true) {
    fail('maintainer review must remain required');
  }
  for (const [action, enabled] of Object.entries(policy.automatic_actions || {})) {
    if (enabled !== false) {
      fail(`automatic action must be disabled: ${action}`);
    }
  }
}

let archive;
try {
  archive = fs.readFileSync(archivePath, 'utf8');
} catch (error) {
  fail(`archive README: ${error.message}`);
}
if (archive) {
  for (const requiredText of ['No assets are currently archived', 'non-runtime', 'decision-grade evidence', 'maintainer approval']) {
    if (!archive.includes(requiredText)) {
      fail(`archive README is missing: ${requiredText}`);
    }
  }
}

function inspectRuntimeFiles(relativePath) {
  const absolute = path.join(repoRoot, relativePath);
  if (!fs.existsSync(absolute)) {
    return;
  }
  const stat = fs.lstatSync(absolute);
  if (stat.isSymbolicLink()) {
    fail(`runtime source must not be a symlink: ${relativePath}`);
    return;
  }
  if (stat.isFile()) {
    if (fs.readFileSync(absolute, 'utf8').includes('lifecycle-policy.json')) {
      fail(`runtime source must not reference lifecycle policy: ${relativePath}`);
    }
    return;
  }
  if (!stat.isDirectory()) {
    fail(`runtime source must be a file or directory: ${relativePath}`);
    return;
  }
  for (const entry of fs.readdirSync(absolute, { withFileTypes: true })) {
    inspectRuntimeFiles(path.join(relativePath, entry.name));
  }
}

for (const runtimePath of [
  'prompts/CLAUDE.fragment.md',
  'skills',
  'experiments/workflows/adaptive-long-horizon.js',
]) {
  inspectRuntimeFiles(runtimePath);
}

if (failures.length > 0) {
  for (const failure of failures) {
    process.stderr.write(`FAIL: ${failure}\n`);
  }
  process.exitCode = 1;
} else {
  process.stdout.write('PASS: lifecycle governance is blocked, advisory-only, non-runtime, and archive-empty.\n');
}
