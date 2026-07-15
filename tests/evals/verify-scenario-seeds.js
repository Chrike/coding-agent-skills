const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');

const BASELINE_REVISION = '9a0318a05962fe1ca5d83e946f8a7cb0d42921bf';
const EXPECTED_SCENARIO_IDS = new Set([
  'SCN-TM-DEBUG-POS-001',
  'SCN-TM-TEST-POS-001',
  'SCN-TM-AGENT-POS-001',
  'SCN-TM-BASE-NEG-001',
  'SCN-NT-AGENT-NEG-001',
  'SCN-AW-STATIC-001'
]);

const repoRoot = path.resolve(__dirname, '..', '..');
const seedPath = path.join(__dirname, 'scenario-seeds.json');
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

function sourcePathFor(record) {
  return path.join(repoRoot, record.source.path);
}

function verifyMarkdownSource(record, content) {
  const match = /^.*row (\d+)$/.exec(record.source.locator);
  if (!match) {
    fail(`${record.scenario_id}: markdown locator must end with a numeric row`);
    return;
  }

  const lineNumber = Number(match[1]);
  const lines = content.split(/\r?\n/);
  const line = lines[lineNumber - 1];
  if (!line || !line.includes(record.prompt_fixture)) {
    fail(`${record.scenario_id}: source ${record.source.path}:${lineNumber} does not contain the prompt fixture`);
  }
}

function verifyEvalSource(record, content) {
  if (record.source.locator !== 'evals[0]') {
    fail(`${record.scenario_id}: unsupported eval locator ${record.source.locator}`);
    return;
  }

  const source = readJson(sourcePathFor(record), record.source.path);
  const prompt = source?.evals?.[0]?.prompt;
  if (prompt !== record.prompt_fixture) {
    fail(`${record.scenario_id}: evals[0].prompt does not match the prompt fixture`);
  }
}

const seeds = readJson(seedPath, 'scenario-seeds.json');
if (!seeds) {
  process.exitCode = 1;
} else {
  if (seeds.$schema !== 'outcome-evaluation-v1-scenario-seed') {
    fail('top-level $schema is not the scenario-seed schema');
  }
  if (seeds.schema_version !== 'outcome-evaluation-v1') {
    fail('top-level schema_version is not outcome-evaluation-v1');
  }
  if (seeds.status !== 'static-seed-only') {
    fail('top-level status must remain static-seed-only');
  }
  if (seeds.source_revision !== BASELINE_REVISION) {
    fail(`top-level source_revision must be ${BASELINE_REVISION}`);
  }
  if (seeds.runtime_installable !== false) {
    fail('scenario seeds must not be runtime-installable');
  }
  if (seeds.outcome_claims !== 'none') {
    fail('scenario seeds must not make outcome claims');
  }
  if (!Array.isArray(seeds.records)) {
    fail('records must be an array');
  } else {
    const seen = new Set();

    for (const record of seeds.records) {
      if (!record || typeof record !== 'object') {
        fail('each record must be an object');
        continue;
      }

      const id = record.scenario_id;
      if (typeof id !== 'string' || id.length === 0) {
        fail('each record must have a non-empty scenario_id');
      } else if (seen.has(id)) {
        fail(`${id}: duplicate scenario_id`);
      } else {
        seen.add(id);
      }

      if (record.scenario_revision !== 1) {
        fail(`${id}: scenario_revision must be 1 for the initial seed corpus`);
      }
      if (record.source?.revision !== BASELINE_REVISION) {
        fail(`${id}: source revision must match the pinned baseline`);
      }
      if (record.seed_status !== 'static-seed') {
        fail(`${id}: seed_status must remain static-seed`);
      }
      if (record.outcome_status !== 'unmeasured') {
        fail(`${id}: outcome_status must remain unmeasured`);
      }
      if (record.acceptance_oracle?.status !== 'blocked') {
        fail(`${id}: acceptance oracle must remain blocked until an independent oracle exists`);
      }
      if (record.acceptance_oracle?.independent !== true) {
        fail(`${id}: acceptance oracle must explicitly state independent=true`);
      }
      if (typeof record.prompt_fixture !== 'string' || record.prompt_fixture.length === 0) {
        fail(`${id}: prompt_fixture must be non-empty`);
      }
      if (record.prompt_sha256 !== sha256(record.prompt_fixture)) {
        fail(`${id}: prompt_sha256 does not match prompt_fixture`);
      }
      if (!record.source?.path || !record.source?.locator) {
        fail(`${id}: source path and locator are required`);
        continue;
      }

      const sourcePath = sourcePathFor(record);
      if (!fs.existsSync(sourcePath)) {
        fail(`${id}: source file does not exist: ${record.source.path}`);
        continue;
      }

      const sourceContent = fs.readFileSync(sourcePath, 'utf8');
      if (record.source.path.endsWith('.md')) {
        verifyMarkdownSource(record, sourceContent);
      } else if (record.source.path.endsWith('.json')) {
        verifyEvalSource(record, sourceContent);
      } else {
        fail(`${id}: unsupported source type: ${record.source.path}`);
      }
    }

    for (const expectedId of EXPECTED_SCENARIO_IDS) {
      if (!seen.has(expectedId)) {
        fail(`expected initial seed is missing: ${expectedId}`);
      }
    }
    for (const actualId of seen) {
      if (!EXPECTED_SCENARIO_IDS.has(actualId)) {
        fail(`unexpected scenario in initial seed corpus: ${actualId}`);
      }
    }
  }
}

if (failures.length > 0) {
  for (const failure of failures) {
    process.stderr.write(`FAIL: ${failure}\n`);
  }
  process.exitCode = 1;
} else {
  process.stdout.write(`PASS: ${EXPECTED_SCENARIO_IDS.size} static scenario seeds conform to the pinned source and unmeasured-outcome contract.\n`);
}
