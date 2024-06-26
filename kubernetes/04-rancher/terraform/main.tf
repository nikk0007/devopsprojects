# Configure the AWS provider
provider "aws" {
  region = "us-east-1" # Replace with your desired region
}

# Create a key pair for the EC2 instance
resource "aws_key_pair" "my_aws_key_pair" {
  key_name   = "mykey"                   # Replace with your desired key name
  public_key = file("../keys/mykey.pub") # Replace with the path to your public key file
}

# Create an EC2 instance
resource "aws_instance" "ubuntu_instance" {
  count         = 4
  ami           = "ami-053b0d53c279acc90" # Replace with your desired AMI
  instance_type = "t2.medium"             # Replace with your desired instance type

  root_block_device {
    volume_size = 30  # Custom volume size in GB
  }
  
  # Configure the security group to allow incoming HTTP (port 8080) traffic
  vpc_security_group_ids = [aws_security_group.my_security_group.id]

  key_name = aws_key_pair.my_aws_key_pair.key_name

  tags = {
    Name = "UbuntuInstance-${count.index + 1}"
  }
  depends_on = [aws_security_group.my_security_group]
}

# Create a security group allowing all inbound and outbound traffic
resource "aws_security_group" "my_security_group" {
  name        = "MySecurityGroup"
  description = "Security group for Ubuntu instance"

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "UbuntuSecurityGroup"
  }
}

output "my_sg" {
  value = aws_security_group.my_security_group.id
}

output "my_ec2_public_ip" {
  value = aws_instance.ubuntu_instance[*].public_ip
}
