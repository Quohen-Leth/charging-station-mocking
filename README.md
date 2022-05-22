Simple EV charging station emulation.
Based on OCPP v2.0.1 protocol over websockets.

To start Charging Station client web interface:
 - run `python -m src`

To start one or more Charging Stations, run station_ocpp -n <Station Name>

Supported CLI commands:
"au" - send authorization message
"br" - get base report
"st" - transaction event info