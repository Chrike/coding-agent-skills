export const meta = {
  name: 'adaptive-long-horizon',
  description: 'Run a bounded, read-only, session-local evidence loop for an explicitly supplied task',
}

const DEFAULT_LIMITS = Object.freeze({
  maxRounds: 3,
  maxAgents: 8,
  noProgressLimit: 2,
})

const EVIDENCE_ITEM = {
  type: 'object',
  properties: {
    path: { type: 'string' },
    version: { type: 'string' },
    detail: { type: 'string' },
  },
  required: ['path', 'version', 'detail'],
  additionalProperties: false,
}

const INVESTIGATION_RESULT = {
  type: 'object',
  properties: {
    status: { enum: ['evidence', 'blocker', 'complete'] },
    conclusion: { type: 'string' },
    evidence: {
      type: 'array',
      items: EVIDENCE_ITEM,
    },
    supportedCriteria: {
      type: 'array',
      items: { type: 'string' },
    },
    resolvedQuestion: { type: 'string' },
    nextQuestion: { type: 'string' },
    blocker: { type: 'string' },
  },
  required: ['status', 'conclusion', 'evidence', 'supportedCriteria', 'resolvedQuestion', 'nextQuestion', 'blocker'],
  additionalProperties: false,
}

const COMPLETION_VERIFICATION = {
  type: 'object',
  properties: {
    status: { enum: ['verified', 'blocker'] },
    conclusion: { type: 'string' },
    criterionEvidence: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          criterion: { type: 'string' },
          evidence: {
            type: 'array',
            items: EVIDENCE_ITEM,
          },
        },
        required: ['criterion', 'evidence'],
        additionalProperties: false,
      },
    },
    blocker: { type: 'string' },
  },
  required: ['status', 'conclusion', 'criterionEvidence', 'blocker'],
  additionalProperties: false,
}

function isStringArray(value) {
  return Array.isArray(value) && value.every((item) => typeof item === 'string' && item.trim())
}

function normalizeInput(value) {
  if (!value || typeof value !== 'object' || Array.isArray(value)) {
    return { blocker: 'Invoke with an object containing task and acceptanceCriteria.' }
  }

  const { task, acceptanceCriteria, targetPaths = [], domainMethod = '', limits = {} } = value
  if (typeof task !== 'string' || !task.trim()) {
    return { blocker: 'Provide a non-empty task.' }
  }
  if (!isStringArray(acceptanceCriteria) || acceptanceCriteria.length === 0) {
    return { blocker: 'Provide one or more non-empty acceptanceCriteria.' }
  }
  if (!isStringArray(targetPaths)) {
    return { blocker: 'targetPaths must be an array of non-empty strings when provided.' }
  }
  if (typeof domainMethod !== 'string') {
    return { blocker: 'domainMethod must be a string when provided.' }
  }
  if (!limits || typeof limits !== 'object' || Array.isArray(limits)) {
    return { blocker: 'limits must be an object when provided.' }
  }

  const maxRounds = limits.maxRounds ?? DEFAULT_LIMITS.maxRounds
  const maxAgents = limits.maxAgents ?? DEFAULT_LIMITS.maxAgents
  if (!Number.isInteger(maxRounds) || maxRounds < 1 || maxRounds > DEFAULT_LIMITS.maxRounds) {
    return { blocker: `limits.maxRounds must be an integer from 1 to ${DEFAULT_LIMITS.maxRounds}.` }
  }
  if (!Number.isInteger(maxAgents) || maxAgents < 1 || maxAgents > DEFAULT_LIMITS.maxAgents) {
    return { blocker: `limits.maxAgents must be an integer from 1 to ${DEFAULT_LIMITS.maxAgents}.` }
  }

  return {
    input: {
      task: task.trim(),
      acceptanceCriteria: acceptanceCriteria.map((criterion) => criterion.trim()),
      targetPaths: targetPaths.map((path) => path.trim()),
      domainMethod: domainMethod.trim(),
      limits: { maxRounds, maxAgents, noProgressLimit: DEFAULT_LIMITS.noProgressLimit },
    },
  }
}

