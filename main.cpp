#include <boost/asio.hpp>
#include <iostream>

int main() {
  boost::asio::io_context io_context;

  boost::asio::ip::tcp::endpoint endpoint(boost::asio::ip::address::from_string("https://00da8604-92f0-4718-a7e0-f972c492dbd4-00-hdletiih8ftf.pike.replit.dev/"), 8080);

  boost::asio::ip::tcp::socket client_socket(io_context); 
  client_socket.connect(endpoint);

  std::string message = "Hello from client!";
  std::cout << "Client sending: " << message << std::endl; // Print the message being sent

  boost::asio::write(client_socket, boost::asio::buffer(message));

  char client_data[1024];
  boost::system::error_code error;
  size_t length = client_socket.read_some(boost::asio::buffer(client_data), error);

  if (!error) {
    std::cout << "Client received: " << std::string(client_data, length) << std::endl;
  } else {
    std::cerr << "Client error: " << error.message() << std::endl;
  }

  return 0;
}