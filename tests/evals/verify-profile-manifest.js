'use strict';

const fs = require('node:fs');
const path = require('node:path');

const repoRoot = path.resolve(__dirname, '..', '..');
const manifestPath = path.join(repoRoot, 'profiles', 'manifest.json');
const failures = [];
const EXPECTED_PROFILES = ['fast', 'quality', 'lab'];
const EXPECTED_SKILLS = [
  'debug-systematically',
  'test-strategy',
  'review-and-finish',
  'agent-workflow',
  'plan-work',
  'design-codebase',
  'reliability-check',
  'finish-branch',
  'issue-workflow',
  'memory-handoff',
  'markdown-memory',
  'skill-refactorer',
  'decision-map',
];
const EXPECTED_FAST = ['debug-systematically', 'test-strategy', 'review-and-finish'];

function fail(message) {
  failures.push(message);
}

function sameArray(actual, expected) {
  return Array.isArray(actual)
    && actual.length === expected.length
    && actual.every((value, index) => value === expected[index]);
}

function exactSet(actual, expected, label) {
  const sortedActual = Array.isArray(actual) ? [...new Set(actual)].sort() : null;
  const sortedExpected = [...expected].sort();
  if (!sortedActual || actual.length !== expected.length || JSON.stringify(sortedActual) !== JSON.stringify(sortedExpected)) {
    fail(`${label} must contain exactly ${sortedExpected.join(', ')}`);
  }
}

function readManifest() {
  try {
    return JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
  } catch (error) {
    fail(`manifest: ${error.message}`);
    return null;
  }
}

function sourceExists(relativePath) {
  const absolute = path.resolve(repoRoot, relativePath);
  const relative = path.relative(repoRoot, absolute);
  return !relative.startsWith('..') && !path.isAbsolute(relative) && fs.existsSync(absolute);
}

const manifest = readManifest();
if (manifest) {
  if (manifest.$schema !== 'coding-agent-skills-profile-manifest-v1') {
    fail('manifest $schema is invalid');
  }
  if (manifest.schema_version !== 'profile-manifest-v1') {
    fail('manifest schema_version is invalid');
  }
  if (manifest.status !== 'non-runtime-distribution-metadata') {
    fail('manifest must remain non-runtime distribution metadata');
  }
  if (manifest.runtime_routing !== false || manifest.lifecycle_automation !== false || manifest.outcome_claims !== 'none') {
    fail('manifest must disable routing, lifecycle automation, and outcome claims');
  }
  if (manifest.recommended_default !== 'quality') {
    fail('quality must be the sole recommended default');
  }
  if (manifest.kernel?.source !== 'prompts/CLAUDE.fragment.md'
    || manifest.kernel?.installation !== 'manual-assembly'
    || manifest.kernel?.automatic_write !== false
    || manifest.kernel?.destination !== 'CLAUDE.md') {
    fail('kernel must remain manual assembly metadata and must not write CLAUDE.md automatically');
  }
  for (const root of ['tests', 'evals', 'profiles', 'governance', 'archive']) {
    if (!manifest.non_installable_roots?.includes(root)) {
      fail(`non_installable_roots is missing ${root}`);
    }
  }
  if (!sourceExists(manifest.kernel.source)) {
    fail(`kernel source is missing: ${manifest.kernel.source}`);
  }

  const skillNames = Object.keys(manifest.skill_sources || {});
  exactSet(skillNames, EXPECTED_SKILLS, 'skill_sources');
  for (const [skillName, entry] of Object.entries(manifest.skill_sources || {})) {
    if (!sourceExists(entry.source)) {
      fail(`${skillName}: source does not exist: ${entry.source}`);
    }
    const expectedRuntimePaths = sourceExists(path.join(entry.source, 'references'))
      ? ['SKILL.md', 'references']
      : ['SKILL.md'];
    if (!sameArray(entry.runtime_paths, expectedRuntimePaths)) {
      fail(`${skillName}: runtime_paths must be exactly ${expectedRuntimePaths.join(' and ')}`);
    }
    if (entry.source.includes('tests') || entry.source.includes('evals') || entry.source.includes('profiles')) {
      fail(`${skillName}: source points into a non-runtime tree`);
    }
    if (!sourceExists(path.join(entry.source, 'SKILL.md'))) {
      fail(`${skillName}: SKILL.md is missing`);
    }
  }

  exactSet(Object.keys(manifest.profiles || {}), EXPECTED_PROFILES, 'profiles');
  const profileSkills = Object.fromEntries(EXPECTED_PROFILES.map((name) => [name, manifest.profiles?.[name]?.skills]));
  exactSet(profileSkills.fast, EXPECTED_FAST, 'fast.skills');
  exactSet(profileSkills.quality, EXPECTED_SKILLS, 'quality.skills');
  exactSet(profileSkills.lab, EXPECTED_SKILLS, 'lab.skills');
  if (!sameArray(manifest.profiles?.fast?.workflows, [])) {
    fail('fast must not include workflows');
  }
  if (!sameArray(manifest.profiles?.quality?.workflows, [])) {
    fail('quality must not include workflows');
  }
  if (!sameArray(manifest.profiles?.lab?.workflows, ['adaptive-long-horizon'])) {
    fail('lab must include only adaptive-long-horizon');
  }
  if (manifest.profiles?.lab?.workflow_visibility !== 'explicit-only') {
    fail('lab workflow visibility must be explicit-only');
  }

  const workflow = manifest.workflow_sources?.['adaptive-long-horizon'];
  if (!workflow || workflow.source !== 'experiments/workflows/adaptive-long-horizon.js'
    || workflow.destination !== 'workflows/adaptive-long-horizon.js'
    || workflow.visibility !== 'explicit-only'
    || workflow.lifecycle !== 'frozen-lab'
    || !sourceExists(workflow.source)) {
    fail('adaptive workflow source/destination/lifecycle contract is invalid');
  }
  if (manifest.profiles?.fast?.workflow_visibility !== 'none' || manifest.profiles?.quality?.workflow_visibility !== 'none') {
    fail('fast and quality must not expose workflows');
  }
}

if (failures.length > 0) {
  for (const failure of failures) {
    process.stderr.write(`FAIL: ${failure}\n`);
  }
  process.exitCode = 1;
} else {
  process.stdout.write('PASS: Fast, Quality, and Lab profiles conform to the non-runtime distribution contract.\n');
}
