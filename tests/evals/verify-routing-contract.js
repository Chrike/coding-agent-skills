'use strict';

const fs = require('node:fs');
const path = require('node:path');

const repoRoot = path.resolve(__dirname, '..', '..');
const skillsRoot = path.join(repoRoot, 'skills');
const failures = [];

function fail(message) {
  failures.push(message);
}

function read(relativePath) {
  const filePath = path.join(repoRoot, relativePath);
  try {
    return fs.readFileSync(filePath, 'utf8');
  } catch (error) {
    fail(`${relativePath}: ${error.message}`);
    return '';
  }
}

function skillSource(skillName) {
  return `skills/${skillName}/SKILL.md`;
}

function parseFrontmatter(content, relativePath) {
  const match = /^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)/.exec(content);
  if (!match) {
    fail(`${relativePath}: missing frontmatter`);
    return { name: '', description: '' };
  }
  const name = /^name:\s*(\S+)\s*$/m.exec(match[1])?.[1] || '';
  const description = /^description:\s*(.+?)\s*$/m.exec(match[1])?.[1] || '';
  if (!name) {
    fail(`${relativePath}: frontmatter name is missing`);
  }
  if (!description) {
    fail(`${relativePath}: frontmatter description is missing`);
  }
  return { name, description };
}

if (!fs.existsSync(path.join(repoRoot, 'prompts/CLAUDE.fragment.md'))) {
  fail('prompts/CLAUDE.fragment.md: canonical Kernel source is missing');
}

const kernel = read('prompts/CLAUDE.fragment.md');
const routingContract = read('tests/routing-contract.md');
const triggerMatrix = read('tests/trigger-matrix.md');
const nonTriggerCases = read('tests/non-trigger-cases.md');

for (const [relativePath, content] of [
  ['tests/routing-contract.md', routingContract],
  ['tests/trigger-matrix.md', triggerMatrix],
  ['tests/non-trigger-cases.md', nonTriggerCases]
]) {
  if (!content.includes('It is not a runtime skill.') && relativePath !== 'tests/non-trigger-cases.md') {
    fail(`${relativePath}: must remain a non-runtime maintenance contract`);
  }
  if (!content.includes('prompts/CLAUDE.fragment.md')) {
    fail(`${relativePath}: must identify the canonical Kernel source`);
  }
  if (!content.includes('skill') || !content.includes('SKILL.md')) {
    fail(`${relativePath}: must identify current skill source ownership`);
  }
}

if (!kernel.includes('# Default Coding Behavior')) {
  fail('prompts/CLAUDE.fragment.md: canonical Kernel heading is missing');
}
if (!routingContract.includes('## Source Of Truth')) {
  fail('tests/routing-contract.md: Source Of Truth section is missing');
}

let skillNames = [];
try {
  skillNames = fs.readdirSync(skillsRoot, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => entry.name)
    .sort();
} catch (error) {
  fail(`skills: ${error.message}`);
}

const sourceIndex = new Map();
for (const match of routingContract.matchAll(/^\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|\s*$/gm)) {
  sourceIndex.set(match[1], match[2]);
}

for (const skillName of skillNames) {
  const relativePath = skillSource(skillName);
  const content = read(relativePath);
  const frontmatter = parseFrontmatter(content, relativePath);
  if (frontmatter.name !== skillName) {
    fail(`${relativePath}: frontmatter name must match directory name ${skillName}`);
  }
  const expectedPath = skillSource(skillName);
  if (sourceIndex.get(skillName) !== expectedPath) {
    fail(`tests/routing-contract.md: missing canonical source index entry for ${skillName}`);
  }
  for (const [label, document] of [
    ['routing contract', routingContract],
    ['trigger matrix', triggerMatrix],
    ['non-trigger cases', nonTriggerCases]
  ]) {
    if (!document.includes(`\`${skillName}\``)) {
      fail(`tests/${label}: missing current skill coverage for ${skillName}`);
    }
  }
}

for (const [skillName, relativePath] of sourceIndex) {
  if (!skillNames.includes(skillName)) {
    fail(`tests/routing-contract.md: source index names unknown skill ${skillName}`);
  }
  if (relativePath !== skillSource(skillName)) {
    fail(`tests/routing-contract.md: source index path is not canonical for ${skillName}`);
  }
}

if (sourceIndex.size !== skillNames.length) {
  fail(`tests/routing-contract.md: canonical source index must contain exactly ${skillNames.length} skills`);
}

if (failures.length > 0) {
  for (const failure of failures) {
    process.stderr.write(`FAIL: ${failure}\n`);
  }
  process.exitCode = 1;
} else {
  process.stdout.write(`PASS: routing, trigger, and non-trigger contracts cover the ${skillNames.length} current skills and canonical Kernel source.\n`);
}
