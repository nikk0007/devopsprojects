we will create 4 Ubuntu t2.medium EC2 using terraform:
- terraform init
- terraform fmt
- terraform validate
- terraform apply --auto-approve


then install docker on all of them using Ansible:
- ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u ubuntu -i 44.202.6.215,44.202.9.183,52.91.189.92,44.203.251.160, --private-key ../keys/mykey -e 'pub_key=../keys/mykey.pub' docker-playbook.yaml

we will be using 1 EC2 for installing Rancher and other 3 will be used to install controlplane, etcd and worker node components. So all 3 EC2s will behave as separate clusters.

We will then use Rancher to bootstrap the other 3 EC2s with Kubernetes.
Execute this on first EC2:
- mkdir volume
- docker run -d --name rancher-server  -v ${PWD}/volume:/var/lib/rancher --restart=unless-stopped -p 80:80 -p 443:443 --privileged rancher/rancher

Now access EC2 public IP to access Rancher UI. Fetch the password by running this in EC2:
- docker logs rancher-server | grep "Bootstrap Password:"

Then get the bootstrapping command from rancher UI and run it on other 3 EC2s and modify the etcd, controlplane and worker flags in the end accordingly. Please note that we have added the -k flag in curl command so as to ignore the security risk of the self signed certificate of Rancher EC2:

- curl -kfL https://44.203.251.160/system-agent-install.sh | sudo  sh -s - --server https://44.203.251.160 --label 'cattle.io/os=linux' --token 659kfpl7f9ncfq96t6p6g4rpm4dp8j8xszws85wf4sx86kh8zfhc4l --ca-checksum b9c2e73ed478fa1a45bdec02b0bfaf34aa66d5b9a936c284beeac2bc42022973 --etcd --controlplane --worker





- terraform destroy --auto-approve