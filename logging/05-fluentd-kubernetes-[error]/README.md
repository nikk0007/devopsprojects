the fluentd `tail` plugin is used to read logs from containers and pods on the file system and collect them.

It is recommended to use manifests from the official fluentd for production:
https://github.com/fluent/fluentd-kubernetes-daemonset

The manifests found here are purely for demo purpose. 
The manifests in this repo are broken down and simplified.

In this example I will use the most common use case and we'll break it down to get an understanding of each component.

## Fluentd Docker

I would recommend to start with the official fluentd docker image:
https://hub.docker.com/r/fluent/fluentd/
 
You may want to build your own image if you want to install plugins.
In this demo we will be using the `fluentd` elasticsearch plugin 
It's pretty simple to adjust `fluentd` to send logs to any other destination in case you are not an `elasticsearch` user. 
So here we will be building our OWN FLUENTD DOCKER IMAGE:
```
docker build . -t nikk007/fluentd-demo

docker push nikk007/fluentd-demo

```

## Fluentd Namespace

```
kubectl create ns fluentd

```
## Fluentd Configmap

We have 5 files in our `fluentd-configmap.yaml` :
* fluent.conf: Our main config which includes all other configurations
* pods-kind-fluent.conf: `tail` config that sources all pod logs on the `kind` cluster.
  Note: `kind` cluster writes its log in a different format
* pods-fluent.conf: `tail` config that sources all pod logs on the `kubernetes` host in the cloud. 
  Note: When running K8s in the cloud, logs may go into JSON format.
* file-fluent.conf: `match` config to capture all logs and write it to file for testing log collection 
  Note: This is great to test if collection of logs works
* elastic-fluent.conf: `match` config that captures all logs and sends it to `elasticseach`

Let's deploy our `configmap`:

```
kubectl apply -f .\monitoring\logging\fluentd\kubernetes\fluentd-configmap.yaml

```

## Fluentd Daemonset

Let's deploy our `daemonset`:

```
kubectl apply -f fluentd-rbac.yaml 
kubectl apply -f fluentd.yaml
kubectl -n fluentd get pods

```

Let's deploy our example app that writes logs to `stdout`

```
kubectl apply -f counter.yaml
kubectl get pods

```

## Demo ElasticSearch and Kibana

```
kubectl create ns elastic-kibana

# deploy elastic search
kubectl -n elastic-kibana apply -f .\elastic\elastic-demo.yaml
kubectl -n elastic-kibana get pods

# deploy kibana
kubectl -n elastic-kibana apply -f .\elastic\kibana-demo.yaml
kubectl -n elastic-kibana get pods
```

## Kibana

```
kubectl -n elastic-kibana port-forward svc/kibana 5601
```