'use strict';

const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { spawnSync } = require('node:child_process');
const { normalizeRelative } = require('../../scripts/install-profile.js');

const repoRoot = path.resolve(__dirname, '..', '..');
const installer = path.join(repoRoot, 'scripts', 'install-profile.js');
const failures = [];

function fail(message) {
  failures.push(message);
}

function run(args, cwd) {
  return spawnSync(process.execPath, [installer, ...args], {
    cwd,
    encoding: 'utf8',
  });
}

function assertSuccess(result, label) {
  if (result.status !== 0) {
    fail(`${label} failed: ${result.stderr.trim() || result.stdout.trim()}`);
  }
}

function assertFailure(result, label) {
  if (result.status === 0) {
    fail(`${label} unexpectedly succeeded`);
  }
}

function listFiles(root) {
  if (!fs.existsSync(root)) {
    return [];
  }
  const result = [];
  const visit = (current) => {
    for (const entry of fs.readdirSync(current, { withFileTypes: true })) {
      const absolute = path.join(current, entry.name);
      if (entry.isDirectory()) {
        visit(absolute);
      } else {
        result.push(path.relative(root, absolute).replace(/\\/g, '/'));
      }
    }
  };
  visit(root);
  return result.sort();
}

function expectedSkillFiles(skillNames) {
  const result = [];
  for (const skillName of skillNames) {
    const source = path.join(repoRoot, 'skills', skillName);
    const visit = (current, relative) => {
      for (const entry of fs.readdirSync(current, { withFileTypes: true })) {
        const absolute = path.join(current, entry.name);
        const next = relative ? path.join(relative, entry.name) : entry.name;
        if (entry.isDirectory()) {
          if (next === 'evals' || next.startsWith(`evals${path.sep}`)) {
            continue;
          }
          visit(absolute, next);
        } else if (next === 'SKILL.md' || next.startsWith(`references${path.sep}`)) {
          result.push(path.join('skills', skillName, next).replace(/\\/g, '/'));
        }
      }
    };
    visit(source, '');
  }
  return result.sort();
}

