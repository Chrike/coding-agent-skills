'use strict';

const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');

const repoRoot = path.resolve(__dirname, '..', '..');
const manifestPath = path.join(__dirname, 'scn-tm-test-pos-001-readiness.json');
const seedPath = path.join(__dirname, 'scenario-seeds.json');
const EXPECTED_SEED_ID = 'SCN-TM-TEST-POS-001';
const BASELINE_REVISION = '9a0318a05962fe1ca5d83e946f8a7cb0d42921bf';
const EXPECTED_CASE_IDS = new Set([
  'ready-before-registration',
  'registration-before-ready',
  'noise-and-duplicate-ready',
  'missing-readiness',
  'delayed-readiness-negative-control'
]);
const EXPECTED_FORBIDDEN_CAPABILITIES = new Set([
  'model_execution',
  'host_routing',
  'three_arm_ab',
  'cost_telemetry',
  'lifecycle_action'
]);
const failures = [];

function fail(message) {
  failures.push(message);
}

function readJson(filePath, label) {
  try {
    return JSON.parse(fs.readFileSync(filePath, 'utf8'));
  } catch (error) {
    fail(`${label}: ${error.message}`);
    return null;
  }
}

function sha256(value) {
  return crypto.createHash('sha256').update(value, 'utf8').digest('hex');
}

function fileSha256(filePath, label) {
  try {
    const content = fs.readFileSync(filePath, 'utf8').replace(/\r\n/g, '\n');
    return sha256(content);
  } catch (error) {
    fail(`${label}: ${error.message}`);
    return null;
  }
}

function resolveRepoPath(relativePath, label) {
  if (typeof relativePath !== 'string' || relativePath.length === 0) {
    fail(`${label} must be a non-empty relative path`);
    return null;
  }
  const resolved = path.resolve(repoRoot, relativePath);
  const relativeToRoot = path.relative(repoRoot, resolved);
  if (relativeToRoot.startsWith('..') || path.isAbsolute(relativeToRoot)) {
    fail(`${label} must remain inside the repository`);
    return null;
  }
  return resolved;
}

function assertExactSet(actual, expected, label) {
  const actualSet = Array.isArray(actual) ? new Set(actual) : null;
  if (!actualSet || actual.length !== expected.size || actualSet.size !== expected.size || actual.some((value) => !expected.has(value))) {
    fail(`${label} must contain exactly: ${Array.from(expected).join(', ')}`);
  }
}

