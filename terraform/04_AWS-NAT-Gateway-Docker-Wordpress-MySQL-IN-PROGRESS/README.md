We will do the following using Terraform:

Create a Provider for AWS.
Create an AWS key pair.
Create a VPC (Virtual Private Cloud in AWS).
Create a Public Subnet with auto public IP Assignment enabled in custom VPC.
Create a Private Subnet in customer VPC.
Create an Internet Gateway for Instances in the public subnet to access the Internet.
Create a routing table consisting of the information of Internet Gateway.
Associate the routing table to the Public Subnet to provide the Internet Gateway address.

Creating an Elastic IP for the NAT Gateway.

- Static IP Address: By using an EIP, the NAT gateway always maintains the same public IP address, even if the NAT gateway is stopped and restarted. This is important because the private resources in your private subnet may have firewall rules or other configurations that rely on a consistent IP address for outbound connectivity. With a static IP address, you can avoid the need to update those configurations each time the NAT gateway changes its IP.

- Whitelisting: In some cases, you may need to whitelist the IP address of your NAT gateway with external services or partners to establish secure connections or access certain resources. Assigning an EIP allows you to provide a fixed IP address that can be whitelisted, ensuring uninterrupted access.

- DNS Filtering: If you need to apply DNS-based filtering or security controls, having a static IP address for the NAT gateway makes it easier to configure and manage such policies. You can specify the EIP in your DNS settings and apply filters or controls based on that IP.

- Logging and Monitoring: Assigning an EIP to a NAT gateway simplifies logging and monitoring activities. You can easily track and analyze traffic logs associated with the EIP, enabling better visibility into network activity and troubleshooting if needed.

- Overall, assigning an Elastic IP to a NAT gateway provides stability, consistency, and easier management for your outbound connectivity and networking configurations in a cloud environment like AWS.





Creating a NAT Gateway for MySQL instance to access the Internet (performing source NAT).
Creating a route table for the Nat Gateway Access which has to be associated with MySQL Instance.
Associating the above-created route table with MySQL instance.
Create a Security Group for the WordPress instance, so that anyone in the outside world can access the instance by SSH.
Create a Security Group for Mysql instance which allows database access to only those instances who are having the WordPress security group created in step 9.
Creating a Security Group for the Bastion Host which allows anyone in the outside world to access the Bastion Host by SSH.
Creating a Security Group for the MySQL Instance which allows only bastion host to connect & do the updates.
Launch a Webserver Instance hosting WordPress in it.
Launch a MySQL instance.
Launch a Bastion Host.
Remote access to bastion host & from there access MySQL remotely and perform configuration.
Remote access to WordPress and perform some configuration.