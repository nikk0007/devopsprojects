# Configure the AWS provider
provider "aws" {
  region = "us-east-1" # Replace with your desired region
}

# Create a key pair for the EC2 instance
resource "aws_key_pair" "my_ec2_key_pair" {
  key_name   = "mykey"                   # Replace with your desired key name
  public_key = file("../keys/mykey.pub") # Replace with the path to your public key file
}

# Create an EC2 instance
resource "aws_instance" "my_ec2_instance" {
  ami           = "ami-0aedf6b1cb669b4c7" # This is Centos Linux AMI. Replace with your desired AMI
  instance_type = "t2.medium"             # Replace with your desired instance type

  # Configure the security group to allow incoming HTTP (port 8080) traffic
  vpc_security_group_ids = [aws_security_group.my_ec2_security_group.id]
  key_name               = aws_key_pair.my_ec2_key_pair.key_name

  tags = {
    Name = "TestEC2Instance"
  }
  depends_on = [aws_security_group.my_ec2_security_group]

  provisioner "remote-exec" {
    inline = [
      "sudo mkdir /tempp",
      "echo Remote Exec Completed!",
    ]

    connection {
      host        = aws_instance.my_ec2_instance.public_ip
      type        = "ssh"
      user        = "centos"
      private_key = file("../keys/mykey")
    }
  }

  provisioner "local-exec" {
    command = <<EOT
      echo "Local Exec Started"
      ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u centos -i ${aws_instance.my_ec2_instance.public_ip}, --private-key ../keys/mykey -e 'pub_key=../keys/mykey.pub' ../ansible/nexus-playbook.yaml
      EOT
  }

}

# Create a security group allowing all inbound and outbound traffic
resource "aws_security_group" "my_ec2_security_group" {
  name        = "MyEC2SecurityGroup"
  description = "Security group for EC2 instance"

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
    Name = "MyEC2SecurityGroup"
  }
}

output "my_sg" {
  value = aws_security_group.my_ec2_security_group.id
}

output "my_ec2_public_ip" {
  value = aws_instance.my_ec2_instance.public_ip
}