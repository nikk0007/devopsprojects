# Use the official PostgreSQL image as the base image
FROM postgres:latest

# Switch to the root user temporarily to perform setup
USER root

# Create a directory to be used as the volume
RUN mkdir -p /var/lib/postgresql/data

# Change ownership of the volume directory to the postgres user
RUN chown -R postgres:postgres /var/lib/postgresql/data

# Switch back to the postgres user
USER postgres
