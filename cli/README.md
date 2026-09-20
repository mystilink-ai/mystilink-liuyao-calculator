# CLI shim notes

After `python3 -m pip install -e .` from the repository root, the console scripts
`liuyao` and `mystilink-liuyao` are available. Equivalent module form:

```bash
python3 -m mystilink_liuyao <subcommand> ...
```

Override the executable used by language bindings with `MYSTILINK_LIUYAO_CLI`.
