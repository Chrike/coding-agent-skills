'use strict';

const path = require('node:path');
const { spawnSync } = require('node:child_process');

const repoRoot = path.resolve(__dirname, '..', '..');
const checks = [
  'verify-experiment-layout.js',
  'verify-evidence-loop-reference.js',
  'verify-profile-manifest.js',
  'verify-profile-installer.js',
  'verify-lifecycle-policy.js',
  'verify-scenario-seeds.js',
  'verify-scn-tm-test-pos-001-readiness.js',
  'verify-blocked-invalid-semantics.js',
];

for (const check of checks) {
  process.stdout.write(`RUN: ${check}\n`);
  const result = spawnSync(process.execPath, [path.join(__dirname, check)], {
    cwd: repoRoot,
    encoding: 'utf8',
  });
  if (result.stdout) {
    process.stdout.write(result.stdout);
  }
  if (result.stderr) {
    process.stderr.write(result.stderr);
  }
  if (result.status !== 0) {
    process.stderr.write(`FAIL: repository boundary check stopped at ${check}\n`);
    process.exitCode = result.status || 1;
    break;
  }
}

if (!process.exitCode) {
  process.stdout.write(`PASS: ${checks.length} repository boundary checks passed without runtime or lifecycle execution.\n`);
}
