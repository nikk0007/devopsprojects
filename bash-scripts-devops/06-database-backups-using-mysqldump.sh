#!/bin/bash

# Database details
db_host="localhost"
db_user="root"
db_password="password"
db_name="mydatabase"

# Backup directory
backup_dir="/path/to/backup"

# Backup file name
backup_file="$backup_dir/backup_$(date +%Y%m%d%H%M%S).sql.gz"

# Perform database backup
mysqldump -h "$db_host" -u "$db_user" -p"$db_password" "$db_name" | gzip > "$backup_file"
