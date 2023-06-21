This project creates an EC2 instance using terraform and then triggers ansible playbook to be executed on this EC2. Playbook installs docker and then starts a simple container with an apache website which can be accessed on port 81 using the public IP of EC2.


- terraform init
- terraform validate
terraform fmt
terraform plan
terraform apply -auto-approve
terraform destroy -auto-approve

After provisioning EC2, terraform will keep on trying to connect to EC2 for "remote-exec" until EC2 is up and running.

================================================
It will then execute local-exec block. But as I was using WSL ubuntu on Windows, it was throwing "command not found" error as there is a "\r" i.e carriage return character. The presence of a carriage return character can occur when the Terraform configuration file contains Windows-style line endings (CRLF) instead of Unix-style line endings (LF).

To resolve this issue, you can convert the line endings in the Terraform configuration file to Unix-style using a text editor or a tool like dos2unix. Here's how you can use dos2unix to convert the line endings:
>sudo apt-get install dos2unix
>dos2unix main.tf

Now run the below command to install docker and then run our application in a docker container.
>terraform apply -auto-approve

================================================
in case you get some AWS Error, then use STS to decode it:
>aws sts decode-authorization-message --encoded-message <ENCODED MESSAGE>

check if "AWSCompromisedKeyQuarantineV2" policy is applied to user in AWS. It can be deleted. But make sure to delete and re-create the compromised credentials.

