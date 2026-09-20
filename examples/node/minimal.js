'use strict';

const path = require('path');
const liuyao = require(path.join(__dirname, '../../bindings/js'));

const result = liuyao.cast({ seed: 123 });
console.log('schema:', result.schema_version);
console.log('bits:', result.original_bits, 'moving:', result.has_moving);
