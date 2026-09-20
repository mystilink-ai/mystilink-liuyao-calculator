'use strict';

function createLiuyaoApi(runCli) {
  if (typeof runCli !== 'function') {
    throw new Error('createLiuyaoApi requires a runCli(args) function that returns parsed JSON');
  }

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

  return { cast, version, runCli };
}

module.exports = { createLiuyaoApi };

if (typeof window !== 'undefined') {
  window.MystilinkLiuyao = { createLiuyaoApi };
}
