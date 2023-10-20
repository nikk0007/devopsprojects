Using kube-prometheus to monitor a kubernetes cluster

(check kubernetes directory to find how to setup a kind cluster)
# Check your kubernetes version:
kubectl version

# check the compatibility matrix on the below link and clone the required release version:
https://github.com/prometheus-operator/kube-prometheus

git clone --depth 1 https://github.com/prometheus-operator/kube-prometheus.git -b release-0.12

# goto manifest folder. It has all the manifests to deploy the entire stack containing alertmanager, blackboxExporter, grafana, kubeStateMetrics, service monitors, nodeExporter, prometheus instance, prometheus adapter, prometheus operator, rbac rolebindings. The setup directory has all the CRDs.

# Deploy the setup directory first as it also has the namespace yaml.
kubectl create -f ./manifests/setup/

in case of any errors in CRDs, use force replace command in setup directory:
kubectl replace -f . --force

kubectl create -f ./manifests/
kubectl get pods -n monitoring


# now we can see that the prometheus operator pod will also be created. It will start looking at those CRDs.

# Fix Grafana Datasource(some bug in kube-prometheus)
edit `manifests/grafana-dashboardDatasources.yaml` and replace the datasource url endpoint with `http://prometheus-operated.monitoring.svc:9090

kubectl apply -f ./manifests/grafana-dashboardDatasources.yaml
kubectl -n monitoring delete po <grafana-pod>

# check Grafana dashboard(http://localhost:3000/) and login with default credentials(admin-admin). First do port forward:
kubectl -n monitoring port-forward svc/grafana 3000

# check prometheus instance console on localhost(http://localhost:9090/). Now we can check status > targets
kubectl -n monitoring port-forward svc/prometheus-operated 9090
=================================================

If still facing issues in node exporte pod, then use helm chart:

helm fetch prometheus-community/kube-prometheus-stack --version 51.4.0
tar -xvzf <helmFileDownloaded>
cd into the extracted folder
helm install my-prometheus .
kubectl patch ds my-prometheus-prometheus-node-exporter --type "json" -p '[{"op": "remove", "path" : "/spec/template/spec/containers/0/volumeMounts/2/mountPropagation"}]'
=============================