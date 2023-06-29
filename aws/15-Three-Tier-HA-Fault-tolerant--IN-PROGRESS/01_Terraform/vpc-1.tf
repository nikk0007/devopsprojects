provider "aws" {
  region = var.REGION-1
}

resource "aws_vpc" "terra-vpc-1" {
  cidr_block           = "172.20.0.0/16"
  instance_tenancy     = "default"
  enable_dns_support   = "true"
  enable_dns_hostnames = "true"
  tags = {
    Name = "terra-vpc-1"
  }
}

// 1 public subnet in each zone
resource "aws_subnet" "terra-vpc-1-Za-pub-1" {
  vpc_id                  = aws_vpc.terra-vpc-1.id
  cidr_block              = "172.20.1.0/24"
  map_public_ip_on_launch = "true"
  availability_zone       = var.REGION-1-ZONE-A
  tags = {
    Name = "terra-vpc-1-Za-pub-1"
  }
}

resource "aws_subnet" "terra-vpc-1-Zb-pub-2" {
  vpc_id                  = aws_vpc.terra-vpc-1.id
  cidr_block              = "172.20.2.0/24"
  map_public_ip_on_launch = "true"
  availability_zone       = var.REGION-1-ZONE-B
  tags = {
    Name = "terra-vpc-1-Zb-pub-1"
  }
}


// 3 private subnets in each zone///////////////////////////
resource "aws_subnet" "terra-vpc-1-Za-priv-3" {
  vpc_id                  = aws_vpc.terra-vpc.id
  cidr_block              = "172.20.3.0/24"
  map_public_ip_on_launch = "true"
  availability_zone       = var.REGION-1-ZONE-A
  tags = {
    Name = "terra-vpc-1-Za-priv-3"
  }
}

resource "aws_subnet" "terra-vpc-1-Za-priv-5" {
  vpc_id                  = aws_vpc.terra-vpc.id
  cidr_block              = "172.20.5.0/24"
  map_public_ip_on_launch = "true"
  availability_zone       = var.REGION-1-ZONE-A
  tags = {
    Name = "terra-vpc-1-Za-priv-5"
  }
}

resource "aws_subnet" "terra-vpc-1-Za-priv-7" {
  vpc_id                  = aws_vpc.terra-vpc.id
  cidr_block              = "172.20.7.0/24"
  map_public_ip_on_launch = "true"
  availability_zone       = var.REGION-1-ZONE-A
  tags = {
    Name = "terra-vpc-1-Za-priv-7"
  }
}
  
///////////////////////////////////////////////

resource "aws_subnet" "terra-vpc-1-Zb-priv-4" {
  vpc_id                  = aws_vpc.terra-vpc.id
  cidr_block              = "172.20.4.0/24"
  map_public_ip_on_launch = "true"
  availability_zone       = var.REGION-1-ZONE-B
  tags = {
    Name = "terra-vpc-1-Zb-priv-4"
  }
}

resource "aws_subnet" "terra-vpc-1-Zb-priv-6" {
  vpc_id                  = aws_vpc.terra-vpc.id
  cidr_block              = "172.20.6.0/24"
  map_public_ip_on_launch = "true"
  availability_zone       = var.REGION-1-ZONE-B
  tags = {
    Name = "terra-vpc-1-Zb-priv-6"
  }
}

resource "aws_subnet" "terra-vpc-1-Zb-priv-8" {
  vpc_id                  = aws_vpc.terra-vpc.id
  cidr_block              = "172.20.8.0/24"
  map_public_ip_on_launch = "true"
  availability_zone       = var.REGION-1-ZONE-B
  tags = {
    Name = "terra-vpc-1-Zb-priv-8"
  }
}

//////////////////  END  /////////////////////////////




resource "aws_internet_gateway" "terra-vpc-1-IGW" {
  vpc_id = aws_vpc.terra-vpc-1.id
  tags = {
    Name = "terra-vpc-1-IGW"
  }
}



resource "aws_route_table" "terra-vpc-1-pub-RT" {
  vpc_id = aws_vpc.terra-vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.terra-vpc-1-IGW.id
  }

  tags = {
    Name = "terra-vpc-1-IGW"
  }
}


resource "aws_route_table_association" "terra-pub-1-a" {
  subnet_id      = aws_subnet.terra-pub-1.id
  route_table_id = aws_route_table.terra-pub-RT.id
}

resource "aws_route_table_association" "terra-pub-2-a" {
  subnet_id      = aws_subnet.terra-pub-2.id
  route_table_id = aws_route_table.terra-pub-RT.id
}
resource "aws_route_table_association" "terra-pub-3-a" {
  subnet_id      = aws_subnet.terra-pub-3.id
  route_table_id = aws_route_table.terra-pub-RT.id
}
