terraform {
  backend "s3" {
    bucket = "terra-state-nikk"
    key    = "terraform/my_backend"
    region = "ap-south-1"
  }
}
