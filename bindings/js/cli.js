'use strict';

const { spawnSync } = require('child_process');

function resolveCli() {
  return process.env.MYSTILINK_LIUYAO_CLI || 'liuyao';
}

function runCli(args, opts = {}) {
  const cli = opts.cli || resolveCli();
  const result = spawnSync(cli, args, {
    encoding: 'utf8',
    maxBuffer: 10 * 1024 * 1024,
  });
  if (result.error) {
    throw result.error;
  }
  if (result.status !== 0) {
    const errText = (result.stderr || result.stdout || '').trim();
    throw new Error(errText || `liuyao exited with code ${result.status}`);
  }
  return JSON.parse(result.stdout);
}

/**
 * @param {{ seed?: number, throws?: string, envelope?: boolean, locale?: string }} [options]
 */
function cast(options = {}) {
  const args = ['cast'];
  if (options.throws) {
    args.push('--throws', String(options.throws));
  } else if (options.seed !== undefined && options.seed !== null) {
    args.push('--seed', String(options.seed));
  }
  if (options.envelope) {
    args.push('--envelope');
  }
  if (options.locale) {
    args.push('--locale', String(options.locale));
  }
  return runCli(args);
}

function version() {
  return runCli(['version']);
}

module.exports = {
  resolveCli,
  runCli,
  cast,
  version,
};
