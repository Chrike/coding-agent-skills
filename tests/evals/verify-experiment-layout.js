'use strict';

const fs = require('node:fs');
const path = require('node:path');

const repoRoot = path.resolve(__dirname, '..', '..');
const failures = [];

function fail(message) {
  failures.push(message);
}

function exists(relativePath) {
  return fs.existsSync(path.join(repoRoot, relativePath));
}

function read(relativePath) {
  try {
    return fs.readFileSync(path.join(repoRoot, relativePath), 'utf8');
  } catch (error) {
    fail(`${relativePath}: ${error.message}`);
    return '';
  }
}

function collectAdaptiveSources(directory) {
  const root = path.join(repoRoot, directory);
  if (!fs.existsSync(root)) {
    return [];
  }

  const found = [];
  const visit = (current) => {
    for (const entry of fs.readdirSync(current, { withFileTypes: true })) {
      const entryPath = path.join(current, entry.name);
      if (entry.isDirectory()) {
        visit(entryPath);
      } else if (entry.name === 'adaptive-long-horizon.js') {
        found.push(path.relative(repoRoot, entryPath).replace(/\\/g, '/'));
      }
    }
  };
  visit(root);
  return found;
}

const expectedSource = 'experiments/workflows/adaptive-long-horizon.js';
if (!exists(expectedSource)) {
  fail(`missing canonical adaptive source: ${expectedSource}`);
}
if (exists('workflows/adaptive-long-horizon.js')) {
  fail('old adaptive source path still exists');
}
if (!exists('experiments/README.md')) {
  fail('missing experiments/README.md');
}

const sources = collectAdaptiveSources('experiments');
if (sources.length !== 1 || sources[0] !== expectedSource) {
  fail(`experiments must contain exactly one adaptive source at ${expectedSource}`);
}

const readme = read('experiments/README.md');
for (const requiredText of [
  'explicit-only',
  'session-local',
  'read-only',
  'bounded',
  'frozen Lab',
  'not a host sandbox',
  'not evidence that adaptive improves outcomes'
]) {
  if (!readme.includes(requiredText)) {
    fail(`experiments/README.md is missing boundary text: ${requiredText}`);
  }
}

const source = read(expectedSource);
if (source.includes('process.env') || source.includes('fs.writeFile')) {
  fail('adaptive source contains an unexpected direct write/environment marker');
}

if (failures.length > 0) {
  for (const failure of failures) {
    process.stderr.write(`FAIL: ${failure}\n`);
  }
  process.exitCode = 1;
} else {
  process.stdout.write('PASS: adaptive has one frozen Lab source and explicit non-runtime boundaries.\n');
}
