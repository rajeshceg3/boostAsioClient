# C++/React Fullstack App

This project consists of a C++ backend server and a React UI frontend.

## Prerequisites

*   **C++ Backend:**
    *   A C++ compiler that supports C++11 (e.g., g++)
    *   Make
    *   OpenSSL libraries (libssl-dev or equivalent) for `cpp-httplib` (if HTTPS is used, or for some crypto functions it might link against)
    *   pthread library
*   **React UI:**
    *   Node.js (which includes npm)

## Building and Running

### 1. C++ Backend Server

1.  **Navigate to the root directory** of the project.
2.  **Build the server:**
    ```bash
    make
    ```
3.  **Run the server:**
    ```bash
    ./main
    ```
    The server will start on `http://localhost:8080`. You should see a message like "Server started on port 8080..." in the console.

### 2. React UI Frontend

1.  **Navigate to the React UI directory:**
    ```bash
    cd react-ui
    ```
2.  **Install dependencies (if you haven't already):**
    ```bash
    npm install
    ```
3.  **Start the development server:**
    ```bash
    npm start
    ```
    This will typically open the React application in your default web browser at `http://localhost:3000`. The UI will attempt to connect to the C++ backend at `http://localhost:8080/api/greet` and display the message.

## Development Notes

*   The C++ server needs to be running for the React UI to fetch data successfully.
*   CORS (Cross-Origin Resource Sharing) has been configured on the C++ server to allow requests from `http://localhost:3000` (or any origin via `*` for development).
