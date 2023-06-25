1. Create an EC2 instance using terraform.
- terraform init
- terraform validate
- terraform fmt
- terraform plan
- terraform apply --auto-approve
- terraform destroy --auto-approve

2. ansible playbook will trigger automatically once EC2 is provisioned. local-exec will wait for remote-exec to finish and this will ensure that ansible scripts will be executed only when the EC2 is ready.

3. Create a role in IAM with the policy given in ECR-Policy.json file. Attach this role to the EC2 instance above to give it action permissions for ECR.

4. Create a private repo named nginx in ECR using the below command:
- aws ecr create-repository --repository-name nginx --region us-east-1
this will return a json which will also have repo URI which will be used in later commands.
verify this on AWS console > ECR > repositories.

Install AWS CLI on EC2 and configure it:
- apt install unzip
- curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
- unzip awscliv2.zip
- sudo ./aws/install

5. Authenticate to ECR inside EC2:
- aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <YOUR ACCOUNT NUMBER>.dkr.ecr.us-east-1.amazonaws.com/nginx

6. create docker image using the dockerfile and html file inside EC2
- docker images
- docker build -t mynginx .
- docker images

7. Tag container and push to ECR:
- docker tag mynginx:latest <YOUR ACCOUNT NUMBER>.dkr.ecr.us-east-1.amazonaws.com/nginx:latest
- docker push <YOUR ACCOUNT NUMBER>.dkr.ecr.us-east-1.amazonaws.com/nginx:latest

Now validate the image inside ECR using dashboard.
__________________________________________________________________________







