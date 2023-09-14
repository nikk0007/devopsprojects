# For AMD64 / x86_64
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
# For ARM64
# [ $(uname -m) = aarch64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-arm64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
----------------------------------
# To create a kind cluster
kind create cluster

# to list all clusters
kind get clusters

# to delete a cluster
kind delete cluster --name <cluster-name>

# create cluster using config yaml
kind create cluster --config kind-config-cluster1.yaml --name cluster1
kind create cluster --config kind-config-cluster1.yaml --name cluster2

# to view all contexts available. Current context will be marked by an asterisk
kubectl config get-contexts

# To change context
kubectl config use-context <Context>

# to get cluster info
kubectl cluster-info --context kind-cluster1
--------------------------------------

To access a service(on localhost:32270) deployed on kind cluster, use port forwarding:
kubectl port-forward svc/example-service 32270:80
=============================================