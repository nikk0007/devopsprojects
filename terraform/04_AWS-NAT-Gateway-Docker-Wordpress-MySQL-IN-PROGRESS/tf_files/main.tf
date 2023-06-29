resource "aws_vpc" "custom" {

  # IP Range for the VPC
  cidr_block = "192.168.0.0/16"

  enable_dns_hostnames = true
  tags = {
    Name = "custom"
  }
}

#Create a Public Subnet with auto public IP Assignment enabled
resource "aws_subnet" "subnet1" {
  depends_on = [
    aws_vpc.custom
  ]

  # VPC
  vpc_id = aws_vpc.custom.id

  # IP Range of this subnet
  cidr_block              = "192.168.0.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true

  tags = {
    Name = "Public Subnet"
  }
}

# Create a Private Subnet
resource "aws_subnet" "subnet2" {
  depends_on = [
    aws_vpc.custom,
    aws_subnet.subnet1
  ]

  vpc_id            = aws_vpc.custom.id
  cidr_block        = "192.168.1.0/24"
  availability_zone = "us-east-1b"

  tags = {
    Name = "Private Subnet"
  }
}

# Creating an Internet Gateway
resource "aws_internet_gateway" "Internet_Gateway" {
  depends_on = [
    aws_vpc.custom,
    aws_subnet.subnet1,
    aws_subnet.subnet2
  ]

  # VPC in which it has to be created!
  vpc_id = aws_vpc.custom.id

  tags = {
    Name = "IG-Public-&-Private-VPC"
  }
}

# Create Route Table for the public subnet!
resource "aws_route_table" "Public-Subnet-RT" {
  depends_on = [
    aws_vpc.custom,
    aws_internet_gateway.Internet_Gateway
  ]

  vpc_id = aws_vpc.custom.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.Internet_Gateway.id
  }

  tags = {
    Name = "Route Table for Internet Gateway"
  }
}

# Route Table Association!
resource "aws_route_table_association" "RT-IG-Association" {

  depends_on = [
    aws_vpc.custom,
    aws_subnet.subnet1,
    aws_subnet.subnet2,
    aws_route_table.Public-Subnet-RT
  ]

  # Public Subnet ID
  subnet_id = aws_subnet.subnet1.id

  #  Route Table ID
  route_table_id = aws_route_table.Public-Subnet-RT.id
}

# Elastic IP for the NAT Gateway!
# It wouldn't make sense to have a dynamic address on a NAT device:
# -- if the address changed, that would be guaranteed to break any sessions in progress and 
# the only way to allocate a static address is by allocating an Elastic IP address (EIP)
resource "aws_eip" "Nat-Gateway-EIP" {
  depends_on = [
    aws_route_table_association.RT-IG-Association
  ]
  vpc = true
}

# NAT Gateway!
resource "aws_nat_gateway" "NAT_GATEWAY" {
  depends_on = [
    aws_eip.Nat-Gateway-EIP
  ]

  # Allocating the Elastic IP to the NAT Gateway!
  allocation_id = aws_eip.Nat-Gateway-EIP.id

  # Associating it in the Public Subnet!
  subnet_id = aws_subnet.subnet1.id
  tags = {
    Name = "Nat-Gateway_Project"
  }
}

# Route Table for the Nat Gateway!
resource "aws_route_table" "NAT-Gateway-RT" {
  depends_on = [
    aws_nat_gateway.NAT_GATEWAY
  ]

  vpc_id = aws_vpc.custom.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.NAT_GATEWAY.id
  }

  tags = {
    Name = "Route Table for NAT Gateway"
  }
}

# Creating an Route Table Association of the NAT Gateway route 
# table with the Private Subnet!
resource "aws_route_table_association" "Nat-Gateway-RT-Association" {
  depends_on = [
    aws_route_table.NAT-Gateway-RT
  ]

  #  Private Subnet ID for adding this route table to the DHCP server of Private subnet!
  subnet_id = aws_subnet.subnet2.id

  # Route Table ID
  route_table_id = aws_route_table.NAT-Gateway-RT.id
}


