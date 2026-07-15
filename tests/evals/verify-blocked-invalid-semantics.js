'use strict';

const fs = require('node:fs');
const path = require('node:path');

const manifestPath = path.join(__dirname, 'blocked-invalid-semantics.json');
const failures = [];

const TERMINAL_STATUSES = new Set(['completed', 'blocked', 'invalid']);
const METRIC_STATUSES = new Set([
  'measured',
  'not_collected',
  'not_applicable',
  'unavailable',
  'invalid'
]);
const ADVISORY_STATUSES = new Set(['blocked', 'inconclusive', 'retain-current']);
const FORBIDDEN_ACTIONS = new Set([
  'promotion',
  'demotion',
  'archive',
  'install',
  'profile',
  'routing',
  'path',
  'git'
]);
const REASON_SPECS = Object.freeze({
  'prerequisite-unavailable': Object.freeze({ status: 'blocked', attempted: false }),
  'critical-field-unverifiable': Object.freeze({ status: 'blocked', attempted: false }),
  'contract-field-missing': Object.freeze({ status: 'invalid', attempted: true }),
  'provenance-mismatch': Object.freeze({ status: 'invalid', attempted: true }),
  'pairing-mismatch': Object.freeze({ status: 'invalid', attempted: true }),
  'environment-mismatch': Object.freeze({ status: 'invalid', attempted: true }),
  'metric-wrapper-invalid': Object.freeze({ status: 'invalid', attempted: true }),
  'terminal-semantics-ambiguous': Object.freeze({ status: 'invalid', attempted: null })
});
const CRITICAL_PROVENANCE_FIELDS = Object.freeze([
  'scenario_revision',
  'prompt_sha256',
  'acceptance_oracle_hash',
  'source_revision',
  'skill_reference_revision',
  'installed_copy_identity',
  'model_provider_version',
  'host_runtime_version',
  'environment_id',
  'tool_policy_revision',
  'profile_id',
  'workspace_state_id'
]);
const METRIC_WRAPPER_KEYS = Object.freeze(['reason', 'status', 'unit', 'value']);
const TERMINAL_FIELD_REGISTRY = Object.freeze([
  '/prerequisites/acceptance_oracle',
  '/prerequisites/host_substrate',
  '/provenance_observed/host_runtime_version',
  '/provenance_observed/source_revision',
  '/provenance_observed/environment_id',
  '/contract/acceptance_oracle_ref',
  '/metrics/tokens_total/status',
  '/metrics/tokens_total/value'
]);
const TOP_LEVEL_KEYS = Object.freeze([
  '$schema',
  'schema_version',
  'status',
  'mode',
  'execution_mode',
  'actual_execution',
  'ab_comparison',
  'runtime_installable',
  'outcome_claims',
  'record_kind',
  'forbidden_capabilities',
  'execution_policy',
  'forbidden_actions',
  'advisory_status',
  'critical_provenance_fields',
  'terminal_field_registry',
  'frozen_provenance',
  'records',
  'paired_sets',
  'expected'
]);

function fail(message) {
  failures.push(message);
}

function isObject(value) {
  return value !== null && typeof value === 'object' && !Array.isArray(value);
}

function readManifest() {
  try {
    return JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
  } catch (error) {
    fail(`manifest: ${error.message}`);
    return null;
  }
}

function sameArray(actual, expected) {
  return Array.isArray(actual)
    && actual.length === expected.length
    && actual.every((value, index) => value === expected[index]);
}

function exactKeys(value, expected, label) {
  if (!isObject(value)) {
    fail(`${label} must be an object`);
    return;
  }
  const actual = Object.keys(value).sort();
  const sortedExpected = [...expected].sort();
  if (!sameArray(actual, sortedExpected)) {
    fail(`${label} must contain exactly ${sortedExpected.join(', ')}`);
  }
}

