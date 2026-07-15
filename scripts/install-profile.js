'use strict';

const fs = require('node:fs');
const path = require('node:path');

const repoRoot = path.resolve(__dirname, '..');
const manifestPath = path.join(repoRoot, 'profiles', 'manifest.json');

function usage() {
  return [
    'Usage: node scripts/install-profile.js --profile <fast|quality|lab> --target-root <path> [--apply] [--force]',
    '',
    'Dry-run is the default. --apply is required for writes. --force replaces differing owned files only.',
  ].join('\n');
}

function fail(message) {
  throw new Error(message);
}

function parseArgs(argv) {
  const options = { apply: false, force: false };
  const valueOptions = new Set(['profile', 'target-root']);
  for (let index = 0; index < argv.length; index += 1) {
    const flag = argv[index];
    if (flag === '--help' || flag === '-h') {
      options.help = true;
      continue;
    }
    if (flag === '--apply') {
      options.apply = true;
      continue;
    }
    if (flag === '--force') {
      options.force = true;
      continue;
    }
    if (!flag.startsWith('--') || !valueOptions.has(flag.slice(2))) {
      fail(`Unknown argument: ${flag}`);
    }
    const key = flag.slice(2);
    const value = argv[index + 1];
    if (!value || value.startsWith('--')) {
      fail(`${flag} requires a value`);
    }
    if (options[key]) {
      fail(`${flag} was provided more than once`);
    }
    options[key] = value;
    index += 1;
  }
  return options;
}

function readManifest() {
  try {
    return JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
  } catch (error) {
    fail(`Unable to read profile manifest: ${error.message}`);
  }
}

function normalizeRelative(value, label) {
  if (typeof value !== 'string' || value.trim() === '') {
    fail(`${label} must be a non-empty relative path`);
  }
  const normalized = value.replace(/\\/g, '/');
  if (path.posix.isAbsolute(normalized)
    || /^[A-Za-z]:\//.test(normalized)
    || normalized.includes(':')
    || normalized.split('/').includes('..')) {
    fail(`${label} must be repository-relative and must not be absolute, drive-qualified, scheme-qualified, or contain parent traversal`);
  }
  return normalized;
}

function assertOutside(root, candidate, label) {
  const relative = path.relative(root, candidate);
  const inside = relative === '' || (!relative.startsWith('..') && !path.isAbsolute(relative));
  if (inside) {
    fail(`${label} must remain outside the repository source tree`);
  }
}

function assertSourcePath(relativePath) {
  const normalized = normalizeRelative(relativePath, 'source path');
  const absolute = path.resolve(repoRoot, normalized);
  const relativeToRepo = path.relative(repoRoot, absolute);
  if (relativeToRepo.startsWith('..') || path.isAbsolute(relativeToRepo)) {
    fail(`source path escapes the repository: ${relativePath}`);
  }
  return absolute;
}

function assertNoSymlinkAlongPath(candidate) {
  const resolved = path.resolve(candidate);
  const parsed = path.parse(resolved);
  const relative = path.relative(parsed.root, resolved);
  const segments = relative ? relative.split(path.sep).filter(Boolean) : [];
  let current = parsed.root;
  for (const segment of segments) {
    current = path.join(current, segment);
    let stat;
    try {
      stat = fs.lstatSync(current);
    } catch (error) {
      if (error.code === 'ENOENT') {
        break;
      }
      if (error.code === 'ENOTDIR') {
        fail(`target path has a non-directory parent: ${path.relative(repoRoot, current)}`);
      }
      fail(`unable to inspect target path: ${path.relative(repoRoot, current)} (${error.message})`);
    }
    if (stat.isSymbolicLink()) {
      fail(`target path contains a symlink: ${path.relative(repoRoot, current)}`);
    }
  }
}

function collectFiles(sourceRoot, relativeRoot) {
  const source = path.join(sourceRoot, relativeRoot);
  if (!fs.existsSync(source)) {
    fail(`missing source path: ${path.relative(repoRoot, source)}`);
  }
  if (fs.lstatSync(source).isSymbolicLink()) {
    fail(`source path must not be a symlink: ${path.relative(repoRoot, source)}`);
  }
  const files = [];
  const visit = (current, relative) => {
    const stat = fs.lstatSync(current);
    if (stat.isSymbolicLink()) {
      fail(`source tree contains a symlink: ${path.relative(repoRoot, current)}`);
    }
    if (stat.isFile()) {
      files.push({ source: current, relative });
      return;
    }
    if (!stat.isDirectory()) {
      fail(`source path is not a regular file or directory: ${path.relative(repoRoot, current)}`);
    }
    for (const entry of fs.readdirSync(current, { withFileTypes: true })) {
      const entryRelative = relative ? path.join(relative, entry.name) : entry.name;
      visit(path.join(current, entry.name), entryRelative);
    }
  };
  visit(source, '');
  return files;
}

