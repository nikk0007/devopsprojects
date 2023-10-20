Elastic search yaml will have two ports: one for accepting the data and one to send the data.

check filebeat, metricbeat modules in documentation.

metricbeat is deplyed as a daemonset as well as a deployment:
daemonset ==> for metrics from host like system metrics, docker stats, metrics from services
deployment ==> to get metrics corresponding to the whole cluster. kube-state-metrics

curator is to delete the logs periodically.

<<< Not Working. Kibana not connecting to Elasticsearch !>>>