function canonicalJson(value) {
  if (Array.isArray(value)) {
    return value.map(canonicalJson);
  }
  if (isObject(value)) {
    return Object.fromEntries(
      Object.entries(value)
        .sort(([left], [right]) => left.localeCompare(right))
        .map(([key, item]) => [key, canonicalJson(item)])
    );
  }
  return value;
}

function pointerTokens(pointer, label) {
  if (typeof pointer !== 'string' || !pointer.startsWith('/') || pointer.includes('~2')) {
    fail(`${label} must be an absolute JSON Pointer`);
    return null;
  }
  return pointer.slice(1).split('/').map((token) => token.replace(/~1/g, '/').replace(/~0/g, '~'));
}

function pointerTarget(record, pointer, label) {
  const tokens = pointerTokens(pointer, label);
  if (!tokens) {
    return { exists: false, value: undefined };
  }
  let current = record;
  for (let index = 0; index < tokens.length - 1; index += 1) {
    const token = tokens[index];
    if ((isObject(current) || Array.isArray(current)) && Object.prototype.hasOwnProperty.call(current, token)) {
      current = current[token];
    } else {
      fail(`${label} points through a missing parent: ${pointer}`);
      return { exists: false, value: undefined };
    }
  }
  const finalToken = tokens[tokens.length - 1];
  if (!isObject(current) && !Array.isArray(current)) {
    fail(`${label} points through a non-container: ${pointer}`);
    return { exists: false, value: undefined };
  }
  return {
    exists: Object.prototype.hasOwnProperty.call(current, finalToken),
    value: current[finalToken]
  };
}

function hasAttempted(record) {
  if (typeof record.execution_attempted !== 'boolean' || typeof record.collection_attempted !== 'boolean') {
    fail(`${record.record_id}: execution_attempted and collection_attempted must be booleans`);
    return null;
  }
  return record.execution_attempted || record.collection_attempted;
}

function validateMetricWrapper(wrapper, label, allowInvalidWrapper) {
  if (!isObject(wrapper)) {
    fail(`${label} must be a metric wrapper object`);
    return false;
  }
  const actualKeys = Object.keys(wrapper).sort();
  const expectedKeys = [...METRIC_WRAPPER_KEYS].sort();
  if (!sameArray(actualKeys, expectedKeys)) {
    fail(`${label} must contain exactly ${expectedKeys.join(', ')}`);
  }
  let valid = actualKeys.length === expectedKeys.length && sameArray(actualKeys, expectedKeys);
  if (!METRIC_STATUSES.has(wrapper.status)) {
    valid = false;
  }
  if (typeof wrapper.unit !== 'string' || wrapper.unit.trim() === '') {
    valid = false;
  }
  if (typeof wrapper.reason !== 'string' || wrapper.reason.trim() === '') {
    valid = false;
  }
  if (wrapper.status === 'measured') {
    if (typeof wrapper.value !== 'number' || !Number.isFinite(wrapper.value) || wrapper.value < 0) {
      valid = false;
    }
  } else if (wrapper.value !== null) {
    valid = false;
  }
  if (allowInvalidWrapper && wrapper.status === 'measured' && wrapper.value === null) {
    valid = false;
  }
  return valid;
}

function validateMetrics(record) {
  if (!isObject(record.metrics) || Object.keys(record.metrics).length === 0) {
    fail(`${record.record_id}: metrics must be a non-empty object`);
    return { valid: false, invalidPointers: [] };
  }
  const invalidPointers = [];
  for (const [metricName, wrapper] of Object.entries(record.metrics)) {
    const valid = validateMetricWrapper(wrapper, `${record.record_id}.metrics.${metricName}`);
    if (!valid) {
      invalidPointers.push(`/metrics/${metricName}/status`, `/metrics/${metricName}/value`);
    }
  }
  return { valid: invalidPointers.length === 0, invalidPointers };
}

