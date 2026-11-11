# Verify boostAsioClient
Boost.Asio WebSocket client: C++ websocket client (main.cpp, httplib vendor) plus a CRA react-ui control panel.
## Launch
react-ui: cd react-ui && npm install && npm start. C++ client: make (needs OpenSSL headers).
## Doctor
`python3 .cursor/skills/verify-boost-asio-client/verify.py`
## Drive
Builds the react-ui CRA app and renders it in headless Chromium asserting the boot marker and zero JS console errors.
## Evidence
`.cursor/skills/verify-boost-asio-client/evidence.json`
## Cleanup
Static/streamlit/next server terminated after the render.
## Known boundaries
C++ build not exercised: the sandbox lacks Boost/OpenSSL development headers.