function formatEvidence(evidence) {
  if (evidence.length === 0) {
    return 'No accepted evidence yet.'
  }

  return evidence
    .map(({ path, version, detail, producer }) => `- ${path} @ ${version} (${producer}): ${detail}`)
    .join('\n')
}

function buildPrompt({ input, question, round, acceptedEvidence, completedScopes }) {
  const targetPaths = input.targetPaths.length > 0 ? input.targetPaths.join(', ') : 'No paths were supplied; establish only the smallest relevant map.'
  const completed = completedScopes.length > 0 ? completedScopes.join(', ') : 'None.'
  const method = input.domainMethod || 'Use repository-first evidence and the smallest relevant investigation method.'

  return `You are a read-only leaf investigator inside the active adaptive-long-horizon workflow.\n\nGoal: ${input.task}\nAcceptance criteria:\n${input.acceptanceCriteria.map((criterion) => `- ${criterion}`).join('\n')}\nRound: ${round}\nAssigned evidence question: ${question}\nTarget paths: ${targetPaths}\nAlready completed scopes: ${completed}\nAccepted evidence:\n${formatEvidence(acceptedEvidence)}\nActive method capsule: ${method}\n\nYou own only this evidence question. Read repository files only. Do not run build, test, install, formatter, generator, migration, or shell commands because they may write caches or other state. Do not edit files, create durable artifacts, commit, push, publish, alter configuration, start another workflow, spawn agents, or ask the user questions. Do not repeat completed scopes unless the accepted evidence identifies a concrete stale dependency. Return only evidence that can change the conclusion, blocker, risk, or next question.\n\nReturn status 'complete' only when the supplied acceptance criteria are supportable from your evidence, and list every supported criterion verbatim in supportedCriteria. A separate verifier will decide whether completion is accepted. Return status 'blocker' when a user-only decision, unavailable permission, missing environment, or missing material evidence prevents a supported conclusion. Otherwise return status 'evidence' with one next bounded evidence question, or an empty nextQuestion when no safe next question exists.`
}

function buildVerificationPrompt({ input, conclusion, evidence }) {
  return `You are a fresh-context completion verifier inside the active adaptive-long-horizon workflow.\n\nTask: ${input.task}\nAcceptance criteria:\n${input.acceptanceCriteria.map((criterion) => `- ${criterion}`).join('\n')}\nCandidate conclusion: ${conclusion}\nCandidate evidence:\n${formatEvidence(evidence)}\n\nRead only the cited repository files needed to verify the candidate conclusion. Do not run commands, edit files, create artifacts, commit, push, publish, alter configuration, start another workflow, spawn agents, or ask the user questions. Return 'verified' only when every acceptance criterion has direct cited evidence. For every criterion, return the supporting evidence records. Return 'blocker' for any missing, contradictory, stale, or unsupported evidence.`
}

const normalized = normalizeInput(args)
if (normalized.blocker) {
  return {
    status: 'blocked',
    blocker: normalized.blocker,
    evidence: [],
    progress: [],
  }
}

const { input } = normalized
const state = {
  input,
  round: 0,
  agentsUsed: 0,
  noProgressRounds: 0,
  acceptedEvidence: [],
  remainingQuestion: `Establish the smallest repository evidence map needed to assess: ${input.task}`,
  completedScopes: [],
  progress: [],
}