function buildPlan(options, manifest) {
  const profile = manifest.profiles?.[options.profile];
  if (!profile) {
    fail(`Unknown profile: ${options.profile}`);
  }
  const targetRoot = path.resolve(process.cwd(), options['target-root']);
  assertOutside(repoRoot, targetRoot, 'target root');
  if (fs.existsSync(targetRoot) && fs.lstatSync(targetRoot).isSymbolicLink()) {
    fail('target root must not be a symlink');
  }
  assertNoSymlinkAlongPath(targetRoot);

  const plan = [];
  for (const skillName of profile.skills) {
    const entry = manifest.skill_sources?.[skillName];
    if (!entry) {
      fail(`Profile references unknown skill: ${skillName}`);
    }
    const sourceRoot = assertSourcePath(entry.source);
    for (const runtimePath of entry.runtime_paths) {
      const normalizedPath = normalizeRelative(runtimePath, `${skillName} runtime path`);
      if (normalizedPath !== 'SKILL.md' && normalizedPath !== 'references') {
        fail(`Unsupported runtime path for ${skillName}: ${runtimePath}`);
      }
      const files = collectFiles(sourceRoot, normalizedPath);
      for (const file of files) {
        const destinationRelative = path.join('skills', skillName, normalizedPath, file.relative);
        plan.push({
          source: file.source,
          destination: path.resolve(targetRoot, destinationRelative),
          destinationRelative: destinationRelative.replace(/\\/g, '/'),
        });
      }
    }
  }

  for (const workflowName of profile.workflows) {
    const entry = manifest.workflow_sources?.[workflowName];
    if (!entry || entry.visibility !== 'explicit-only') {
      fail(`Profile references an invalid workflow: ${workflowName}`);
    }
    const source = assertSourcePath(entry.source);
    const destinationRelative = normalizeRelative(entry.destination, `${workflowName} destination`);
    plan.push({
      source,
      destination: path.resolve(targetRoot, destinationRelative),
      destinationRelative,
    });
  }

  const seen = new Set();
  for (const item of plan) {
    if (seen.has(item.destination)) {
      fail(`profile contains duplicate destination: ${item.destinationRelative}`);
    }
    seen.add(item.destination);
    assertNoSymlinkAlongPath(item.destination);
  }
  return { targetRoot, plan };
}

function inspectPlan(plan, force) {
  const entries = [];
  for (const item of plan) {
    let stat;
    try {
      stat = fs.lstatSync(item.destination);
    } catch (error) {
      if (error.code === 'ENOENT') {
        entries.push({ ...item, status: 'add' });
        continue;
      }
      fail(`unable to inspect destination: ${item.destinationRelative} (${error.message})`);
    }
    if (stat.isSymbolicLink() || !stat.isFile()) {
      fail(`destination is not a regular file: ${item.destinationRelative}`);
    }
    const same = Buffer.compare(fs.readFileSync(item.destination), fs.readFileSync(item.source)) === 0;
    if (same) {
      entries.push({ ...item, status: 'unchanged' });
    } else if (force) {
      if (Number.isInteger(stat.nlink) && stat.nlink > 1) {
        fail(`refusing to replace a hardlinked destination: ${item.destinationRelative}`);
      }
      entries.push({ ...item, status: 'replace' });
    } else {
      fail(`conflicting destination (use --force to replace): ${item.destinationRelative}`);
    }
  }
  return entries;
}

function ensureParentDirectories(targetRoot, destination) {
  if (!fs.existsSync(targetRoot)) {
    fs.mkdirSync(targetRoot, { recursive: true });
  }
  const relative = path.relative(targetRoot, path.dirname(destination));
  const segments = relative ? relative.split(path.sep) : [];
  let current = targetRoot;
  for (const segment of segments) {
    current = path.join(current, segment);
    if (fs.existsSync(current)) {
      if (!fs.lstatSync(current).isDirectory() || fs.lstatSync(current).isSymbolicLink()) {
        fail(`destination parent is not a normal directory: ${path.relative(targetRoot, current)}`);
      }
    } else {
      fs.mkdirSync(current);
    }
  }
}

function main(argv) {
  const options = parseArgs(argv);
  if (options.help) {
    process.stdout.write(`${usage()}\n`);
    return;
  }
  if (!options.profile || !options['target-root']) {
    fail(`--profile and --target-root are required\n\n${usage()}`);
  }
  const manifest = readManifest();
  const { targetRoot, plan } = buildPlan(options, manifest);
  const entries = inspectPlan(plan, options.force);
  for (const entry of entries) {
    process.stdout.write(`${entry.status}\t${entry.destinationRelative}\n`);
  }
  if (!options.apply) {
    process.stdout.write('DRY-RUN: no files were written; pass --apply to install.\n');
    return;
  }
  for (const entry of entries) {
    if (entry.status === 'unchanged') {
      continue;
    }
    ensureParentDirectories(targetRoot, entry.destination);
    fs.copyFileSync(entry.source, entry.destination);
  }
  process.stdout.write(`APPLIED: ${entries.filter(({ status }) => status !== 'unchanged').length} file(s) written.\n`);
}

if (require.main === module) {
  try {
    main(process.argv.slice(2));
  } catch (error) {
    process.stderr.write(`ERROR: ${error.message}\n`);
    process.exitCode = 1;
  }
}

module.exports = { main, parseArgs, normalizeRelative };
