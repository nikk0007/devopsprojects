we will create 4 Ubuntu t2.medium EC2 using terraform:
- terraform init
- terraform fmt
- terraform validate
- terraform plan
- terraform apply --auto-approve


then install docker on all of them using Ansible:
- ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u ubuntu -i 34.205.77.142,54.157.42.46,3.86.94.46,3.94.170.6, --private-key ../keys/mykey -e 'pub_key=../keys/mykey.pub' ../ansible/docker-playbook.yaml

we will be using 1 EC2 for installing Rancher and other 3 will be used to install controlplane, etcd and worker node components. So all 3 EC2s will behave as separate clusters.

We will then use Rancher to bootstrap the other 3 EC2s with Kubernetes.
Execute this on first EC2:
- mkdir volume
- docker run -d --name rancher-server  -v ${PWD}/volume:/var/lib/rancher --restart=unless-stopped -p 80:80 -p 443:443 --privileged rancher/rancher

Now access EC2 public IP to access Rancher UI. Fetch the password by running this in EC2:
- docker logs rancher-server | grep "Bootstrap Password:"

Now create cluster > Custom > enter some new cluster name.

Then get the bootstrapping command from rancher UI and run it on other 3 EC2s and modify the etcd, controlplane and worker flags in the end accordingly. Please note that we have added the -k flag in curl command so as to ignore the security risk of the self signed certificate of Rancher EC2:

- curl -kfL https://44.203.251.160/system-agent-install.sh | sudo  sh -s - --server https://44.203.251.160 --label 'cattle.io/os=linux' --token 659kfpl7f9ncfq96t6p6g4rpm4dp8j8xszws85wf4sx86kh8zfhc4l --ca-checksum b9c2e73ed478fa1a45bdec02b0bfaf34aa66d5b9a936c284beeac2bc42022973 --etcd --controlplane --worker

Once all nodes are in Running state, then click on 3 dots menu icon on top right and then Download KubeConfig file and save it on Rancher EC2 machine.

Then set env variable:
- export KUBECONFIG=/home/ubuntu/config.yaml

Install kubectl on Rancher EC2:
-    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
- sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

Now we can check:
- kubectl get nodes
- kubectl create deployment depp --image=nikk007/app2
==========================================================

- terraform destroy --auto-approve
=========================================================

Notes:

Multiple etcd might follow raft algorithm so thast there is only one Leader.
------------------------------------------------------------