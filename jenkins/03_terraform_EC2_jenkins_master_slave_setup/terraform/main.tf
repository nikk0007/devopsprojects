# Configure the AWS provider
provider "aws" {
  access_key = "AKIAXDAL3MFDJNU2N2VV" #"<YOUR AWS ACCESS KEY>"
  secret_key = "blY0K2a0X/LomkqV81i8+jijIrhArhFkvOyEGO5c" # "<YOUR AWS SECRET>"
  region     = "us-east-1" # Replace with your desired region
}

# Create a key pair for the EC2 instance
resource "aws_key_pair" "jenkins_key_pair" {
  key_name   = "mykey"                   # Replace with your desired key name
  public_key = file("../keys/mykey.pub") # Replace with the path to your public key file
}

# Create an EC2 instance
resource "aws_instance" "jenkins_instance" {
  count         = 3
  ami           = "ami-053b0d53c279acc90" # Replace with your desired AMI
  instance_type = "t2.micro"              # Replace with your desired instance type

  # Configure the security group to allow incoming HTTP (port 8080) traffic
  vpc_security_group_ids = [aws_security_group.jenkins_security_group.id]

  key_name = aws_key_pair.jenkins_key_pair.key_name

  tags = {
    Name = "JenkinsInstance-${count.index + 1}"
  }
  depends_on = [aws_security_group.jenkins_security_group]
}

# Create a security group allowing all inbound and outbound traffic
resource "aws_security_group" "jenkins_security_group" {
  name        = "JenkinsSecurityGroup"
  description = "Security group for Jenkins instance"

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
    Name = "JenkinsSecurityGroup"
  }
}

output "my_sg" {
  value = aws_security_group.jenkins_security_group.id
}

output "my_ec2_public_ip" {
  value = aws_instance.jenkins_instance[*].public_ip
}