function validateTerminalFields(record) {
  if (!Array.isArray(record.terminal_fields)) {
    fail(`${record.record_id}: terminal_fields must be an array`);
    return;
  }
  const fields = record.terminal_fields;
  if (!sameArray(fields, [...new Set(fields)].sort())) {
    fail(`${record.record_id}: terminal_fields must be unique and sorted`);
  }
  if (fields.includes('/terminal_reason')) {
    fail(`${record.record_id}: terminal_fields cannot hide the cause behind /terminal_reason`);
  }
  if (record.terminal_status === 'completed') {
    if (fields.length !== 0) {
      fail(`${record.record_id}: completed record must have no terminal_fields`);
    }
    return;
  }
  if (fields.length === 0) {
    fail(`${record.record_id}: non-completed record must have terminal_fields`);
  }
  for (const pointer of fields) {
    pointerTarget(record, pointer, `${record.record_id}.terminal_fields`);
    if (!TERMINAL_FIELD_REGISTRY.includes(pointer)) {
      fail(`${record.record_id}: terminal field is not a registered run-schema pointer: ${pointer}`);
    }
  }
}

function validateProvenance(record, frozen) {
  if (record.provenance_ref !== 'frozen-provenance-v1') {
    fail(`${record.record_id}: provenance_ref must identify the frozen synthetic provenance`);
  }
  if (!isObject(record.provenance_observed)) {
    fail(`${record.record_id}: provenance_observed must be an object`);
    return;
  }
  for (const field of CRITICAL_PROVENANCE_FIELDS) {
    if (!Object.prototype.hasOwnProperty.call(record.provenance_observed, field)) {
      fail(`${record.record_id}: missing critical provenance field ${field}`);
    }
  }
  const mismatches = CRITICAL_PROVENANCE_FIELDS.filter((field) => (
    record.provenance_observed[field] !== frozen[field]
  ));
  if (record.terminal_reason_code === 'provenance-mismatch' && mismatches.length === 0) {
    fail(`${record.record_id}: provenance-mismatch must identify an observed mismatch`);
  }
  if (!['provenance-mismatch', 'pairing-mismatch'].includes(record.terminal_reason_code)
    && record.terminal_status !== 'blocked'
    && mismatches.length > 0) {
    fail(`${record.record_id}: unexpected provenance mismatch in ${mismatches.join(', ')}`);
  }
}

function validateRecord(record, frozen, expectedOutcome) {
  if (!isObject(record)) {
    fail('each record must be an object');
    return;
  }
  if (typeof record.record_id !== 'string' || record.record_id.length === 0) {
    fail('each record must have a non-empty record_id');
    return;
  }
  if (!TERMINAL_STATUSES.has(record.terminal_status)) {
    fail(`${record.record_id}: invalid terminal_status`);
    return;
  }
  const attempted = hasAttempted(record);
  const spec = record.terminal_status === 'completed'
    ? null
    : REASON_SPECS[record.terminal_reason_code];
  if (record.terminal_status !== 'completed' && !spec) {
    fail(`${record.record_id}: terminal_reason_code is not in the fixed registry`);
  }
  if (spec && spec.status !== record.terminal_status) {
    fail(`${record.record_id}: reason code ${record.terminal_reason_code} does not match terminal_status`);
  }
  if (spec && spec.attempted !== null && attempted !== spec.attempted) {
    fail(`${record.record_id}: attempt boundary does not match ${record.terminal_reason_code}`);
  }
  if (record.terminal_status !== 'completed') {
    if (typeof record.terminal_reason !== 'string' || record.terminal_reason.trim() === '') {
      fail(`${record.record_id}: non-completed record needs a non-empty terminal_reason`);
    }
    if (record.record_preserved !== true) {
      fail(`${record.record_id}: non-completed record must be preserved`);
    }
  } else if (record.record_preserved !== true) {
    fail(`${record.record_id}: completed record must also be preserved`);
  }
  validateTerminalFields(record);
  validateProvenance(record, frozen);
  const metricResult = validateMetrics(record);
  if (record.terminal_reason_code === 'metric-wrapper-invalid') {
    if (metricResult.invalidPointers.length === 0) {
      fail(`${record.record_id}: metric-wrapper-invalid must contain an invalid wrapper`);
    } else if (!metricResult.invalidPointers.every((pointer) => record.terminal_fields.includes(pointer))) {
      fail(`${record.record_id}: metric wrapper pointers must be terminal_fields`);
    }
  } else if (!metricResult.valid) {
    fail(`${record.record_id}: invalid metric wrapper requires metric-wrapper-invalid`);
  }
  if (!expectedOutcome) {
    fail(`${record.record_id}: missing expected record outcome`);
  } else {
    const actualOutcome = {
      terminal_status: record.terminal_status,
      terminal_reason_code: record.terminal_reason_code ?? null,
      terminal_fields: record.terminal_fields
    };
    if (JSON.stringify(actualOutcome) !== JSON.stringify(expectedOutcome)) {
      fail(`${record.record_id}: actual terminal outcome differs from expected synthetic outcome`);
    }
  }
}

