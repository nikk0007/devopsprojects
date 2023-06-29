variable "REGION-1" {
  default = "us-east-1"
}

variable "REGION-2" {
  default = "us-west-2"
}

variable "REGION-1-ZONE-A" {
  default = "us-east-1a"
}

variable "REGION-1-ZONE-B" {
  default = "us-east-1b"
}

variable "REGION-2-ZONE-A" {
  default = "us-west-2a"
}

variable "REGION-2-ZONE-B" {
  default = "us-west-2b"
}

======================================================
variable "AMIS" {
  type = map(any)
  default = {
    us-east-1 = "ami-06489866022e12a14"
    us-west-2  = "ami-0947d2ba12ee1ff75"
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
