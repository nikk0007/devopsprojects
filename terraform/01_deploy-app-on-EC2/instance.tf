resource "aws_key_pair" "my-key" {
  key_name   = "mykey"
  public_key = file(var.PUB_KEY)
}

resource "aws_instance" "my-web" {
  ami                    = var.AMIS[var.REGION]
  instance_type          = "t2.micro"
  subnet_id              = aws_subnet.terra-pub-1.id
  key_name               = aws_key_pair.my-key.key_name
  vpc_security_group_ids = [aws_security_group.mystack_sg.id]
  tags = {
    Name = "my-terra-instance"
  }
  
  provisioner "file" {
    source      = "web.sh"
    destination = "/tmp/web.sh"
  }

  provisioner "remote-exec" {

    inline = [
      "chmod +x /tmp/web.sh",
      "sudo /tmp/web.sh"
    ]
  }

  connection {
    user        = var.USER
    private_key = file("mykey")
    host        = self.public_ip
  }
  
}

resource "aws_ebs_volume" "vol_4_terra" {
  availability_zone = var.ZONE1
  size              = 3
  tags = {
    Name = "extr-vol-4-terra"
  }
}

resource "aws_volume_attachment" "atch_vol_terra" {
  device_name = "/dev/xvdh"
  volume_id   = aws_ebs_volume.vol_4_terra.id
  instance_id = aws_instance.my-web.id
}

output "PublicIP" {
  value = aws_instance.my-web.public_ip
}

  
