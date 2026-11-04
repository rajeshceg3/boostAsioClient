#define CPPHTTPLIB_OPENSSL_SUPPORT
#include "vendor/httplib.h"
#include <iostream>
#include <stdexcept>

int main(int argc, char* argv[]) {
  try {
    unsigned long port = 8080;
    if (argc > 2) throw std::invalid_argument("Usage: main [port 0-65535]");
    if (argc == 2) {
      const std::string value(argv[1]);
      if (value.empty() || value.find_first_not_of("0123456789") != std::string::npos)
        throw std::invalid_argument("Port must contain decimal digits");
      port = std::stoul(value);
      if (port > 65535) throw std::out_of_range("Port must be 0-65535");
    }
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

    int bound_port = static_cast<int>(port);
    if (port == 0) {
      bound_port = svr.bind_to_any_port("0.0.0.0");
      if (bound_port < 0) throw std::runtime_error("Cannot bind server");
    } else if (!svr.bind_to_port("0.0.0.0", bound_port)) {
      throw std::runtime_error("Cannot bind server");
    }
    std::cout << "Server started on port " << bound_port << "..." << std::endl;
    if (!svr.listen_after_bind()) throw std::runtime_error("Listen failed");

    return 0;
  } catch (const std::exception& error) {
    std::cerr << "Server error: " << error.what() << std::endl;
    return 1;
  }
}
