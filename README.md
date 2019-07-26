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

sudo systemctl daemon-reload

sudo systemctl enable elasticsearch

sudo systemctl restart elasticsearch


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

You can see here: http://45.124.95.145/app/kibana#/discover?_g=()&_a=(columns:!(_source),index:%27*%27,interval:auto,query:%27%27,sort:!(_score,desc))
            
            
            
Now, we can connect Kafka Stream with Cassandra (NoSQL).

Prerequisites:
 
 -Confluent 3.0.0
 
 -Cassandra 3.11.1
 
 
 1. Start Conluent:
 
 -cd confluent3.0.0
 
 - Start ZooKeeper:  ./bin/zookeeper-server-start ./etc/kafka/zookeeper.properties
 
 -Start  Kafka Stream: /bin/kafka-server-start ./etc/kafka/server.properties
 
 -Start Schema Registry:  /bin/schema-registry-start ./etc/schema-registry/schema-registry.properties
 
 -Start Kafka Connect: bin/connect-distributed etc/schema-registry/connect-avro-distributed.properties
 
 
 2. Start Cassandra Database: 
 
 We can use bin/cqlsh in apache-cassandra-3.11.1 to:
 
 -Create KeySpace demo:  cqlsh>CREATE KEYSPACE demo WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 3};
 
 -Create table foottraffic: 
 cqlsh>use demo
 
 cqlsh-demo> create table foottraffic (uid bigint, n tinyint, type tinyint, time double, exitv double, PRIMARY KEY (uid, time)) WITH CLUSTERING ORDER BY (time asc); 
 
3. Connector: cassandra-sink-foottraffic:

-Create file cassandra-sink-distributed-foottraffic.properties: with the following contents:

name=cassandra-sink-foottraffic

connector.class=com.datamountaineer.streamreactor.connect.cassandra.sink.CassandraSinkConnector

tasks.max=1

topics=foottraffic-topic

connect.cassandra.export.route.query=INSERT INTO foottraffic SELECT * FROM foottraffic-topic

connect.cassandra.contact.points=localhost

connect.cassandra.port=9042

connect.cassandra.key.space=demo

connect.cassandra.username=cassandra

connect.cassandra.password=cassandra

-Add plugin kafka-connect-cassandra to CLASSPATH: 
  
    . Download `Stream Reactor`(stream-reactor-release-0.2-3.0.0.tar.gz) - https://github.com/datamountaineer/stream-reactor/releases/download/v0.2/stream-reactor-release-0.2-3.0.0.tar.gz  
    
  Uncompress the file. 
  
   .export CLASSPATH=$(PWD)/stream-reactor-release-0.2-3.0.0/kafka-connect-cassandra-0.2-3.0.0-all.jar
   
   You must replasce $PWD with your path to the connector jar file. 
   
-Start Cassandra-Sink:  


   Download kafka-connect-cli -  https://github.com/Landoop/kafka-connect-tools/releases/tag/v0.5
   
   Create Connect `cassandra-sink-orders`:
   
java -jar kafka-connect-cli-0.5-all.jar create cassandra-sink-orders < cassandra-sink-distributed-orders.properties

- Restart Kafka Connect: 

    cd confluent-3.0.0
    
       bin/connect-distributed etc/schema-registry/connect-avro-distributed.properties

-Check for available connector plugins:

   curl http://localhost:8083/connector-plugins
   
   You can see cassandra-sink connector
   
4. Writing Data to Cassandra through Kafka Stream:

- python readurl.py | bin/kafka-avro-console-producer --broker-list localhost:9092 --topic foottraffic-topic --property value.schema='{"type": "record","name": "opendata","fields": [ {"name": "uid", "type": "string"},{"name": "n","type": "int"},{"name": "type", "type": "int"},{"name": "time", "type": "double"},{"name":"exitv", "type": "double"}]}'


-Check data in Cassandra Database: 
cqlsh-demo> select * from foottraffic; 


