the python app exposes some metrics on port 8000.
we want prometheus to scrape these metrics using service monitor.

First we will dockerise the app and then deploy it on kubernetes cluster. Then create a service to access it.

docker build -t <username>/python-metrics:latest .
docker push <username>/python-metrics


We need to check how to create a new Prometheus instance that will scrape this app's metrics using a ServiceMonitor.





