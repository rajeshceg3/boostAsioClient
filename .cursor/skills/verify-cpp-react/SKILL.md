---
name: verify-cpp-react
description: Build and drive boostAsioClient's actual cpp-httplib HTTP backend and production React UI, including real backend failure at phone/desktop sizes.
---
# Verify C++ React greeting
## Launch
Despite repository name, surface is cpp-httplib0.21 HTTPserver(main.cpp) and CRAReact19UI(react-ui/src/App.js). Backend defaults0.0.0.0:8080, optionaldecimal0-65535port;0 uses ownedephemeralport. Prints assignedport aftersuccessfulbind. UI APIbase buildtime REACT_APP_API_BASE_URL defaults http://localhost:8080. No auth/DB. C++requiresg++/make/OpenSSL/pthread, JSrequiresNode/npm and installedReactdependencies. No secrets.
`npm ci --prefix react-ui` then `npm ci --prefix .cursor/skills/verify-cpp-react`. Node22.12+ and Chrome installed; CHROME_PATH optional. OpenSSLheaders/libs may live in privateunpackedpackage tree. Proof used Ubuntu libssl-dev3.0.2-0ubuntu1.30 under /tmp/cpp-http-runtime/usr; hostruntime libs. No systeminstall or Replitcertification.
## Doctor
`python3 .cursor/skills/verify-cpp-react/helpers/verify.py doctor --openssl-root /tmp/cpp-http-runtime/usr --out .verification-evidence/cpp-react`
Read-only tool/source/dependency check. Doesnotconnectshared8080 or executeoldtrackedbinary.
## Drive
`python3 .cursor/skills/verify-cpp-react/helpers/verify.py drive --openssl-root /tmp/cpp-http-runtime/usr --out .verification-evidence/cpp-react`
BuildactualC++source throughMakefile in uniquetempdir;4invalidargs+ownedbusyport; startownedbackend0/readactualport; GETmessage/CORS, OPTIONS204 andmissing404. BuildactualReactproduction output withactualAPIbase into sametempdir. Serve viaownedloopbackport, actualbrowser390/1365 verifiesresponse text/layout. Stopownedbackend then reloadrealUI to verifyfailuremessage atbothwidths. No networkmock/proxy/internalsetter in end-to-endproof. Separate Jesttests mockAxios atordinaryHTTPboundary to cover loading/success/failure; these are supplementary, not end-to-endproof.
`CI=true npm test --prefix react-ui -- --watchAll=false --runInBand`
## Evidence
JSON, backend/frontendbuildlogs, backendlog andsuccess/failure browserJSON+screenshots. Inspectpixels forreadability. Browserpageerrors mustbeempty; stoppedbackend's expectednetwork/consoleerrors not treatedasuncaughtexceptions. Success provesactualgreeting only, notauth/TLS/load/publicdeployment. ExistingReactlock audit69findings(4critical/33high/13moderate/19low) remainsunresolved; no forceupgrade or securityacceptance.
## Cleanup
Helperstops/reaps exactownedC++child, closesbrowser, shutdown/joinownedHTTPserver, removesuniquetempbuild; evidenceoutside survives. Sourcestatuscheckedunchanged. Nevermakeclean/deleteoldtrackedmain/cache, killbyname, probespecificshared8080 or modifysettings/deploy.
## Helpers
Executable helpers/verify.py Pythonstdlib; helpers/browser.mjs actualPuppeteerbrowserpinned25.16.0. Featuremapfeatures/README.md. Use /maintain-verification-skill whenappchanges.
