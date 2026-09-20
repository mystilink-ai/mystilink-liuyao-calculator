#include <stdio.h>
#include <stdlib.h>

#include "../../bindings/c/mystilink_liuyao.h"

int main(void) {
    char err[512];
    err[0] = '\0';
    char *json = mystilink_liuyao_cast(123, 1, NULL, err, sizeof(err));
    if (!json) {
        fprintf(stderr, "error: %s\n", err);
        return 1;
    }
    fputs(json, stdout);
    fputc('\n', stdout);
    mystilink_liuyao_free(json);
    return 0;
}
