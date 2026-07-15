'use strict';

const CRITERIA = Object.freeze([
  Object.freeze({
    id: 'A1',
    observable: 'A readiness event that occurs before gate registration is observed as ready when the gate is registered.',
    evidence_kind: 'test'
  }),
  Object.freeze({
    id: 'A2',
    observable: 'A readiness event that occurs after gate registration resolves the gate at the readiness step.',
    evidence_kind: 'test'
  }),
  Object.freeze({
    id: 'A3',
    observable: 'Noise and duplicate readiness events preserve one stable ready terminal result.',
    evidence_kind: 'test'
  }),
  Object.freeze({
    id: 'A4',
    observable: 'Missing readiness reaches a bounded timeout and never remains pending.',
    evidence_kind: 'test'
  }),
  Object.freeze({
    id: 'A5',
    observable: 'Repeated execution of each controlled case returns identical public results.',
    evidence_kind: 'test'
  }),
  Object.freeze({
    id: 'A6',
    observable: 'A fixed-sleep control misses delayed readiness while the condition/event gate observes it.',
    evidence_kind: 'test'
  })
]);

function stableResult(value) {
  return JSON.stringify(value);
}

function runGateCase(fixtureModule, testCase, registerAt) {
  const fixture = fixtureModule.createReadinessFixture({ events: testCase.events });
  const gate = { handle: null };
  fixture.advanceTo(registerAt);
  gate.handle = fixture.waitForReady({ timeoutSteps: testCase.timeout_steps });
  fixture.advanceTo(Math.max(...testCase.events.map((event) => event.at), registerAt + testCase.timeout_steps));
  return {
    gate: gate.handle.snapshot(),
    fixture: fixture.snapshot()
  };
}

function checkA1(fixtureModule, testCase) {
  const result = runGateCase(fixtureModule, testCase, testCase.register_gate_at);
  return result.gate.status === 'ready' && result.gate.resolvedAt === 2;
}

function checkA2(fixtureModule, testCase) {
  const result = runGateCase(fixtureModule, testCase, testCase.register_gate_at);
  return result.gate.status === 'ready' && result.gate.resolvedAt === 3;
}

function checkA3(fixtureModule, testCase) {
  const result = runGateCase(fixtureModule, testCase, testCase.register_gate_at);
  return result.gate.status === 'ready'
    && result.gate.resolvedAt === 2
    && result.fixture.readinessCount === 2
    && result.gate.resolvedAt !== 3;
}

function checkA4(fixtureModule, testCase) {
  const result = runGateCase(fixtureModule, testCase, testCase.register_gate_at);
  return result.gate.status === 'timeout'
    && result.gate.resolvedAt === testCase.timeout_steps
    && result.gate.status !== 'pending';
}

function checkA5(fixtureModule, testCase) {
  const first = runGateCase(fixtureModule, testCase, testCase.register_gate_at);
  const second = runGateCase(fixtureModule, testCase, testCase.register_gate_at);
  return stableResult(first) === stableResult(second);
}

function checkA6(fixtureModule, testCase) {
  const fixture = fixtureModule.createReadinessFixture({ events: testCase.events });
  const fixedSleep = fixture.fixedSleepControl({ sleepSteps: testCase.fixed_sleep_steps });
  const gate = fixture.waitForReady({ timeoutSteps: testCase.timeout_steps });
  fixture.advanceTo(Math.max(...testCase.events.map((event) => event.at), testCase.timeout_steps));
  return fixedSleep.status === 'not-ready' && gate.status() === 'ready';
}

function criterion(id, caseIds, passed) {
  const definition = CRITERIA.find((item) => item.id === id);
  return {
    criterion_id: id,
    observable: definition.observable,
    evidence_kind: definition.evidence_kind,
    case_ids: caseIds,
    status: passed ? 'pass' : 'fail'
  };
}

function evaluate({ fixtureModule, cases, repeatCount }) {
  const byId = new Map(cases.map((testCase) => [testCase.case_id, testCase]));
  const results = [];

  results.push(criterion('A1', ['ready-before-registration'], checkA1(
    fixtureModule,
    byId.get('ready-before-registration')
  )));
  results.push(criterion('A2', ['registration-before-ready'], checkA2(
    fixtureModule,
    byId.get('registration-before-ready')
  )));
  results.push(criterion('A3', ['noise-and-duplicate-ready'], checkA3(
    fixtureModule,
    byId.get('noise-and-duplicate-ready')
  )));
  results.push(criterion('A4', ['missing-readiness'], checkA4(
    fixtureModule,
    byId.get('missing-readiness')
  )));

  let stable = true;
  for (const testCase of cases) {
    for (let repeat = 0; repeat < repeatCount; repeat += 1) {
      const result = runGateCase(fixtureModule, testCase, testCase.register_gate_at);
      if (repeat === 0) {
        testCase.firstResult = result;
      } else if (stableResult(testCase.firstResult) !== stableResult(result)) {
        stable = false;
      }
    }
    delete testCase.firstResult;
  }
  results.push(criterion('A5', cases.map((testCase) => testCase.case_id), stable));

  results.push(criterion('A6', ['delayed-readiness-negative-control'], checkA6(
    fixtureModule,
    byId.get('delayed-readiness-negative-control')
  )));

  return Object.freeze({
    criteria: Object.freeze(results),
    status: results.every((result) => result.status === 'pass') ? 'pass' : 'fail'
  });
}

module.exports = {
  API_VERSION: 'readiness-oracle-v1',
  CRITERIA,
  evaluate
};
