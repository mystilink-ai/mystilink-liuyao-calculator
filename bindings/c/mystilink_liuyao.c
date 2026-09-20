#include "mystilink_liuyao.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef _WIN32
#define POPEN _popen
#define PCLOSE _pclose
#else
#define POPEN popen
#define PCLOSE pclose
#endif

static const char *cli_path(void) {
    const char *env = getenv("MYSTILINK_LIUYAO_CLI");
    return (env && env[0]) ? env : "liuyao";
}

static void set_err(char *errbuf, int errbuf_len, const char *msg) {
    if (!errbuf || errbuf_len <= 0) {
        return;
    }
    snprintf(errbuf, (size_t)errbuf_len, "%s", msg ? msg : "unknown error");
}

static char *read_all(FILE *fp) {
    size_t cap = 4096;
    size_t len = 0;
    char *buf = (char *)malloc(cap);
    if (!buf) {
        return NULL;
    }
    for (;;) {
        if (len + 1024 >= cap) {
            cap *= 2;
            char *nbuf = (char *)realloc(buf, cap);
            if (!nbuf) {
                free(buf);
                return NULL;
            }
            buf = nbuf;
        }
        size_t n = fread(buf + len, 1, 1024, fp);
        len += n;
        if (n < 1024) {
            break;
        }
    }
    buf[len] = '\0';
    return buf;
}

static char *shell_quote(const char *s) {
    /* Simple single-quote wrapping for POSIX shells. */
    size_t len = strlen(s);
    /* worst case: every char is ' -> '\'' */
    char *out = (char *)malloc(len * 4 + 3);
    if (!out) {
        return NULL;
    }
    char *p = out;
    *p++ = '\'';
    for (size_t i = 0; i < len; i++) {
        if (s[i] == '\'') {
            memcpy(p, "'\\''", 4);
            p += 4;
        } else {
            *p++ = s[i];
        }
    }
    *p++ = '\'';
    *p = '\0';
    return out;
}

char *mystilink_liuyao_run(int argc, const char *const *argv, char *errbuf, int errbuf_len) {
    if (argc < 1 || !argv) {
        set_err(errbuf, errbuf_len, "no arguments");
        return NULL;
    }

    size_t cmd_cap = 256;
    char *cmd = (char *)malloc(cmd_cap);
    if (!cmd) {
        set_err(errbuf, errbuf_len, "out of memory");
        return NULL;
    }
    cmd[0] = '\0';

    const char *cli = cli_path();
    char *qcli = shell_quote(cli);
    if (!qcli) {
        free(cmd);
        set_err(errbuf, errbuf_len, "out of memory");
        return NULL;
    }
    snprintf(cmd, cmd_cap, "%s", qcli);
    free(qcli);

    for (int i = 0; i < argc; i++) {
        char *qa = shell_quote(argv[i]);
        if (!qa) {
            free(cmd);
            set_err(errbuf, errbuf_len, "out of memory");
            return NULL;
        }
        size_t need = strlen(cmd) + 1 + strlen(qa) + 1;
        if (need > cmd_cap) {
            while (cmd_cap < need) {
                cmd_cap *= 2;
            }
            char *ncmd = (char *)realloc(cmd, cmd_cap);
            if (!ncmd) {
                free(qa);
                free(cmd);
                set_err(errbuf, errbuf_len, "out of memory");
                return NULL;
            }
            cmd = ncmd;
        }
        strcat(cmd, " ");
        strcat(cmd, qa);
        free(qa);
    }

    /* Redirect stderr to stdout so callers see errors in the buffer when needed.
       Prefer capturing stdout only for success JSON. */
    {
        size_t need = strlen(cmd) + 16;
        if (need > cmd_cap) {
            char *ncmd = (char *)realloc(cmd, need);
            if (!ncmd) {
                free(cmd);
                set_err(errbuf, errbuf_len, "out of memory");
                return NULL;
            }
            cmd = ncmd;
            cmd_cap = need;
        }
        strcat(cmd, " 2>/dev/null");
    }

    FILE *fp = POPEN(cmd, "r");
    free(cmd);
    if (!fp) {
        set_err(errbuf, errbuf_len, "failed to start liuyao");
        return NULL;
    }

    char *out = read_all(fp);
    int status = PCLOSE(fp);
    if (!out) {
        set_err(errbuf, errbuf_len, "failed to read CLI output");
        return NULL;
    }
    if (status != 0) {
        set_err(errbuf, errbuf_len, out[0] ? out : "liuyao failed");
        free(out);
        return NULL;
    }
    return out;
}

char *mystilink_liuyao_cast(
    int seed,
    int use_seed,
    const char *throws_or_null,
    char *errbuf,
    int errbuf_len
) {
    char seed_buf[32];
    const char *argv_store[8];
    int n = 0;
    argv_store[n++] = "cast";
    if (throws_or_null && throws_or_null[0]) {
        argv_store[n++] = "--throws";
        argv_store[n++] = throws_or_null;
    } else if (use_seed) {
        snprintf(seed_buf, sizeof(seed_buf), "%d", seed);
        argv_store[n++] = "--seed";
        argv_store[n++] = seed_buf;
    }
    return mystilink_liuyao_run(n, argv_store, errbuf, errbuf_len);
}

void mystilink_liuyao_free(char *p) {
    free(p);
}
