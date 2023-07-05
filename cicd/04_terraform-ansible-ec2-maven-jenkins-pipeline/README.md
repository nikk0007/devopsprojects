Simple Jenkins pipeline using Jenkinsfile for a maven project from git repo.

create EC2 instance using terraform:
- terraform init
- terraform validate
- terraform fmt
- terraform plan
- terraform apply -auto-approve

# to destroy resources after the work is done
- terraform destroy -auto-approve


install Java, maven and Jenkins on EC2 using ansible playbook:
- ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u ubuntu -i <EC2_PUBLIC_IP>, --private-key ../keys/mykey -e 'pub_key=../keys/mykey.pub' jenkins-maven-docker-playbook.yaml

take EC2 SSH and check Jenkins, java and maven installation using these commands:
- which jenkins
- java -version
- mvn -version  (note down maven home path from the output)

install git, maven integration plugins.

In Jenkins dashboard:
Manage Jenkins > System Configuration > tools > scroll down to find Maven section > uncheck auto install > add name and then add path as noted above)

In job configuration under General Section tick Github project and provide your project url from Github- https://github.com/nikk0007/simple-java-app.git.

Under Source Code Management section click on Git radio button and provide Repository URL- https://github.com/nikk0007/simple-java-app.git
select main branch.

Can use poll SCM with * * * * * to check every minute for simplicity OR you can build it manually.

Build Now > then check /var/lib/jenkins/workspace/<JOB NAME>/target/  for the jar as output.

Jenkinsfile can use the shell script with commands to be executed in the "Deliver" stage of the Pipeline. This script finds out the name and version of the final jar from the pom file and then executes the jar.
Jar execution results in "Hello World!" printed on the screen.

Link for Jenkinsfile: https://github.com/nikk0007/simple-java-app/blob/main/Jenkinsfile

After the work is done, destroy infrastructure:
- terraform destroy -auto-approve
=================================================================


