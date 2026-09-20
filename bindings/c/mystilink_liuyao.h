#ifndef MYSTILINK_LIUYAO_H
#define MYSTILINK_LIUYAO_H

#ifdef __cplusplus
extern "C" {
#endif

/**
 * Run liuyao with argc/argv-style arguments (excluding program name).
 * On success, returns a heap-allocated JSON string (caller must free with
 * mystilink_liuyao_free). On failure, returns NULL and optionally writes an
 * error message into errbuf (if errbuf and errbuf_len are provided).
 *
 * CLI path: environment MYSTILINK_LIUYAO_CLI, else "liuyao" (alias mystilink-liuyao).
 */
char *mystilink_liuyao_run(int argc, const char *const *argv, char *errbuf, int errbuf_len);

/** Convenience: cast [--seed ...] or [--throws ...] */
char *mystilink_liuyao_cast(
    int seed,
    int use_seed,
    const char *throws_or_null,
    char *errbuf,
    int errbuf_len
);

/** Free a string returned by the API. */
void mystilink_liuyao_free(char *p);

#ifdef __cplusplus
}
#endif

#endif /* MYSTILINK_LIUYAO_H */
