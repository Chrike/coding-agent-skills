'use strict';

const fs = require('node:fs');
const path = require('node:path');

const repoRoot = path.resolve(__dirname, '..', '..');
const evalsPath = path.join(repoRoot, 'skills', 'agent-workflow', 'evals', 'evals.json');
const failures = [];
const EXPECTED_EVAL_IDS = Array.from({ length: 12 }, (_, index) => index + 1);

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

function requireNonEmptyString(value, label) {
  if (typeof value !== 'string' || value.trim() === '') {
    fail(`${label} must be a non-empty string`);
  }
}

const evalsDocument = readJson(evalsPath, 'skills/agent-workflow/evals/evals.json');
if (evalsDocument) {
  if (evalsDocument.skill_name !== 'agent-workflow') {
    fail('skill_name must be agent-workflow');
  }
  if (!Array.isArray(evalsDocument.evals)) {
    fail('evals must be an array');
  } else {
    if (evalsDocument.evals.length !== EXPECTED_EVAL_IDS.length) {
      fail(`evals must contain exactly ${EXPECTED_EVAL_IDS.length} records`);
    }

    const seenIds = new Set();
    for (const [index, evaluation] of evalsDocument.evals.entries()) {
      const label = `evals[${index}]`;
      if (!evaluation || typeof evaluation !== 'object' || Array.isArray(evaluation)) {
        fail(`${label} must be an object`);
        continue;
      }

      if (!Number.isInteger(evaluation.id)) {
        fail(`${label}.id must be an integer`);
      } else if (seenIds.has(evaluation.id)) {
        fail(`${label}.id is duplicated: ${evaluation.id}`);
      } else {
        seenIds.add(evaluation.id);
      }

      requireNonEmptyString(evaluation.prompt, `${label}.prompt`);
      requireNonEmptyString(evaluation.expected_output, `${label}.expected_output`);

      if (!Array.isArray(evaluation.assertions) || evaluation.assertions.length === 0) {
        fail(`${label}.assertions must be a non-empty array`);
      } else {
        const seenAssertions = new Set();
        for (const [assertionIndex, assertion] of evaluation.assertions.entries()) {
          const assertionLabel = `${label}.assertions[${assertionIndex}]`;
          requireNonEmptyString(assertion, assertionLabel);
          if (typeof assertion === 'string') {
            if (seenAssertions.has(assertion)) {
              fail(`${assertionLabel} is duplicated`);
            }
            seenAssertions.add(assertion);
          }
        }
      }
    }

    const actualIds = Array.from(seenIds).sort((left, right) => left - right);
    if (actualIds.length !== EXPECTED_EVAL_IDS.length
      || actualIds.some((id, index) => id !== EXPECTED_EVAL_IDS[index])) {
      fail(`eval IDs must be exactly ${EXPECTED_EVAL_IDS.join(', ')}`);
    }
  }
}

if (failures.length > 0) {
  for (const failure of failures) {
    process.stderr.write(`FAIL: ${failure}\n`);
  }
  process.exitCode = 1;
} else {
  process.stdout.write(`PASS: ${EXPECTED_EVAL_IDS.length} agent-workflow static eval records conform to the non-runtime structure contract.\n`);
}
