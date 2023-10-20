goto https://artifacthub.io/ and search for Logstash. Use the official helm chart:
https://artifacthub.io/packages/helm/elastic/logstash

then cd into logstash folder
helm repo add elastic https://helm.elastic.co
helm fetch elastic/logstash --version 8.5.1
tar -xvzf logstash-8.5.1.tgz

set input and output of logstash in the values.yaml file.

we can delete the examples, makefile and readme files in all the helm charts. They are not required.


goto filebeat folder:
helm repo add elastic https://helm.elastic.co
tar -xvzf filebeat-8.5.1.tgz
configure the input and output in values.yaml

goto elasticsearch folder:
helm repo add elastic https://helm.elastic.co
tar -xvzf elasticsearch-8.5.1.tgz
here, resource requests section can be removed if running on low resources. Like I am running on docker-desktop.

goto kibana folder:
helm fetch elastic/kibana --version 8.5.1
tar -xvzf kibana-8.5.1.tgz

in their respective folders:
helm install filebeat .
helm install logstash .
helm install elasticsearch .
helm install kibana .

forgot to uncomment service section in logstash values.yaml file. Do it. then:
helm upgrade logstash .











