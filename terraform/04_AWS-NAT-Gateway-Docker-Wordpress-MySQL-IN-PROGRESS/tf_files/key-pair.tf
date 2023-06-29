# Creating a New Key
resource "aws_key_pair" "Key-Pair" {

  # Name of the Key
  key_name = "MyKey"

  # Adding the SSH authorized key !
  //public_key = file("~/.ssh/authorized_keys")
  public_key = file("../keys/mykey.pub")

}