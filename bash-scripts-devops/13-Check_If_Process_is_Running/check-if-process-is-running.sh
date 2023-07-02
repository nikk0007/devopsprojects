#!/bin/bash

# Check if a specific process is running

# Process name to check
process_name="nginx"

# Get the process information using ps -aux
process_info=$(ps -aux | grep -v grep | grep "$process_name")

# Check if the process exists
if [[ -n "$process_info" ]]; then
    echo "$process_name is running."
else
    echo "$process_name is not running."
fi
