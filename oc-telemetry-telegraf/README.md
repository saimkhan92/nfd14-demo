
# Openconfig Telemetry Demo using Telegraf Plugin

This project show how to collect Openconfig Telemetry information on a Juniper devices
using an open source software name `telegraf`.

To be able to collect Openconfig Telemetry with Telegraf, Juniper developed a new input plugin name `openconfig_telemetry`

In this directory you'll find 2 examples of projects where telegraf collects information on a Junos devices and send it to:
 - A timeserie Database - influxdb
 - AWS cloudwatch

## Requirements
To execute this demo you need
 - docker and docker-compose installed on a server or a laptop
 - A Junos device running 16.1R3 minimum

### preparation of the Junos device

In order to be able to collect information on a Junos device, you need to:
- Junos 16.1R3 minimum
- Install the package `JUNOS Network Agent` (available on juniper.net)
- Enable gRPC on your device with the configuration below

```
set system services extension-service request-response grpc clear-text port 50051
set system services extension-service request-response grpc skip-authentication
set system services extension-service notification allow-clients address 0.0.0.0/0
```

# Demo with Influxdb

## Customize the telegraf configuration file

You need to customize telegraf configuration file (`telegraf-influxdb`) to at least indicate the IP address of your Junos device (line 84)

```
[[inputs.openconfig_telemetry]]

  server = "<device IP>:50051"
```
> Optional: You can also change the list of sensors that you want to collect starting line 93

## Start the demo

To start the demo, you need to execute `make start-influxdb`. It will start 2 containers:
1. Influxdb
2. Telegraf

## Verify that everything is running as expected

To check that data are coming into the database, you can access the Admin interface of the database on port `8083`: `http://localhost:8083`

You can also look at telegraf log to verify if telegraf is able to collect some data: `docker logs octelemetrytelegraf_telegraf_1 -f`

here is an example of logs that indicate that everything is working as expected
```
2017-01-18T02:31:32Z I! Loaded inputs: inputs.openconfig_telemetry
2017-01-18T02:31:32Z I! Tags enabled: host=6e26fb4e24cd
2017-01-18T02:31:32Z I! Agent Config: Interval:10s, Quiet:false, Hostname:"6e26fb4e24cd", Flush Interval:5s
2017-01-18T02:31:32Z I! Started OpenConfig Telemetry plugin
2017-01-18T02:31:40Z D! Input [inputs.openconfig_telemetry] gathered metrics, (10s interval) in 110.077µs
2017-01-18T02:31:45Z I! Output [influxdb] buffer fullness: 166 / 10000 metrics. Total gathered metrics: 166. Total dropped metrics: 0.
2017-01-18T02:31:45Z I! Output [influxdb] wrote batch of 166 metrics in 108.797476ms
2017-01-18T02:31:50Z D! Input [inputs.openconfig_telemetry] gathered metrics, (10s interval) in 7.751727ms
2017-01-18T02:31:50Z I! Output [influxdb] buffer fullness: 137 / 10000 metrics. Total gathered metrics: 303. Total dropped metrics: 0.
```

## stop the demo
```
make stop-influxdb
```
