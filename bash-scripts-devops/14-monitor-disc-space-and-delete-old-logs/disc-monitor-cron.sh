#!/bin/bash

# Define the threshold percentage for disk usage
threshold=80

# Define the directory where log files are located
log_directory="/var/log"

# Check disk usage
disk_usage=$(df -h --output=pcent / | awk 'NR==2 {print substr($0, 1, length($0)-1)}')

# If disk usage exceeds the threshold, delete old log files
if [[ $disk_usage -gt $threshold ]]; then
    echo "Disk usage is above threshold. Cleaning up old log files..."

    # Define the age limit for log files (in days)
    age_limit=30

    # Find and delete log files older than the age limit
    find "$log_directory" -type f -name "*.log" -mtime +$age_limit -delete

    echo "Old log files have been deleted."
else
    echo "Disk usage is within the threshold."
fi
