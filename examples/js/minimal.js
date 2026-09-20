'use strict';

const { createLiuyaoApi } = require('../../bindings/js/browser');

async function demo(runCli) {
  const api = createLiuyaoApi(runCli);
  const result = await Promise.resolve(api.cast({ seed: 123 }));
  console.log('bits:', result.original_bits, result.schema_version);
}

if (require.main === module) {
  const nodeApi = require('../../bindings/js');
  demo((args) => nodeApi.runCli(args)).catch((err) => {
    console.error(err);
    process.exit(1);
  });
}

module.exports = { demo };
