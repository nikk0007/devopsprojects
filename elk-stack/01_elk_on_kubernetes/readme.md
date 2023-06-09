I used local kubernetes cluster created using Docker Descktop.

apply the corresponding manifests in this order:
- elasticsearch > can verify it on browser using http://localhost:31335
- logstash
- filebeat
- metricbeat
- kibana

acecss kibana on localhost using NodePort > then goto Management > create index
>http://localhost:31336/

Then you will be able to see logs in Kibana.
