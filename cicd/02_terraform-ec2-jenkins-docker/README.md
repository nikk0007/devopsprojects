To setup Jenkins and docker on EC2.


create an EC2 instance using terraform:
- terraform init
- terraform validate
- terraform fmt
- terraform plan
- terraform apply -auto-approve
- terraform destroy -auto-approve


then update the ansible inventory file with EC2 public IP and local private key path and run the playbook.
this will install Jenkins and docker on EC2.
then configure docker credentials in Jenkins and then use the jenkinsfile to build a docker image, push it to dockerhub using credentials and then using this image to create a running docker container and the webpage via EC2's public IP.
