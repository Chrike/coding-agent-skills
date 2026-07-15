'use strict';

const fs = require('node:fs');
const path = require('node:path');

const repoRoot = path.resolve(__dirname, '..', '..');
const failures = [];

function fail(message) {
  failures.push(message);
}

function read(relativePath) {
  try {
    return fs.readFileSync(path.join(repoRoot, relativePath), 'utf8');
  } catch (error) {
    fail(`${relativePath}: ${error.message}`);
    return '';
  }
}

const skill = read('skills/agent-workflow/SKILL.md');
const reference = read('skills/agent-workflow/references/evidence-loop.md');

if (!skill.includes('[evidence-loop.md](references/evidence-loop.md)')) {
  fail('agent-workflow SKILL.md must directly link evidence-loop.md');
}
for (const requiredText of [
  'candidate evidence',
  'fresh-context verifier',
  'minimal material carry-forward',
  'contradictions',
  'bounded stop condition',
  'leaf workers',
  'verifier verifies'
]) {
  if (!reference.includes(requiredText)) {
    fail(`evidence-loop reference is missing: ${requiredText}`);
  }
}
for (const forbiddenText of [
  'automatic router',
  'lifecycle controller',
  'adaptive-long-horizon.js',
  'function normalizeInput',
  'const DEFAULT_LIMITS'
]) {
  if (reference.includes(forbiddenText)) {
    fail(`evidence-loop reference must not duplicate adaptive/runtime content: ${forbiddenText}`);
  }
}

if (failures.length > 0) {
  for (const failure of failures) {
    process.stderr.write(`FAIL: ${failure}\n`);
  }
  process.exitCode = 1;
} else {
  process.stdout.write('PASS: evidence-loop principles have one on-demand agent-workflow reference.\n');
}
