#!/bin/bash

# Log directory and file pattern
log_dir="/path/to/logs"
log_file_pattern="app*.log"

# Archive log files
find "$log_dir" -name "$log_file_pattern" -type f -mtime +7 -exec gzip {} \;

# Remove archived log files older than 30 days
find "$log_dir" -name "$log_file_pattern.gz" -type f -mtime +30 -delete

