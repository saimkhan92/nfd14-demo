# nfd14-demo
Demos presented during NFD14

##[JET App, Dynamic QOS](dynamic-cos)
This Dynamic COS App monitors satellite site's modems in 10 seconds interval and detects the changes in modem codes, error noise ratios and symbol rates. Then computes new COS values based on changes in modem values and generate cos configurations and dynamically pushes to site's ingess interface of MX based Edge router and also updates dynamic server db with new values.

##[Openconfig Telemetry w/ Telegraf](oc-telemetry-telegraf)
This project show how to collect Openconfig Telemetry information on a Juniper devices using an open source software name **telegraf**.
To be able to collect Openconfig Telemetry with Telegraf, Juniper developed a new input plugin name `openconfig_telemetry`
