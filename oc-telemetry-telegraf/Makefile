

build:
	docker build -t juniper/nfd14-demo-oc-telemetry .

start-influxdb: build
	docker-compose -f docker-compose-influx.yml up -d

stop-influxdb:
	docker-compose -f docker-compose-influx.yml down
