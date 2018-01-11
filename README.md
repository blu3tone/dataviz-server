# dataviz-server

## Please add instructions on steps to download, build, run and test your deliverables here
## Add your design documents to "docs" folder, and update docs/SUMMARY.md
## Update CHANGES.md with each deliverable check-in
In Ubuntu 16.04 (Streaming Platform) for foottraffic

1. Install Kafka Stream :
-Download Confluent 4.0.0 : wget http://packages.confluent.io/archive/4.0/confluent-oss-4.0.0-2.11.tar.gz
- Extract Confluent : tar -xzf confluent-oss-4.0.0-2.11.tar.gz to directory confluent-4.0.0

2. Start Kafka Stream: 
  cd confluent-4.0.0
  bin/confluent start
  The screen show: 
  Starting zookeeper
zookeeper is [UP]
Starting kafka
kafka is [UP]
Starting schema-registry
schema-registry is [UP]
Starting kafka-rest
kafka-rest is [UP]
Starting connect
connect is [UP]

Here, ZooKeeper, Kafka Stream, Schema Registry server, kafka Rest API Server and Kafka Connect started

3. Install ElasticSearch and Kibana

4. Register the foottraffic data schema to the Schema Registry server and load the data to the Kafka:

python readurl | ./bin/kafka-avro-console-producer --broker-list localhost:9092 --topic test-elasticsearch-sink --property value.schema='{"type": "record","name": "opendata","fields": [ {"name": "uid", "type": "long"},{"name": "n","type": "int"},{"name": "type", "type": "int"},{"name": "time", "type": "double"},{"name":"exitv", "type": "double"}]}'

Note that Confluent uses avro schema, and we define the avro schema for foot data traffic as follows: 






  
  


