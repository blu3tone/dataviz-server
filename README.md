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

3.1  ElasticSearch
mkdir elasticsearch; cd elasticsearch

wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.2.2.deb

sudo dpkg -i elasticsearch-5.2.2.deb

3.2  Kibana

4. Register the foottraffic data schema to the Schema Registry server and load the data to the Kafka:

python readurl.py | ./bin/kafka-avro-console-producer --broker-list localhost:9092 --topic test-elasticsearch-sink --property value.schema='{"type": "record","name": "opendata","fields": [ {"name": "uid", "type": "long"},{"name": "n","type": "int"},{"name": "type", "type": "int"},{"name": "time", "type": "double"},{"name":"exitv", "type": "double"}]}'


Note that Confluent uses avro schema, and we define the avro schema for foot data traffic as follows: 

Data:

{"uid":"1578491135641261986","n":0,"type":1,"time":1515652581.100507,"exitv":-1.2196424841942493}

{"uid":"1527786296288744591","n":1,"type":1,"time":1515652580.260067,"exitv":-0.5785242144177053}

{"uid":"1578491135641261986","n":0,"type":1,"time":1515652589.100508,"exitv":-1.3053659701459766}

{"uid":"1578491135641261986","n":1,"type":1,"time":1515652591.100509,"exitv":-1.7864380367093664}

{"uid":"1578491135641261986","n":1,"type":1,"time":1515652591.10051,"exitv":-1.7021117657779847}


Schema: 

'{ "type": "record",

   "name": "opendata",
   
   "fields": [ {"name": "uid", "type": "long"},
   
              {"name": "n","type": "int"},
              
              {"name": "type", "type": "int"},
              
              {"name": "time", "type": "double"},
              
              {"name":"exitv", "type": "double"}
        
        ]}'
        

5. Load the ElasticSearch-sink (in Kafka Connect):
bin/confluent load elasticseach-sink

The outputs are: 

6. View the results:
-View with command: curl -XGET 'http://localhost:9200/test-elasticsearch-sink/_search?pretty'



{

  "took" : 53,
  
  "timed_out" : false,
  
  "_shards" : {
  
    "total" : 5,
    
    "successful" : 5,
    
    "failed" : 0
    
  },
  
  "hits" : {
  
    "total" : 42,
    
    "max_score" : 1.0,
    
    
    "hits" : [ {
    
      "_index" : "test-elasticsearch-sink",
      
      "_type" : "kafka-connect",
      
      "_id" : "test-elasticsearch-sink+0+4",
      
      "_score" : 1.0,
      
      "_source" : {
      
        "uid" : "1578491135641261986",
        
        "n" : 1,
        
        "type" : 1,
        
        "time" : 1.51564734710012E9,
        
        "exitv" : -1.2873750736468446
        
      }
      
    }, {
    
      "_index" : "test-elasticsearch-sink",
      
      "_type" : "kafka-connect",
      
      "_id" : "test-elasticsearch-sink+0+0",
      
      "_score" : 1.0,
      
      "_source" : {
      
        "uid" : "1523977911038645569",
        
        "n" : 1,
        
        "type" : 1,
        
        "time" : 1.515647344206663E9,
        
        "exitv" : 0.6841413703674778
        
      }
    }, {
    
      "_index" : "test-elasticsearch-sink",
      
      "_type" : "kafka-connect",
      
      "_id" : "test-elasticsearch-sink+0+11",
      
      "_score" : 1.0,
      
      "_source" : {
      
        "uid" : "1523979445533152588",
        
        "n" : 1,
        
        "type" : 1,
        
        "time" : 1.515647356111992E9,
        
        "exitv" : -2.1120907174809274
        
      }
    }, {
    
    
    
      "_index" : "test-elasticsearch-sink",
      "_type" : "kafka-connect",
      "_id" : "test-elasticsearch-sink+0+9",
      "_score" : 1.0,
      "_source" : {
        "uid" : "1523977911038645569",
        "n" : 0,
        "type" : 1,
        "time" : 1.515647352206666E9,
        "exitv" : 1.9189196620755813
      }
    }, {
     

-View in Kibana:
              






  
  


