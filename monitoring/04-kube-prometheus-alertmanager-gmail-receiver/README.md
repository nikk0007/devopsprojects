#inside helmm folder in our case:
helm fetch prometheus-community/kube-prometheus-stack --version 51.4.0
tar -xvzf <helmFileDownloaded>
cd into the extracted folder
helm install myprometh .

#To resolve node exporter pod crashloopbackoff issue:
kubectl patch ds myprometh-prometheus-node-exporter --type "json" -p '[{"op": "remove", "path" : "/spec/template/spec/containers/0/volumeMounts/2/mountPropagation"}]'
----------------------
- convert nodeexporter, kube state metrics, prometheus and grafana services to NodePort to access them in browser:
kubectl patch svc <service-name> -p '{"spec": {"type": "NodePort"}}'

Grafana credentials:
user: admin
password: prom-operator

node exporter port exposes: /metrics
kube state metrics port exposes: /metrics AND /healthz
prometheus port exposes: prometheus UI(/graph) AND prometheus metrics(/metrics)
-------------------------------------

To decode alertmenager secret to reveal its config file(This step is just for info. It is Not Required):
kubectl get secret alertmanager-myprometh-kube-prometheus-alertmanager-generated -o jsonpath='{.data.alertmanager\.yaml\.gz}' | base64 -d | gunzip > alertmanager-configs/original.yaml

Refer to the below URL for Slack/PagerDuty/Gmail receiver configuration templates:
https://grafana.com/blog/2020/02/25/step-by-step-guide-to-setting-up-prometheus-alertmanager-with-slack-pagerduty-and-gmail/


AlertManager is deployed as a statefulset and its configuration(a secret) is injected as a volume.
Passing your own configuration secret as a volume into the statefulset wont work as it will immediately revert to original configuration as it is handles by HELM.

To edit the statefulset and replace the config file secret with our new secret created in previous step: [THIS WONT WORK]
- kubectl edit statefulset alertmanager-myprom-kube-prometheus-sta-alertmanager

So, in order to inject our own Alertmanager receiver configuration, we have to make the necessary changes in helm chart's values.yaml file and then upgrade the helm chart to pick up the new values from our custom values.yaml file(i.e myvalues.yaml in this case)

- Make a copy of values.yaml and name it as myvalues.yaml
- search for the keyword "receiver" in this file and make the necessary changes in "Alertmanager configuration directives" block. Then trigger upgrade of this helm chart to reload the configuration:

helm list

- Now go inside the "helmm" folder(i.e where we had extracted out helm chart)

helm upgrade myprometh . --values myvalues.yaml

- To check helm status. It will show us the new updated Revision number
helm status myprometh

- to verify if the new configuration has been applied, we can check the current active configuration inside the alertmanager pod:

k get pods
k exec -it alertmanager-myprometh-kube-prometheus-alertmanager-0 -- /bin/sh
cat /etc/alertmanager/config_out/alertmanager.env.yaml

OR directly execute:
k exec -it alertmanager-myprometh-kube-prometheus-alertmanager-0 -- cat /etc/alertmanager/config_out/alertmanager.env.yaml
 
in case the changes are not applied in the pod, delete the pod:
k delete pod alertmanager-myprometh-kube-prometheus-alertmanager-0

In case of any issue:
- try editing the original values.yaml file itself OR
- try uninstalling and reinstalling helm chart
- check altertmanager logs:
k logs alertmanager-myprometh-kube-prometheus-alertmanager-0

Note: I have not changed the original name of the receiver(i.e "null") as it might result in certain issues due to some bug in the helm chart as mentioned in the below URLs:

https://github.com/bitnami/charts/issues/4596

https://github.com/prometheus-community/helm-charts/issues/255#issuecomment-715666986

==============================================

For setting up gmail receiver, we can use app password. To generate one:
https://support.google.com/accounts/answer/185833?hl=en

Account Settings -> Security -> Signing in to Google -> App password

- working template for config file:

 config:
    global:
      resolve_timeout: 1m
    route:
      receiver: 'null'
      group_by: ['namespace']
      group_wait: 30s
      group_interval: 1m
      repeat_interval: 5m
    receivers:
    - name: 'null'
      email_configs:
      - to: 'myemail@gmail.com'
        from: 'myprometh@gmail.com'
        smarthost: smtp.gmail.com:587
        auth_username: 'myemail@gmail.com'
        auth_identity: 'myemail@gmail.com'
        auth_password: 'abcdabcdabcdabcd'
        send_resolved: true
        tls_config:
            insecure_skip_verify: true


================================================

To check all the alerting rules in effect, we can use the following command and check the YAMLS:
k get prometheusrules

==================================================
In Grafana, add data source URL using ClusterIP of the service and their respective ports like:
http://10.110.163.172:9100




