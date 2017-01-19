

build:
	docker build -t juniper/nfd14-demo-oc-telemetry .

start-influxdb: build
	docker-compose -f docker-compose-influx.yml up -d

grafana-create-source:
	@echo "Create Datasource in Grafana"
	@curl 'http://admin:admin@localhost:3000/api/datasources' -X POST -H 'Content-Type: application/json;charset=UTF-8' --data-binary '{"name":"influxdb","type":"influxdb","url":"http://influxdb:8086","access":"proxy","isDefault":true,"database":"oc-telemetry"}'

stop-influxdb:
	docker-compose -f docker-compose-influx.yml down

start-aws: build
	docker-compose -f docker-compose-aws.yml up -d

stop-aws:
	docker-compose -f docker-compose-aws.yml down
