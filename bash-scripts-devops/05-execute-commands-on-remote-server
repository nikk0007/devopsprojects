#!/bin/bash

# Server details
server_ip="123.45.67.89"
server_user="ubuntu"
ssh_key_path="/path/to/private/key.pem"

# SSH into the server and execute commands
ssh -i "$ssh_key_path" "$server_user@$server_ip" << EOF
  # Commands to run on the server
  sudo apt update
  sudo apt install -y nginx
  sudo systemctl start nginx
EOF
