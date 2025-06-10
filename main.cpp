#define CPPHTTPLIB_OPENSSL_SUPPORT
#include "vendor/httplib.h"
#include <iostream>

int main() {
    httplib::Server svr;

    svr.Get("/api/greet", [](const httplib::Request &, httplib::Response &res) {
        res.set_header("Access-Control-Allow-Origin", "*");
        res.set_content("{\"message\": \"Hello from C++ backend!\"}", "application/json");
    });

    svr.Options("/api/greet", [](const httplib::Request &, httplib::Response &res) {
        res.set_header("Access-Control-Allow-Origin", "*");
        res.set_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS");
        res.set_header("Access-Control-Allow-Headers", "Content-Type");
        res.status = 204; // No Content
    });

    std::cout << "Server started on port 8080..." << std::endl;
    svr.listen("0.0.0.0", 8080);

    return 0;
}
