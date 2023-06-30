use terraform script to create three t2.micro instances. Make sure to add your AWS user credentials in main.tf
Note how we have used "count" to create 3 instances and how we are displaying public IPs of all three in output.

Do remember to create a public-private key pair(mykey and mykey.pub) using ssh-keygen command and store it in a folder named "keys" inside this project folder.

from inside terraform folder:
- terraform init
- terraform validate
- terraform fmt
- terraform plan
- terraform apply -auto-approve
- terraform destroy -auto-approve
- this will also print all the public IPs of the three EC2 instances as output


from inside ansible folder:
- ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u ubuntu -i <JENKINS MASTER PUBLIC IP>, --private-key ../keys/mykey -e 'pub_key=../keys/mykey.pub' ../ansible/jenkins-master-playbook.yaml
- ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u ubuntu -i <JENKINS SLAVE_1 PUBLIC IP>, --private-key ../keys/mykey -e 'pub_key=../keys/mykey.pub' ../ansible/jenkins-slave-playbook.yaml
- ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u ubuntu -i <JENKINS SLAVE_2 PUBLIC IP>, --private-key ../keys/mykey -e 'pub_key=../keys/mykey.pub' ../ansible/jenkins-slave-playbook.yaml

Ideally, jenkins slave's security group should allow SSH only from Jenkins master. But to make things less complicated, we will be using same security groups for all EC2 instances which allows all traffic from anywhere.

- Now access jenkins dashboard using <master-public-ip>:8080
- login using initial admi password. It can be retrieved by connecting to master via SSH and check this path(/var/lib/jenkins/secrets/initialAdminPassword)
- skip setting username and password > skip installing any plugins(de-select all and proceed)
- Manage jenkins > plugins > install git, github and SSH Build Agents plugins. SSH Build Agents plugin is required for master to access slaves via SSH.
- In Jenkins dashboard > click on Setup an Agent > enter some nodeName and select as permanent agent > remote root directory: /home/ubuntu/
- enter slave EC2's private Ip in host field > add credentials > kind:SSH username with private key > ID, description, username: ubuntu(based on tha AMI we selected) > enter private key directly and paste the contents of our private key > Host Key Verification Strategy: manually trusted key verification > save
- Now agent will be successfully connected. In case of any issue, click on launch agent again.
- while adding second node as slave, we can use the option to copy all configuration from our first slave. But remember to change the private I and label.

To test:
- create a new job > select freestyle project > give any name > build steps section: execute shell and type hostname(to print private IP of EC2)
- in restrict where the project can be run option: choose slave of your choice > save > build now > check console output and verify the IP.
- now configure the job again and select the other slave this time > build > verify IP.

In case you logout, then you can login again using admin as username and initialAdminPassword we used earlier.
_______________________________________________________________________________________________

















