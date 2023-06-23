#!/bin/bash

# Application details
app_name="myapp"
app_dir="/path/to/app"

# Git repository
git_repo="https://github.com/username/myapp.git"
git_branch="main"

# Clone or update the repository
if [ -d "$app_dir" ]; then
  # Directory already exists, update the code
  cd "$app_dir"
  git pull origin "$git_branch"
else
  # Directory doesn't exist, clone the repository
  git clone -b "$git_branch" "$git_repo" "$app_dir"
fi

# Additional deployment steps
cd "$app_dir"
# Run any build steps, dependency installations, etc.

# Restart application server
sudo systemctl restart myapp