function validatePair(pair, recordsById, expectedOutcome) {
  if (!isObject(pair)) {
    fail('each paired set must be an object');
    return;
  }
  if (!Array.isArray(pair.member_ids) || pair.member_ids.length === 0) {
    fail(`${pair.paired_set_id}: member_ids must be non-empty`);
    return;
  }
  const members = pair.member_ids.map((id) => recordsById.get(id));
  if (members.some((member) => !member)) {
    fail(`${pair.paired_set_id}: every member_id must reference a preserved record`);
    return;
  }
  if (members.some((member) => member.paired_set_id !== pair.paired_set_id)) {
    fail(`${pair.paired_set_id}: every member record must declare the same paired_set_id`);
  }
  const invalid = members.find((member) => member.terminal_status === 'invalid');
  const blocked = members.find((member) => member.terminal_status === 'blocked');
  const derivedStatus = invalid ? 'invalid' : blocked ? 'blocked' : 'completed';
  const derivedMember = invalid || blocked;
  const derivedCode = derivedMember?.terminal_reason_code ?? null;
  if (pair.terminal_status !== derivedStatus || (pair.terminal_reason_code ?? null) !== derivedCode) {
    fail(`${pair.paired_set_id}: paired terminal status/code do not propagate from members`);
  }
  if (pair.record_preserved !== true) {
    fail(`${pair.paired_set_id}: paired set must be preserved`);
  }
  if (!Array.isArray(pair.terminal_fields) || pair.terminal_fields.length === 0) {
    fail(`${pair.paired_set_id}: propagated paired set needs terminal_fields`);
  } else {
    for (const pointer of pair.terminal_fields) {
      if (!/^\/members\/[^/]+\/(terminal_status|terminal_reason_code|terminal_fields|provenance_observed\/environment_id)$/.test(pointer)) {
        fail(`${pair.paired_set_id}: invalid paired propagation pointer ${pointer}`);
      }
    }
  }
  if (!expectedOutcome || pair.terminal_status !== expectedOutcome.terminal_status
    || (pair.terminal_reason_code ?? null) !== expectedOutcome.terminal_reason_code) {
    fail(`${pair.paired_set_id}: paired outcome differs from expected synthetic outcome`);
  }
}

