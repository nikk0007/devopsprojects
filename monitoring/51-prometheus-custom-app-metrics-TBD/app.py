from prometheus_client import start_http_server, Counter, Gauge
import time

# Create a counter metric for requests
requests_counter = Counter('http_requests_total', 'Total HTTP Requests')

# Create a gauge metric for the current active users
active_users = Gauge('active_users', 'Current Active Users')

# Create another gauge metric for memory usage
memory_usage = Gauge('memory_usage_bytes', 'Memory Usage in Bytes')

# Create a gauge metric for CPU usage
cpu_usage = Gauge('cpu_usage_percentage', 'CPU Usage Percentage')

# Start an HTTP server on port 8000 to expose the metrics
start_http_server(8000)

while True:
    # Simulate some requests
    requests_counter.inc(1)

    # Update the metrics
    active_users.set(42)  # Replace with the actual value
    memory_usage.set(512 * 1024 * 1024)  # Replace with the actual memory usage in bytes
    cpu_usage.set(75.0)  # Replace with the actual CPU usage percentage

    time.sleep(1)
