'use strict';

const VALID_EVENT_TYPES = new Set(['noise', 'ready']);

function assertInteger(value, label, minimum = 0) {
  if (!Number.isInteger(value) || value < minimum) {
    throw new TypeError(`${label} must be an integer >= ${minimum}`);
  }
}

function normalizeEvents(events) {
  if (!Array.isArray(events)) {
    throw new TypeError('events must be an array');
  }

  return events.map((event, index) => {
    if (!event || typeof event !== 'object') {
      throw new TypeError(`events[${index}] must be an object`);
    }
    assertInteger(event.at, `events[${index}].at`, 1);
    if (!VALID_EVENT_TYPES.has(event.type)) {
      throw new TypeError(`events[${index}].type must be noise or ready`);
    }
    return Object.freeze({ at: event.at, type: event.type, order: index });
  });
}

function createReadinessFixture({ events }) {
  const normalizedEvents = normalizeEvents(events);
  const gates = [];
  let currentStep = 0;
  let nextEventIndex = 0;
  let readinessCount = 0;
  let noiseCount = 0;
  let firstReadyAt = null;

  function updateGate(gate) {
    if (gate.status !== 'pending') {
      return;
    }

    if (firstReadyAt !== null) {
      gate.status = 'ready';
      gate.resolvedAt = firstReadyAt;
    } else if (currentStep >= gate.deadline) {
      gate.status = 'timeout';
      gate.resolvedAt = gate.deadline;
    }
  }

  function deliverEventsAt(step) {
    while (nextEventIndex < normalizedEvents.length && normalizedEvents[nextEventIndex].at === step) {
      const event = normalizedEvents[nextEventIndex];
      nextEventIndex += 1;
      if (event.type === 'ready') {
        readinessCount += 1;
        if (firstReadyAt === null) {
          firstReadyAt = step;
        }
      } else {
        noiseCount += 1;
      }
    }
  }

  function advanceTo(step) {
    assertInteger(step, 'step');
    if (step < currentStep) {
      throw new RangeError('step must not move backwards');
    }

    for (let nextStep = currentStep + 1; nextStep <= step; nextStep += 1) {
      currentStep = nextStep;
      deliverEventsAt(currentStep);
      for (const gate of gates) {
        updateGate(gate);
      }
    }

    return snapshot();
  }

  function waitForReady({ timeoutSteps }) {
    assertInteger(timeoutSteps, 'timeoutSteps');
    const gate = {
      registeredAt: currentStep,
      deadline: currentStep + timeoutSteps,
      status: 'pending',
      resolvedAt: null
    };
    gates.push(gate);
    updateGate(gate);

    return Object.freeze({
      status() {
        updateGate(gate);
        return gate.status;
      },
      snapshot() {
        updateGate(gate);
        return Object.freeze({
          registeredAt: gate.registeredAt,
          deadline: gate.deadline,
          status: gate.status,
          resolvedAt: gate.resolvedAt
        });
      }
    });
  }

  function fixedSleepControl({ sleepSteps }) {
    assertInteger(sleepSteps, 'sleepSteps');
    advanceTo(currentStep + sleepSteps);
    return Object.freeze({
      status: firstReadyAt === null ? 'not-ready' : 'ready',
      snapshot: snapshot()
    });
  }

  function snapshot() {
    return Object.freeze({
      currentStep,
      readinessObserved: firstReadyAt !== null,
      readinessCount,
      noiseCount,
      firstReadyAt,
      processedEvents: nextEventIndex
    });
  }

  return Object.freeze({
    advanceTo,
    waitForReady,
    fixedSleepControl,
    snapshot
  });
}

module.exports = {
  API_VERSION: 'readiness-fixture-v1',
  createReadinessFixture
};
