from kubernetes import client, config
from kubernetes.client import Configuration
from kubernetes.client.rest import ApiException
import datetime
import time

def get_node_metrics(api_instance):
    try:
        nodes = api_instance.list_node().items
        for node in nodes:
            print(f"Node: {node.metadata.name}")
            print(f"  CPU Usage: {node.usage['cpu']}")
            print(f"  Memory Usage: {node.usage['memory']}")
    except ApiException as e:
        print(f"Error getting node metrics: {e}")

def get_pod_metrics(api_instance, namespace):
    try:
        pods = api_instance.list_pod_for_all_namespaces().items
        for pod in pods:
            if pod.metadata.namespace == namespace:
                print(f"Pod: {pod.metadata.name}")
                print(f"  CPU Usage: {pod.usage['cpu']}")
                print(f"  Memory Usage: {pod.usage['memory']}")
    except ApiException as e:
        print(f"Error getting pod metrics: {e}")

def get_kube_events(api_instance, namespace):
    try:
        events = api_instance.list_namespaced_event(namespace).items
        for event in events:
            print(f"Event: {event.metadata.name}")
            print(f"  Type: {event.type}")
            print(f"  Reason: {event.reason}")
            print(f"  Message: {event.message}")
    except ApiException as e:
        print(f"Error getting Kubernetes events: {e}")

# Assuming you have an Ingress controller, adjust accordingly
def get_ingress_metrics(api_instance, namespace):
    try:
        ingresses = api_instance.list_namespaced_ingress(namespace).items
        for ingress in ingresses:
            print(f"Ingress: {ingress.metadata.name}")
            # Add metrics retrieval specific to your Ingress controller
    except ApiException as e:
        print(f"Error getting Ingress metrics: {e}")

def main():
    config.load_kube_config()

    v1 = client.CoreV1Api()
    v1beta1 = client.ExtensionsV1beta1Api()

    namespace = "your_namespace"  # Replace with your namespace

    while True:
        print(f"\nTimestamp: {datetime.datetime.now()}")

        get_node_metrics(v1)
        get_pod_metrics(v1, namespace)
        get_kube_events(v1, namespace)
        get_ingress_metrics(v1beta1, namespace)

        time.sleep(60)  # Sleep for 60 seconds

if __name__ == '__main__':
    main()
