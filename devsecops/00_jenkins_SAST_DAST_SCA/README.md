To setup Jenkins and docker on EC2 and then run jenkins pipeline with SAST stage using jenkinsfile.
We will be using Horusec, Snyk and Owasp ZAP tools for SAST, SCA and DAST stages.
We will use OWASP Juice Shop application for testing:
Code to test: Juiceshop:
https://github.com/juice-shop/juice-shop.git

create an EC2 instance using terraform:
- terraform init
- terraform validate
- terraform fmt
- terraform plan
- terraform apply -auto-approve
- terraform destroy -auto-approve
______________________________________________

Install Jenkins and docker on EC2 using Ansible playbook. It will also output the initial Jenkins admin passcode.

- ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u ubuntu -i <EC2 PUBLIC IP>, --private-key ../keys/mykey -e 'pub_key=../keys/mykey.pub' jenkins-docker-playbook.yaml

Install git,  github and pipeline plugins on Jenkins.
_______________________________________________

Create a pipeline job in Jenkins > use the jenkinsfile provided to run the pipeline.
Check output for output of all the stages.






