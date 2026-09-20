#include <iostream>
#include <string>

#include "../../bindings/cpp/mystilink_liuyao.hpp"

int main() {
    try {
        std::string json = mystilink::liuyao::cast(123);
        std::cout << json << std::endl;
    } catch (const std::exception &ex) {
        std::cerr << "error: " << ex.what() << std::endl;
        return 1;
    }
    return 0;
}
