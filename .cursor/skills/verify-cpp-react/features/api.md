# Backend greeting API and startup
## Sub-features
GET /api/greet returns JSONmessage, permissiveCORS; OPTIONS204; unknownpath404; optionalport anddiagnosticfailure.
## How to get to it (user POV)
Buildsource withmake, run main0or explicitport, request /api/greet onprintedport. Default8080/bind0.0.0.0preserved.
## Driving it with verify.py
Actualbuild,4invalidargs, ownedportcollision, startupreadiness andrealHTTPresponse/CORS/OPTIONS404 assertions. Noexistingserverassumption.
## Gotchas
Port0requiresbind_to_any_port pluslisten_after_bind supportedbyvendoredheader. Originalprintedstartupbeforelistenandignoredfailure, nowcorrected. Noactualpublicnetwork/TLS/securityaudit. PermissiveCORSpreserved,notnewauthorizationdesign.
