To setup Jenkins on EC2.


create an EC2 instance using terraform:
- terraform init
- terraform validate
- terraform fmt
- terraform plan
- terraform apply -auto-approve
- terraform destroy -auto-approve


then update the ansible inventory file with EC2 public IP and local private key path and run the playbook.

We can then use the jenkinsfile to create a simple apache website and test it using EC2 public IP

