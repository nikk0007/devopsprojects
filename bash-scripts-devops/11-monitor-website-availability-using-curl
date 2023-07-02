#!/bin/bash

# Website URL
website_url="https://www.example.com"

# Perform HTTP request. -s option to suppress output.
# -o /dev/null option to discard the response body
# The -w "%{http_code}" option is used to extract and print only the HTTP response code
http_response=$(curl -s -o /dev/null -w "%{http_code}" "$website_url")

# Check HTTP response code
if [ "$http_response" -eq 200 ]; then
  echo "Website is accessible"
else
  echo "Website is down with HTTP response code: $http_response"
  # Add logic to send notifications or take appropriate actions
fi
