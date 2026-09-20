# @mystilink/liuyao-calculator

Node and browser binding for the `liuyao` CLI.

## Prerequisites

Install the Python package so `liuyao` is on `PATH`, or set `MYSTILINK_LIUYAO_CLI` to the executable path.

## Node

```js
const liuyao = require('@mystilink/liuyao-calculator');
const result = liuyao.cast({ seed: 123 });
```

## Browser

```js
const { createLiuyaoApi } = require('@mystilink/liuyao-calculator/browser');
const api = createLiuyaoApi(async (args) => hostRunCli(args));
```