const allSkills = [
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
const fastSkills = ['debug-systematically', 'test-strategy', 'review-and-finish'];
const tempRoot = fs.mkdtempSync(path.join(os.tmpdir(), 'coding-agent-skills-profile-'));
const fastTarget = path.join(tempRoot, 'fast', '.claude');
const qualityTarget = path.join(tempRoot, 'quality', '.claude');
const labTarget = path.join(tempRoot, 'lab', '.claude');

try {
  const dryRun = run(['--profile', 'fast', '--target-root', fastTarget], repoRoot);
  assertSuccess(dryRun, 'fast dry-run');
  if (fs.existsSync(fastTarget)) {
    fail('dry-run created the target directory');
  }

  const fastApply = run(['--profile', 'fast', '--target-root', fastTarget, '--apply'], repoRoot);
  assertSuccess(fastApply, 'fast apply');
  if (JSON.stringify(listFiles(fastTarget)) !== JSON.stringify(expectedSkillFiles(fastSkills))) {
    fail('fast installed files differ from the expected skill set');
  }
  if (listFiles(fastTarget).some((file) => file.includes('/evals/') || file.endsWith('/CLAUDE.md'))) {
    fail('fast installed a forbidden eval or CLAUDE.md file');
  }
  fs.mkdirSync(path.join(fastTarget, 'unrelated'), { recursive: true });
  fs.writeFileSync(path.join(fastTarget, 'unrelated', 'keep.txt'), 'keep');
  const fastRepeat = run(['--profile', 'fast', '--target-root', fastTarget, '--apply'], repoRoot);
  assertSuccess(fastRepeat, 'fast idempotent apply');
  if (fs.readFileSync(path.join(fastTarget, 'unrelated', 'keep.txt'), 'utf8') !== 'keep') {
    fail('unrelated target file was changed');
  }

  const qualityApply = run(['--profile', 'quality', '--target-root', qualityTarget, '--apply'], repoRoot);
  assertSuccess(qualityApply, 'quality apply');
  if (JSON.stringify(listFiles(qualityTarget)) !== JSON.stringify(expectedSkillFiles(allSkills))) {
    fail('quality installed files differ from the expected skill set');
  }

  const labApply = run(['--profile', 'lab', '--target-root', labTarget, '--apply'], repoRoot);
  assertSuccess(labApply, 'lab apply');
  const labFiles = listFiles(labTarget);
  if (!labFiles.includes('workflows/adaptive-long-horizon.js')) {
    fail('lab did not install the adaptive workflow');
  }
  if (labFiles.filter((file) => file === 'workflows/adaptive-long-horizon.js').length !== 1) {
    fail('lab installed duplicate adaptive workflows');
  }

  const conflictPath = path.join(fastTarget, 'skills', 'debug-systematically', 'SKILL.md');
  fs.writeFileSync(conflictPath, 'conflict');
  assertFailure(run(['--profile', 'fast', '--target-root', fastTarget, '--apply'], repoRoot), 'conflicting apply');
  assertSuccess(run(['--profile', 'fast', '--target-root', fastTarget, '--apply', '--force'], repoRoot), 'forced conflict apply');

  assertFailure(run(['--profile', 'unknown', '--target-root', path.join(tempRoot, 'unknown')], repoRoot), 'unknown profile');
  assertFailure(run(['--target-root', path.join(tempRoot, 'missing-profile')], repoRoot), 'missing profile');
  assertFailure(run(['--profile', 'fast'], repoRoot), 'missing target');
  assertFailure(run(['--profile', 'fast', '--target-root', path.join(tempRoot, 'bad'), '--unknown'], repoRoot), 'unknown flag');
  assertFailure(run(['--profile', 'fast', '--target-root', path.join(repoRoot, 'profiles')], repoRoot), 'source-inside target');
  for (const value of ['C:/outside.js', 'C:\\outside.js', 'scheme:value']) {
    try {
      normalizeRelative(value, 'test path');
      fail(`normalizeRelative accepted unsafe path: ${value}`);
    } catch (error) {
      if (!error.message.includes('repository-relative')) {
        throw error;
      }
    }
  }
  const symlinkTarget = path.join(tempRoot, 'symlink-target');
  fs.mkdirSync(symlinkTarget, { recursive: true });
  const symlinkPath = path.join(tempRoot, 'symlink-root');
  const nestedTarget = path.join(symlinkPath, 'nested', '.claude');
  try {
    fs.symlinkSync(symlinkTarget, symlinkPath, 'junction');
    assertFailure(run(['--profile', 'fast', '--target-root', symlinkPath], repoRoot), 'symlink target root');
    assertFailure(run(['--profile', 'fast', '--target-root', nestedTarget], repoRoot), 'symlinked ancestor target root');
  } catch (error) {
    if (error.code !== 'EPERM' && error.code !== 'EEXIST') {
      throw error;
    }
  }

  const danglingPath = path.join(fastTarget, 'skills', 'test-strategy', 'SKILL.md');
  fs.rmSync(danglingPath, { force: true });
  fs.symlinkSync(path.join(tempRoot, 'missing-outside-file'), danglingPath, 'file');
  assertFailure(run(['--profile', 'fast', '--target-root', fastTarget, '--apply'], repoRoot), 'dangling destination symlink');

  const hardlinkSource = path.join(tempRoot, 'hardlink-outside.txt');
  const hardlinkDestination = path.join(fastTarget, 'skills', 'review-and-finish', 'SKILL.md');
  fs.writeFileSync(hardlinkSource, 'outside');
  fs.unlinkSync(hardlinkDestination);
  fs.linkSync(hardlinkSource, hardlinkDestination);
  assertFailure(run(['--profile', 'fast', '--target-root', fastTarget, '--apply', '--force'], repoRoot), 'hardlinked destination');
} finally {
  fs.rmSync(tempRoot, { recursive: true, force: true });
}

if (failures.length > 0) {
  for (const failure of failures) {
    process.stderr.write(`FAIL: ${failure}\n`);
  }
  process.exitCode = 1;
} else {
  process.stdout.write('PASS: profile installer is explicit, dry-run by default, conflict-safe, idempotent, and non-runtime.\n');
}
