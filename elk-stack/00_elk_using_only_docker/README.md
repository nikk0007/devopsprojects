I have implemented this POC on Windows using Docker Desktop and WSL2 Ubuntu.
To implement ELK components as Docker containers, you can follow these steps:

Start Elasticsearch container: start the Elasticsearch container using Docker. Run the following command:
>docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.14.0

This command starts the Elasticsearch container and exposes ports 9200 (HTTP) and 9300 (communication between nodes).

Use the below command to find the IP of any container:
>docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <CONTAINER NAME>
===========================================
Start Kibana container: start the Kibana container using Docker. Run the following command:
>docker run -d --name kibana -p 5601:5601 -e "ELASTICSEARCH_HOSTS=http://<elasticsearch-ip>:9200" docker.elastic.co/kibana/kibana:7.14.0

Replace <elasticsearch-ip> with the IP of the  Elasticsearch container. This command starts the Kibana container and exposes port 5601 (Kibana UI).
=================================================
Start Logstash container: start the Logstash container using Docker. Create a Logstash configuration file named logstash.conf with the required input and output configurations. For example:

input {
  beats {
    port => 5044
  }
}

output {
  elasticsearch {
    hosts => ["<elasticsearch-ip>:9200"]
  }
}

Replace <elasticsearch-ip> with the IP of Elasticsearch container.

Start the Logstash container using the following command:
>docker run -d --name logstash -p 5044:5044 -v /path/to/logstash.conf:/usr/share/logstash/pipeline/logstash.conf docker.elastic.co/logstash/logstash:7.14.0

This command starts the Logstash container, maps port 5044 (Beats input) and mounts the logstash.conf file into the container.
==========================================
Start Filebeat container: start the Filebeat container using Docker. Create a Filebeat configuration file named filebeat.yml with the required settings. For example:

filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /path/to/your/logs/*.log
output.logstash:
  hosts: ["<logstash-ip>:5044"]


Replace <logstash-ip> with the IP Logstash container.

Start the Filebeat container using the following command:
>docker run -d --name filebeat -v /path/to/filebeat.yml:/usr/share/filebeat/filebeat.yml -v /path/to/your/logs:/path/to/your/logs docker.elastic.co/beats/filebeat:7.14.0

This command starts the Filebeat container, mounts the filebeat.yml file and the log directory into the container.

That's it! You now have ELK components running as Docker containers on separate EC2 instances. Filebeat will send logs to Logstash, which in turn forwards them to Elasticsearch. Kibana can be accessed on browser using:
http://localhost:5601

create index pattern > click on discover > check logs
=======================================================

For generating logs, I am using a very simple python app on which we can access two URLs.
To run app:
>python3 my-flask-app.py

On browser:
localhost:5000
localhost:5000/user/david

==========================================================

Exercise: Similar setup can be done on EC2. We can even create separate EC2 instances, one for each of filebeat, elasticsearch, logstash and kibana. In this case we will have to use EC2 private IP addresses instead of container IPs.
==========================================================