function verifyManifest(manifest, seeds) {
  if (!manifest) {
    return;
  }
  if (manifest.$schema !== 'outcome-evaluation-v1-readiness-self-check') {
    fail('manifest $schema is invalid');
  }
  if (manifest.schema_version !== 'readiness-self-check-v1') {
    fail('manifest schema_version is invalid');
  }
  if (manifest.mode !== 'fixture-oracle-readiness-only') {
    fail('manifest mode must remain fixture-oracle-readiness-only');
  }
  if (manifest.runtime_installable !== false) {
    fail('readiness slice must not be runtime-installable');
  }
  if (manifest.outcome_claims !== 'none') {
    fail('readiness slice must not make outcome claims');
  }
  if (!Number.isInteger(manifest.slice_revision) || manifest.slice_revision < 1) {
    fail('slice_revision must be a positive integer');
  }
  if (!Number.isInteger(manifest.repeat_count) || manifest.repeat_count < 1) {
    fail('repeat_count must be a positive integer');
  }

  const seedRef = manifest.seed_ref;
  const seed = seeds?.records?.find((record) => record.scenario_id === EXPECTED_SEED_ID);
  if (!seed) {
    fail(`seed corpus is missing ${EXPECTED_SEED_ID}`);
  }
  if (seedRef?.path !== 'tests/evals/scenario-seeds.json') {
    fail('seed_ref.path must point to scenario-seeds.json');
  }
  if (seedRef?.scenario_id !== EXPECTED_SEED_ID) {
    fail(`seed_ref.scenario_id must be ${EXPECTED_SEED_ID}`);
  }
  if (seedRef?.scenario_revision !== 1 || seed?.scenario_revision !== 1) {
    fail('seed scenario_revision must remain 1');
  }
  if (seedRef?.source_revision !== BASELINE_REVISION || seed?.source?.revision !== BASELINE_REVISION) {
    fail('seed source revision must remain the pinned baseline');
  }
  if (seedRef?.prompt_sha256 !== seed?.prompt_sha256) {
    fail('seed_ref.prompt_sha256 does not match the static seed');
  }
  if (seed?.seed_status !== 'static-seed'
    || seed?.outcome_status !== 'unmeasured'
    || seed?.outcome_execution_eligible !== false
    || typeof seed?.eligible_for_routing_screen !== 'boolean') {
    fail('referenced seed must remain static, unmeasured, routing-screen-only, and outcome-ineligible');
  }
  if (seed?.acceptance_oracle?.status !== 'blocked'
    || seed?.acceptance_oracle?.available !== false
    || seed?.acceptance_oracle?.independence_required !== true) {
    fail('referenced seed oracle must remain blocked, unavailable, and independence-required');
  }

  const fixturePath = resolveRepoPath(manifest.fixture?.path, 'fixture.path');
  const oraclePath = resolveRepoPath(manifest.oracle?.path, 'oracle.path');
  if (fixturePath && manifest.fixture.sha256 !== fileSha256(fixturePath, 'fixture hash')) {
    fail('fixture.sha256 does not match the fixture file');
  }
  if (oraclePath && manifest.oracle.sha256 !== fileSha256(oraclePath, 'oracle hash')) {
    fail('oracle.sha256 does not match the oracle file');
  }
  if (manifest.oracle?.fixture_behavior_only !== true) {
    fail('oracle.fixture_behavior_only must remain true');
  }
  if (manifest.oracle?.public_fixture_api_only !== true) {
    fail('oracle.public_fixture_api_only must remain true');
  }

  const cases = manifest.cases;
  if (!Array.isArray(cases)) {
    fail('cases must be an array');
  } else {
    const caseIds = cases.map((testCase) => testCase?.case_id);
    assertExactSet(caseIds, EXPECTED_CASE_IDS, 'case IDs');
    for (const testCase of cases) {
      if (!testCase || typeof testCase !== 'object') {
        fail('each case must be an object');
        continue;
      }
      if (!Array.isArray(testCase.events) || testCase.events.length === 0) {
        fail(`${testCase.case_id}: events must be non-empty`);
        continue;
      }
      let previousAt = 0;
      for (const event of testCase.events) {
        if (!Number.isInteger(event?.at) || event.at < 1 || event.at < previousAt) {
          fail(`${testCase.case_id}: events must use non-decreasing positive steps`);
        }
        if (!['noise', 'ready'].includes(event?.type)) {
          fail(`${testCase.case_id}: event type must be noise or ready`);
        }
        previousAt = event?.at;
      }
      for (const field of ['register_gate_at', 'timeout_steps']) {
        if (!Number.isInteger(testCase[field]) || testCase[field] < 0) {
          fail(`${testCase.case_id}: ${field} must be a non-negative integer`);
        }
      }
    }
  }
  assertExactSet(manifest.forbidden_capabilities, EXPECTED_FORBIDDEN_CAPABILITIES, 'forbidden_capabilities');

  if (oraclePath) {
    try {
      const oracleModule = require(oraclePath);
      if (manifest.oracle?.revision !== oracleModule.API_VERSION) {
        fail('oracle revision does not match oracle API_VERSION');
      }
      if (!Array.isArray(oracleModule.CRITERIA) || oracleModule.CRITERIA.length === 0) {
        fail('oracle must export non-empty CRITERIA');
      } else if (manifest.oracle.criteria_sha256 !== sha256(JSON.stringify(oracleModule.CRITERIA))) {
        fail('oracle.criteria_sha256 does not match the frozen oracle criteria');
      }
    } catch (error) {
      fail(`oracle module: ${error.message}`);
    }
  }
}

const manifest = readJson(manifestPath, 'readiness manifest');
const seeds = readJson(seedPath, 'scenario-seeds.json');
verifyManifest(manifest, seeds);

if (failures.length > 0) {
  const report = {
    slice_status: 'blocked',
    reason: 'readiness manifest or static seed conformance failed',
    failures
  };
  process.stderr.write(`${JSON.stringify(report, null, 2)}\n`);
  process.exitCode = 1;
} else {
  const fixturePath = path.resolve(repoRoot, manifest.fixture.path);
  const oraclePath = path.resolve(repoRoot, manifest.oracle.path);
  try {
    const fixtureModule = require(fixturePath);
    const oracleModule = require(oraclePath);
    if (manifest.fixture.revision !== fixtureModule.API_VERSION) {
      throw new Error('fixture revision does not match fixture API_VERSION');
    }
    if (typeof fixtureModule.createReadinessFixture !== 'function') {
      throw new Error('fixture must export createReadinessFixture');
    }
    if (typeof oracleModule.evaluate !== 'function') {
      throw new Error('oracle must export evaluate');
    }
    const cases = JSON.parse(JSON.stringify(manifest.cases));
    const result = oracleModule.evaluate({
      fixtureModule,
      cases,
      repeatCount: manifest.repeat_count
    });
    const report = {
      slice_status: result.status,
      mode: manifest.mode,
      slice_id: manifest.slice_id,
      fixture_revision: manifest.fixture.revision,
      oracle_revision: manifest.oracle.revision,
      repeat_count: manifest.repeat_count,
      criteria: result.criteria,
      outcome_claims: manifest.outcome_claims
    };
    process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
    if (result.status !== 'pass') {
      process.exitCode = 1;
    }
  } catch (error) {
    process.stderr.write(`${JSON.stringify({
      slice_status: 'blocked',
      reason: error.message
    }, null, 2)}\n`);
    process.exitCode = 1;
  }
}
