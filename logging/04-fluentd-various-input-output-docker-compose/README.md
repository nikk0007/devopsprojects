# Introduction to Fluentd

## Collecting logs from files

Reading logs from a file we need an application that writes logs to a file. <br/>
Lets start one:


To just start the file-myapp service from the docker-compose yaml. It just keeps on adding sample log into the example-log.log file:
docker-compose up -d file-myapp

To stop it:
docker-compose down file-myapp


To collect the logs, lets start fluentd:
docker-compose up -d fluentd

---------------------------------------------------------

the http app sends json logs to port 9880 every 5 seconds using curl(and fluentd is listening to this port for http logs):
docker-compose up -d http-myapp

================================

Elasticsearch indez name is also defined in the fluentd config file.
==================================

uncomment the match blocks in containers-fluent.conf AND file-fluent.conf to send logs to file instead of elasticsearch
=======================================


