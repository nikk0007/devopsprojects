#!/bin/bash

# Threshold for disk usage (%)
threshold=90

# Get disk usage percentage. sed command here is to remove the %age sign
disk_usage=$(df -h | grep "/dev/" | awk '{ print $5 }' | sed 's/%//')

# Check if disk usage exceeds the threshold
if [ "$disk_usage" -ge "$threshold" ]; then
  # Send alert
  echo "Disk usage is above the threshold. Current usage: $disk_usage%"
  # Add logic to send email, trigger notifications, etc.
else
  echo "Disk usage is within the threshold. Current usage: $disk_usage%"
fi
