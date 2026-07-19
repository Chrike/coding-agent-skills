export const meta = {
  name: 'fresh-findings-review',
  description: 'Run one bounded, read-only findings-only review with a fresh project Agent when available',
}

const READ_ONLY_FALLBACK_AGENT = 'Explore'

const FINDINGS_RESULT = {
  type: 'object',
  properties: {
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          severity: { enum: ['critical', 'high', 'medium', 'low'] },
          summary: { type: 'string', minLength: 1 },
          path: { type: 'string', minLength: 1 },
          location: { type: 'string', minLength: 1 },
          failureScenario: { type: 'string', minLength: 1 },
          evidence: { type: 'string', minLength: 1 },
        },
        required: ['severity', 'summary', 'path', 'location', 'failureScenario', 'evidence'],
        additionalProperties: false,
      },
    },
    blocker: { type: 'string' },
  },
  required: ['findings', 'blocker'],
  additionalProperties: false,
}

function normalizeText(value) {
  return typeof value === 'string' ? value.trim() : ''
}

function normalizeRepoPath(value) {
  const raw = normalizeText(value).replace(/\\/g, '/')
  if (!raw || raw.startsWith('/') || /^[A-Za-z]:/.test(raw) || raw.includes(':')) {
    return null
  }
  const segments = raw.split('/')
  if (segments.some((segment) => segment === '..')) {
    return null
  }
  return segments.filter((segment) => segment && segment !== '.').join('/') || null
}

function isUsableLocation(value) {
  const location = normalizeText(value)
  if (/^(?:symbol|section):\s*\S.*$/i.test(location)) {
    return true
  }

  const match = /^lines:(\d+)(?:-(\d+))?$/i.exec(location)
  if (!match) {
    return false
  }

  const start = Number(match[1])
  const end = Number(match[2] || match[1])
  return Number.isSafeInteger(start)
    && Number.isSafeInteger(end)
    && start >= 1
    && end >= start
}

function isSelectorResolutionError(error) {
  const message = normalizeText(error?.message || error)
  return /^agent\(\{agentType\}\): agent type '[^']+' not found\.$/i.test(message)
}

function buildPrompt(input) {
  const targetPaths = input.targetPaths.length > 0
    ? input.targetPaths.join(', ')
    : 'Use the smallest relevant repository-relative scope.'

  return `You are a fresh-context, read-only findings-only reviewer. Review only this task: ${input.task}

Review context:
${input.context || 'No additional context was supplied.'}

Allowed cited paths:
${targetPaths}

Inspect only the supplied scope. Identify concrete correctness, security, compatibility, or regression failures introduced or exposed by the reviewed artifact. Do not treat style preferences, missing tests, or speculative concerns as findings without a concrete propagation path. Return findings ordered by severity. Each finding must include severity, concise summary, repository-relative path, exact location written as symbol: Name, section: Name, or lines:N-M, a concrete failureScenario, and supporting evidence. Return an empty findings array when no grounded issue remains, or blocker when the scope/evidence is insufficient.

Do not edit, write, run commands, create artifacts, commit, push, publish, alter configuration, decide completion, perform branch actions, delegate, or ask questions. Stop after this bounded findings-only pass.`
}

async function runReviewer(prompt) {
  try {
    return await agent(prompt, {
      agentType: 'fresh-findings-reviewer',
      label: 'fresh findings-only review',
      schema: FINDINGS_RESULT,
    })
  } catch (error) {
    if (!isSelectorResolutionError(error)) {
      throw error
    }
    return await agent(prompt, {
      agentType: READ_ONLY_FALLBACK_AGENT,
      label: 'read-only findings-only review fallback',
      schema: FINDINGS_RESULT,
    })
  }
}

function validateResult(result, targetPaths) {
  if (!result || !Array.isArray(result.findings) || typeof result.blocker !== 'string') {
    return { blocker: 'The findings reviewer returned a malformed result.' }
  }
  if (result.blocker.trim()) {
    return { blocker: result.blocker.trim() }
  }

  const findings = []
  for (const finding of result.findings) {
    const path = normalizeRepoPath(finding.path)
    const location = normalizeText(finding.location)
    const summary = normalizeText(finding.summary)
    const failureScenario = normalizeText(finding.failureScenario)
    const evidence = normalizeText(finding.evidence)
    if (!path || !isUsableLocation(location)) {
      return { blocker: 'The findings reviewer returned an invalid repository path or location.' }
    }
    if (!['critical', 'high', 'medium', 'low'].includes(finding.severity)) {
      return { blocker: 'The findings reviewer returned an unsupported severity.' }
    }
    if (!summary || !failureScenario || !evidence) {
      return { blocker: 'The findings reviewer returned an empty summary, failure scenario, or evidence field.' }
    }
    if (targetPaths.length > 0 && !targetPaths.some((target) => path === target || path.startsWith(`${target}/`))) {
      return { blocker: `The findings reviewer cited ${path} outside the supplied targetPaths boundary.` }
    }
    findings.push({
      severity: finding.severity,
      summary,
      path,
      location,
      failureScenario,
      evidence,
    })
  }

  return { findings }
}

const input = args
if (!input || typeof input !== 'object' || Array.isArray(input) || !normalizeText(input.task)) {
  return { status: 'blocked', blocker: 'Invoke with an object containing a non-empty task.' }
}

if (input.targetPaths !== undefined && !Array.isArray(input.targetPaths)) {
  return { status: 'blocked', blocker: 'targetPaths must be an array when provided.' }
}

const targetPaths = (input.targetPaths || []).map(normalizeRepoPath)
if (targetPaths.some((path) => !path)) {
  return { status: 'blocked', blocker: 'targetPaths must contain repository-relative paths.' }
}

const result = await runReviewer(buildPrompt({
  task: normalizeText(input.task),
  context: normalizeText(input.context),
  targetPaths,
}))
const validated = validateResult(result, targetPaths)
if (validated.blocker) {
  return { status: 'blocked', blocker: validated.blocker }
}

return { status: 'reviewed', findings: validated.findings, blocker: '' }