# Creating a Security Group for WordPress
resource "aws_security_group" "WS-SG" {

  depends_on = [
    aws_vpc.custom,
    aws_subnet.subnet1,
    aws_subnet.subnet2
  ]

  description = "HTTP, PING, SSH"

  # Name of the security Group!
  name = "webserver-sg"

  # VPC ID in which Security group has to be created!
  vpc_id = aws_vpc.custom.id

  # Created an inbound rule for webserver access!
  ingress {
    description = "HTTP for webserver"
    from_port   = 80
    to_port     = 80

    # Here adding tcp instead of http, because http is part of tcp only!
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Created an inbound rule for ping
  ingress {
    description = "Ping"
    from_port   = 0
    to_port     = 0
    protocol    = "ICMP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Created an inbound rule for SSH
  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22

    # Here adding tcp instead of ssh, because ssh in part of tcp only!
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Outward Network Traffic for the WordPress
  egress {
    description = "output from webserver"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


# Creating security group for MySQL, this will allow access only from the instances having the security group created above.
resource "aws_security_group" "MySQL-SG" {

  depends_on = [
    aws_vpc.custom,
    aws_subnet.subnet1,
    aws_subnet.subnet2,
    aws_security_group.WS-SG
  ]

  description = "MySQL Access only from the Webserver Instances!"
  name        = "mysql-sg"
  vpc_id      = aws_vpc.custom.id

  # Created an inbound rule for MySQL
  ingress {
    description     = "MySQL Access"
    from_port       = 3306
    to_port         = 3306
    protocol        = "tcp"
    security_groups = [aws_security_group.WS-SG.id]
  }

  # Created an inbound rule for SSH - This is only for Ansible on local system to install docker on this EC2.
  # we will remove this SSH permission later
  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22

    # Here adding tcp instead of ssh, because ssh in part of tcp only!
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "output from MySQL"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


# Creating security group for Bastion Host/Jump Box. Full access to anyone.
resource "aws_security_group" "BH-SG" {

  depends_on = [
    aws_vpc.custom,
    aws_subnet.subnet1,
    aws_subnet.subnet2
  ]

  description = "MySQL Access only from the Webserver Instances!"
  name        = "bastion-host-sg"
  vpc_id      = aws_vpc.custom.id

  # Created an inbound rule for Bastion Host SSH
  ingress {
    description = "Bastion Host SG"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "output from Bastion Host"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


# Creating security group for MySQL which allows only bastion host to connect & do the updates!
resource "aws_security_group" "DB-SG-SSH" {

  depends_on = [
    aws_vpc.custom,
    aws_subnet.subnet1,
    aws_subnet.subnet2,
    aws_security_group.BH-SG
  ]

  description = "MySQL Bastion host access for updates!"
  name        = "mysql-sg-bastion-host"
  vpc_id      = aws_vpc.custom.id

  # Created an inbound rule for MySQL Bastion Host
  ingress {
    description     = "Bastion Host SG"
    from_port       = 22
    to_port         = 22
    protocol        = "tcp"
    security_groups = [aws_security_group.BH-SG.id]
  }

  egress {
    description = "output from MySQL BH"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


# Launch a Webserver EC2 Instance hosting WordPress in it in public subnet!
resource "aws_instance" "webserver" {

  depends_on = [
    aws_vpc.custom,
    aws_subnet.subnet1,
    aws_subnet.subnet2,
    aws_security_group.BH-SG,
    aws_security_group.DB-SG-SSH
  ]

  ami           = "ami-053b0d53c279acc90"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.subnet1.id
  # Keyname and security group are obtained from the reference of their instances created above!
  # Here I am providing the name of the key which is already uploaded on the AWS console.
  key_name = "MyKey"

  # Security groups to use!
  vpc_security_group_ids = [aws_security_group.WS-SG.id]

  tags = {
    Name = "Webserver_From_Terraform"
  }
}


# Launch a MySQL EC2 instance in the private subnet!
resource "aws_instance" "MySQL" {
  depends_on = [
    aws_instance.webserver,
  ]

  ami           = "ami-053b0d53c279acc90"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.subnet2.id

  key_name = "MyKey"

  # Attaching 2 security groups here, 1 for the MySQL Database access by the Web-servers,
  # & other one for the Bastion Host access for applying updates & patches!
  vpc_security_group_ids = [aws_security_group.MySQL-SG.id, aws_security_group.DB-SG-SSH.id]

  tags = {
    Name = "MySQL_From_Terraform"
  }
}

# Launch a Bastion Host instance in the public subnet!
resource "aws_instance" "Bastion-Host" {
  depends_on = [
    aws_instance.webserver,
    aws_instance.MySQL
  ]

  ami           = "ami-053b0d53c279acc90"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.subnet1.id

  # Keyname and security group are obtained from the reference of their instances created above!
  key_name = "MyKey"

  # Security group ID's
  vpc_security_group_ids = [aws_security_group.BH-SG.id]
  tags = {
    Name = "Bastion_Host_From_Terraform"
  }
}

output "BastionHost_PublicIP" {
  value = aws_instance.Bastion-Host.public_ip
}

output "Wordpress_EC2_PublicIP" {
  value = aws_instance.webserver.public_ip
}

output "MySQL_EC2_PrivateIP" {
  value = aws_instance.MySQL.private_ip
}





