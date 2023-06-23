variable "REGION" {
  default = "ap-south-1"
}

variable "ZONE1" {
  default = "ap-south-1a"
}

variable "ZONE2" {
  default = "ap-south-1b"
}

variable "ZONE3" {
  default = "ap-south-1c"
}

variable "AMIS" {
  type = map(any)
  default = {
    ap-south-1 = "ami-06489866022e12a14"
    us-east-1  = "ami-0947d2ba12ee1ff75"
  }
}

variable "USER" {
  default = "ec2-user"
}

variable "PUB_KEY" {
  default = "mykey.pub"
}

variable "PRIV_KEY" {
  default = "mykey"
}

variable "MYIP" {
  default = "122.162.151.174/32"
}