function verify(manifest) {
  if (!manifest) {
    return;
  }
  exactKeys(manifest, TOP_LEVEL_KEYS, 'manifest');
  if (manifest.$schema !== 'outcome-evaluation-v1-blocked-invalid-semantics') {
    fail('manifest $schema is invalid');
  }
  if (manifest.schema_version !== 'blocked-invalid-semantics-v1') {
    fail('manifest schema_version is invalid');
  }
  if (manifest.status !== 'synthetic-metadata-only'
    || manifest.mode !== 'metadata-only-conformance-v1'
    || manifest.execution_mode !== 'synthetic-metadata-only'
    || manifest.record_kind !== 'synthetic-metadata-case') {
    fail('manifest must remain metadata-only synthetic conformance');
  }
  if (manifest.actual_execution !== false
    || manifest.ab_comparison !== 'not_applicable'
    || manifest.runtime_installable !== false
    || manifest.outcome_claims !== 'none') {
    fail('manifest must not execute, install, compare arms, or make outcome claims');
  }
  const expectedCapabilities = [
    'model_execution',
    'host_routing',
    'skill_activation',
    'three_arm_ab',
    'cost_telemetry',
    'lifecycle_action'
  ];
  if (!sameArray([...new Set(manifest.forbidden_capabilities || [])].sort(), [...expectedCapabilities].sort())
    || manifest.forbidden_capabilities.length !== expectedCapabilities.length) {
    fail('forbidden_capabilities must be the exact metadata-only denylist');
  }
  exactKeys(manifest.execution_policy, [
    'model_provider_execution',
    'host_runtime_routing',
    'skill_activation',
    'workspace_mutation',
    'ab_arm_execution',
    'telemetry_collection',
    'retries',
    'lifecycle_writes'
  ], 'execution_policy');
  for (const [key, value] of Object.entries(manifest.execution_policy || {})) {
    if (value !== false) {
      fail(`execution_policy.${key} must remain false`);
    }
  }
  exactKeys(manifest.forbidden_actions, [...FORBIDDEN_ACTIONS], 'forbidden_actions');
  for (const action of FORBIDDEN_ACTIONS) {
    if (manifest.forbidden_actions?.[action] !== false) {
      fail(`forbidden action ${action} must remain rejected`);
    }
  }
  if (!ADVISORY_STATUSES.has(manifest.advisory_status) || manifest.advisory_status !== 'inconclusive') {
    fail('advisory_status must remain inconclusive for metadata-only conformance');
  }
  if (!Array.isArray(manifest.critical_provenance_fields)
    || !sameArray(manifest.critical_provenance_fields, [...CRITICAL_PROVENANCE_FIELDS])) {
    fail('critical_provenance_fields must match the frozen provenance registry in stable order');
  }
  if (!Array.isArray(manifest.terminal_field_registry)
    || !sameArray(manifest.terminal_field_registry, [...TERMINAL_FIELD_REGISTRY])) {
    fail('terminal_field_registry must match the frozen canonical pointer registry in stable order');
  }
  if (manifest.terminal_field_registry.some((pointer) => !pointer.startsWith('/'))) {
    fail('terminal_field_registry must contain only root-relative JSON pointers');
  }
  if (!isObject(manifest.frozen_provenance)) {
    fail('frozen_provenance must be an object');
  }
  if (manifest.execution_mode !== 'synthetic-metadata-only' || manifest.actual_execution !== false) {
    fail('execution_mode and actual_execution must prove metadata-only non-execution');
  }
  if (manifest.ab_comparison !== 'not_applicable') {
    fail('ab_comparison must remain not_applicable');
  }

  const records = Array.isArray(manifest.records) ? manifest.records : [];
  if (!Array.isArray(manifest.records)) {
    fail('records must be an array');
  }
  const recordsById = new Map();
  for (const record of records) {
    if (recordsById.has(record?.record_id)) {
      fail(`duplicate record_id: ${record.record_id}`);
    }
    if (record?.record_id) {
      recordsById.set(record.record_id, record);
    }
    validateRecord(record, manifest.frozen_provenance, manifest.expected?.record_outcomes?.[record?.record_id]);
  }
  const expectedRecordIds = manifest.expected?.preserved_record_ids || [];
  if (!sameArray([...recordsById.keys()].sort(), [...expectedRecordIds].sort())) {
    fail('all and only expected record IDs must be preserved');
  }
  for (const id of expectedRecordIds) {
    if (recordsById.get(id)?.record_preserved !== true) {
      fail(`${id}: expected preserved record is absent or not marked record_preserved`);
    }
  }

  const memberPairCounts = new Map();
  const pairs = Array.isArray(manifest.paired_sets) ? manifest.paired_sets : [];
  if (!Array.isArray(manifest.paired_sets)) {
    fail('paired_sets must be an array');
  }
  const pairsById = new Map();
  for (const pair of pairs) {
    if (pairsById.has(pair?.paired_set_id)) {
      fail(`duplicate paired_set_id: ${pair.paired_set_id}`);
    }
    if (pair?.paired_set_id) {
      pairsById.set(pair.paired_set_id, pair);
    }
    for (const memberId of pair?.member_ids || []) {
      memberPairCounts.set(memberId, (memberPairCounts.get(memberId) || 0) + 1);
    }
    validatePair(pair, recordsById, manifest.expected?.paired_outcomes?.[pair?.paired_set_id]);
  }
  for (const record of records) {
    if (memberPairCounts.get(record.record_id) !== 1) {
      fail(`${record.record_id}: every preserved record must belong to exactly one paired set`);
    }
  }
  const expectedPairIds = manifest.expected?.preserved_paired_set_ids || [];
  if (!sameArray([...pairsById.keys()].sort(), [...expectedPairIds].sort())) {
    fail('all and only expected paired-set IDs must be preserved');
  }
  for (const id of expectedPairIds) {
    if (pairsById.get(id)?.record_preserved !== true) {
      fail(`${id}: expected preserved paired set is absent or not marked record_preserved`);
    }
  }

  const expectedAggregate = manifest.expected?.aggregate;
  const recordCounts = records.reduce((counts, record) => {
    counts[record.terminal_status] += 1;
    return counts;
  }, { completed: 0, blocked: 0, invalid: 0 });
  const pairCounts = pairs.reduce((counts, pair) => {
    counts[pair.terminal_status] += 1;
    return counts;
  }, { completed: 0, blocked: 0, invalid: 0 });
  const countReasons = (items) => {
    const counts = items.reduce((result, item) => {
      if (item.terminal_status !== 'completed') {
        result[item.terminal_reason_code] = (result[item.terminal_reason_code] || 0) + 1;
      }
      return result;
    }, {});
    return Object.fromEntries(Object.entries(counts).sort(([left], [right]) => left.localeCompare(right)));
  };
  const aggregate = {
    record_total: records.length,
    record_complete_denominator: recordCounts.completed,
    outcome_denominator: 0,
    record_blocked: recordCounts.blocked,
    record_invalid: recordCounts.invalid,
    record_attrition: recordCounts.blocked + recordCounts.invalid,
    raw_run_reason_counts: countReasons(records),
    paired_set_total: pairs.length,
    paired_set_complete_denominator: pairCounts.completed,
    paired_set_blocked: pairCounts.blocked,
    paired_set_invalid: pairCounts.invalid,
    paired_set_attrition: pairCounts.blocked + pairCounts.invalid,
    paired_set_reason_counts: countReasons(pairs),
    advisory_status: manifest.advisory_status
  };
  if (JSON.stringify(canonicalJson(aggregate)) !== JSON.stringify(canonicalJson(expectedAggregate))) {
    fail(`aggregate counts differ: expected ${JSON.stringify(canonicalJson(expectedAggregate))}, got ${JSON.stringify(canonicalJson(aggregate))}`);
  }
}

const manifest = readManifest();
verify(manifest);

if (failures.length > 0) {
  process.stderr.write(`${JSON.stringify({ status: 'fail', failures }, null, 2)}\n`);
  process.exitCode = 1;
} else {
  process.stdout.write(`${JSON.stringify({
    status: 'pass',
    mode: 'metadata-only-conformance-v1',
    record_count: manifest.records.length,
    paired_set_count: manifest.paired_sets.length,
    advisory_status: manifest.advisory_status,
    outcome_claims: manifest.outcome_claims
  }, null, 2)}\n`);
}
