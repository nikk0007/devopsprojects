#!/bin/bash

# Server details
server_ip="123.45.67.89"

# Ping the server. The -c 4 flag specifies that four ICMP packets should be sent
ping -c 4 "$server_ip" > /dev/null

# Check the ping result
if [ $? -eq 0 ]; then
  echo "Server is reachable"
else
  echo "Server is unreachable"
  # Add logic to send alert/notification
fi
