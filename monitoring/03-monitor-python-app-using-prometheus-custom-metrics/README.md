# create and push docker image. check dockerfile inside the python-app folder
docker build -t nikk007/pythonapp .
docker push nikk007/pythonapp

# setup a kind cluster first and then setup kube-prometheus on it.
check folder monitoring > 02-kube-prometheus-to-monitor-k8s-cluster.

# deploy our python app and expose it via a service.
kubectl apply -n default -f kubernetes-app/deployment.yaml
kubectl apply -n default -f kubernetes-app/service.yaml

k get pods -n default
k get svc -n default

# to access the python app on localhost(http://localhost:32270/home and http://localhost:32270/metrics), use port forwarding. I am using 32270 as a random port:
kubectl port-forward svc/example-service 32270:80

# access prometheus on localhost(localhost:9090). we can check the targers, service monitors.
kubectl -n monitoring port-forward prometheus-applications-0 9090

# prometheus instance is deployed in monitoring namespace
kubectl apply -n monitoring -f service-monitor/prometheus.yaml

# service monitor is deployed in default namespace(same as the microservice deployment and service)
kubectl apply -n default -f service-monitor/servicemonitor.yaml

# access grafana dashboards on
kubectl -n monitoring port-forward svc/grafana 3000