uid                 | time       | exitv     | n | type

---------------------+------------+-----------+---+------

 1578491135641261986 | 1.5161e+09 |  -2.62536 | 1 |    1
 
 1578491135641261986 | 1.5161e+09 |  -1.07685 | 2 |    1
 
 1578491135641261986 | 1.5161e+09 | -0.429762 | 1 |    1
 
 1578491135641261986 | 1.5161e+09 |  -2.72652 | 1 |    1
 
 1578491135641261986 | 1.5161e+09 |   1.84174 | 0 |    1
 
 1578491135641261986 | 1.5161e+09 |   1.54139 | 1 |    1
 
 1578491135641261986 | 1.5161e+09 | -0.840557 | 1 |    1
 
 1578491135641261986 | 1.5161e+09 | -0.369334 | 1 |    1

.....

The README.md have steps to install Confluent Kafka and ElasticSearch from these 4 URLs:
https://docs.confluent.io/current/installation/installing_cp.html#zip-and-tar-archives
https://docs.confluent.io/current/quickstart.html#quickstart
https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html#install-deb
https://docs.confluent.io/current/connect/quickstart.html
 
Deliverable 1 (16hrs): Steps 1 & 2 in README.md: Install and run Confluent 4.0.0
I read https://docs.confluent.io/current/installation/installing_cp.html#debian-and-ubuntu and completed this installation in less than 30 minutes, which requires 4 commands.
There are no github check-in's for configuration and test for this deliverable

Deliverable 2 (16hrs): Steps 3 in README.md: Install ElasticSearch
is there a good reason to use version 5.2.2? The current version is 6.1.2
I read https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html#install-deb and completed installing ElasticSearch 6.1.2 in less than 30 minutes, which requires 8 commands.
There are no github check-in's for configuration and test for this deliverable

There are no steps for Kibana installation.
I read this https://www.elastic.co/guide/en/kibana/current/deb.html#install-deb, and completed installation in less than 20 minutes, which requires 7 commands.

Deliverable 3 (16hrs): Data Filtering readurl.py (8 lines of python script to skip lines with no valid uid), averaging 2hrs per line of code.
import urllib
import sys
import json
datasource= urllib.urlopen("https://dashboard.motionloft.com/api/v1/stream?api_key=01cecfc22e99fee8a46e92f1bcd61fd3");

while (1):
	line=datasource.readline();
	if  line.find("uid")>0 : print line,
Deliverable 4 (8hrs): Define/Register Data Schema, Load data to Kafka
an example is provided here: https://docs.confluent.io/current/quickstart.html
https://sematext.com/blog/kafka-connect-elasticsearch-how-to/#
https://github.com/confluentinc/kafka-connect-elasticsearch/issues/154#issuecomment-357499243
Add to etc/kafka-connect-elasticsearch/quickstart-elasticsearch.properties: schema.ignore=true
This took me less than 20 minutes to read and to figure out the schema syntax.

The schema is a simple match to the Motionloft data record:

{"uid":"1578491135641261986","n":1,"type":1,"time":1516422900.113616,"exitv":2.3743743052653232}

'{ "type": "record",
   "name": "opendata",
   "fields": [ {"name": "uid", "type": "long"},
                  {"name": "n","type": "int"},
                  {"name": "type", "type": "int"},
                  {"name": "time", "type": "double"},
                  {"name":"exitv", "type": "double"}
                ]}'

Deliverable 5 (16hrs): Connect data stream to Kafka, Output to ElasticSearch
https://docs.confluent.io/current/connect/connect-elasticsearch/docs/elasticsearch_connector.html#quick-start
This took me 20 minutes to read and run 2 commands

Deliverable 6 (24hrs): integration and test, step 6 in README.md
Only 1 Kibana query, no integration and test cases checked into github.
Examples are provided here https://www.elastic.co/guide/en/kibana/current/tutorial-load-dataset.html


 
   
   
  
  

 
   





  
  


