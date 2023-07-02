#!/bin/bash

# Check if file path is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <file_path>"
    exit 1
fi

file_path=$1

# Check if the file exists
if [ ! -e "$file_path" ]; then
    echo "File does not exist!"
    exit 1
fi

# Get the permissions of the file
permissions=$(stat -c "%A" "$file_path")

echo "Permissions of $file_path: $permissions"
