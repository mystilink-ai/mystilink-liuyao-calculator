#ifndef MYSTILINK_LIUYAO_HPP
#define MYSTILINK_LIUYAO_HPP

#include "../c/mystilink_liuyao.h"

#include <stdexcept>
#include <string>
#include <vector>

namespace mystilink {
namespace liuyao {

inline std::string run(const std::vector<std::string> &args) {
    std::vector<const char *> argv;
    argv.reserve(args.size());
    for (const auto &a : args) {
        argv.push_back(a.c_str());
    }
    char err[512];
    err[0] = '\0';
    char *json = mystilink_liuyao_run(static_cast<int>(argv.size()), argv.data(), err, sizeof(err));
    if (!json) {
        throw std::runtime_error(err[0] ? err : "mystilink_liuyao_run failed");
    }
    std::string out(json);
    mystilink_liuyao_free(json);
    return out;
}

inline std::string cast(int seed = -1, const std::string &throws = "") {
    char err[512];
    err[0] = '\0';
    char *json = mystilink_liuyao_cast(
        seed,
        throws.empty() && seed >= 0 ? 1 : 0,
        throws.empty() ? nullptr : throws.c_str(),
        err,
        sizeof(err)
    );
    if (!json) {
        throw std::runtime_error(err[0] ? err : "cast failed");
    }
    std::string out(json);
    mystilink_liuyao_free(json);
    return out;
}

}  // namespace liuyao
}  // namespace mystilink

#endif
