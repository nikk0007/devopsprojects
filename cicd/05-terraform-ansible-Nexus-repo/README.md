This project is to create an EC2 using terraform and automatically trigger ansible to copy and execute the script on it to setup exus repo.

Create a t2.medium EC2 with Centos.

- terraform init
- terraform validate
- terraform fmt
- terraform plan
- terraform apply -auto-approve

You can access nexus at port8081 using EC2 Public IP.

Destroy the infra after use:
- terraform destroy -auto-approve


In case of any windows related error regarding some extra characters like "\r". use below:
- sudo apt-get install dos2unix
- dos2unix main.tf

in case you get some AWS Error, then use STS to decode it:
- aws sts decode-authorization-message --encoded-message <ENCODED MESSAGE>

#check if "AWSCompromisedKeyQuarantineV2" policy is applied to user in AWS. It can be deleted. But make sure to delete and re-create the compromised credentials.


