docker-desktop container logs are in this folder:
\\wsl.localhost\docker-desktop-data\data\docker\containers

we have copied some log files from there into our logs-source folder.
Fluentd is taking logs from this folder and then dumping them in logs-from-fluend folder as we have specified in the fluentd configuration file.

to run:
docker compose up