while (state.round < input.limits.maxRounds && state.agentsUsed < input.limits.maxAgents) {
  state.round += 1
  state.agentsUsed += 1

  const result = await agent(buildPrompt({
    input,
    question: state.remainingQuestion,
    round: state.round,
    acceptedEvidence: state.acceptedEvidence,
    completedScopes: state.completedScopes,
  }), {
    label: `adaptive evidence round ${state.round}`,
    schema: INVESTIGATION_RESULT,
  })

  if (!result) {
    return {
      status: 'blocked',
      blocker: 'The assigned investigation did not return a result.',
      evidence: state.acceptedEvidence,
      progress: state.progress,
    }
  }

  const newEvidence = result.evidence.filter((candidate) => !state.acceptedEvidence.some((accepted) => (
    accepted.path === candidate.path && accepted.version === candidate.version && accepted.detail === candidate.detail
  )))
  const madeProgress = newEvidence.length > 0 || result.status !== 'evidence'

  state.acceptedEvidence.push(...newEvidence.map((evidence) => ({ ...evidence, producer: `round-${state.round}` })))
  if (result.resolvedQuestion && newEvidence.length > 0) {
    state.completedScopes.push(result.resolvedQuestion)
  }
  state.progress.push({
    round: state.round,
    question: state.remainingQuestion,
    status: result.status,
    conclusion: result.conclusion,
    newEvidence: newEvidence.length,
  })

  if (result.status === 'complete') {
    const unsupportedCriteria = input.acceptanceCriteria.filter((criterion) => !result.supportedCriteria.includes(criterion))
    if (unsupportedCriteria.length > 0) {
      return {
        status: 'blocked',
        blocker: `The completion result omitted acceptance criteria: ${unsupportedCriteria.join('; ')}`,
        evidence: state.acceptedEvidence,
        progress: state.progress,
      }
    }

    state.agentsUsed += 1
    if (state.agentsUsed > input.limits.maxAgents) {
      return {
        status: 'blocked',
        blocker: `Completion verification would exceed the configured ${input.limits.maxAgents}-agent pilot limit.`,
        evidence: state.acceptedEvidence,
        progress: state.progress,
      }
    }

    const verification = await agent(buildVerificationPrompt({
      input,
      conclusion: result.conclusion,
      evidence: state.acceptedEvidence,
    }), {
      label: 'adaptive completion verification',
      schema: COMPLETION_VERIFICATION,
    })

    if (!verification || verification.status !== 'verified') {
      return {
        status: 'blocked',
        blocker: verification?.blocker || 'The independent completion verifier did not accept the candidate conclusion.',
        evidence: state.acceptedEvidence,
        progress: state.progress,
      }
    }

    const verifiedCriteria = verification.criterionEvidence
      .filter(({ evidence }) => evidence.length > 0)
      .map(({ criterion }) => criterion)
    const unverifiedCriteria = input.acceptanceCriteria.filter((criterion) => !verifiedCriteria.includes(criterion))
    if (unverifiedCriteria.length > 0) {
      return {
        status: 'blocked',
        blocker: `The independent completion verifier omitted evidence for: ${unverifiedCriteria.join('; ')}`,
        evidence: state.acceptedEvidence,
        progress: state.progress,
      }
    }

    return {
      status: 'complete',
      conclusion: verification.conclusion,
      evidence: state.acceptedEvidence,
      verification: verification.criterionEvidence,
      progress: state.progress,
    }
  }

  if (result.status === 'blocker') {
    return {
      status: 'blocked',
      blocker: result.blocker || result.conclusion,
      evidence: state.acceptedEvidence,
      progress: state.progress,
    }
  }

  state.noProgressRounds = madeProgress ? 0 : state.noProgressRounds + 1
  if (state.noProgressRounds >= input.limits.noProgressLimit) {
    return {
      status: 'blocked',
      blocker: 'Two consecutive investigation rounds returned no inspectable new evidence or resolved scope.',
      evidence: state.acceptedEvidence,
      progress: state.progress,
    }
  }

  if (!result.nextQuestion.trim()) {
    return {
      status: 'blocked',
      blocker: 'The investigation returned no safe next evidence question.',
      evidence: state.acceptedEvidence,
      progress: state.progress,
    }
  }

  state.remainingQuestion = result.nextQuestion
}

return {
  status: 'blocked',
  blocker: state.round >= input.limits.maxRounds
    ? `Reached the configured ${input.limits.maxRounds}-round pilot limit.`
    : `Reached the configured ${input.limits.maxAgents}-agent pilot limit.`,
  evidence: state.acceptedEvidence,
  progress: state.progress,
}
