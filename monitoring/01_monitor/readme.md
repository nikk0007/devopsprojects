On local k8s cluster using Docker Desktop:

install helm

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

helm repo update
helm install prometheus prometheus-community/prometheus

check for prometheus-server service and checnge it to NodePort type:
>k get svc
>k edit svc prometheus-server
>k get svc

OR use the below command to change it to NodePort type:
>kubectl expose service prometheus-server --type=NodePort --target-port=9090 --name=prometheus-server-ext

Now access this service on browser on localhost to acess Prometheus UI:
http://localhost:30286/

=================================

GRAFANA

>helm repo add grafana https://grafana.github.io/helm-charts
>helm repo update
>helm install grafana grafana/grafana
>helm list
>k get secret

now get the grafana default password using
>k get secret
>kubectl get secret --namespace default grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo

- now use "admin" as username and the decoded passcode 
- add Prometheus as the data source(use prometheus internal IP and ports)












