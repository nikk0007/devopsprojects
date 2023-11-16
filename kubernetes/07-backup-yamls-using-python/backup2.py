from kubernetes import client, config
import os
import yaml

def backup_resources(namespace, output_directory):
    # Load Kubernetes configuration from default location
    config.load_kube_config()

    # Create Kubernetes API clients
    core_api_instance = client.CoreV1Api()
    apps_api_instance = client.AppsV1Api()
    rbac_api_instance = client.RbacAuthorizationV1Api()

    # List all resources in the specified namespace
    core_resources = core_api_instance.list_namespaced_pod(namespace).items + \
                     core_api_instance.list_namespaced_service(namespace).items + \
                     core_api_instance.list_namespaced_config_map(namespace).items + \
                     core_api_instance.list_namespaced_secret(namespace).items + \
                     core_api_instance.list_namespaced_persistent_volume_claim(namespace).items + \
                     core_api_instance.list_namespaced_service_account(namespace).items

    apps_resources = apps_api_instance.list_namespaced_deployment(namespace).items

    rbac_resources = rbac_api_instance.list_namespaced_role(namespace).items + \
                     rbac_api_instance.list_namespaced_role_binding(namespace).items

    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Export each resource to a YAML file
    for resource in core_resources + apps_resources + rbac_resources:
        kind = resource.kind.lower() if resource.kind else "unknown"
        name = resource.metadata.name
        filename = os.path.join(output_directory, f"{kind}_{name}.yaml")

        with open(filename, 'w') as file:
            yaml.dump(resource.to_dict(), file)

        print(f"Exported {kind} '{name}' to {filename}")

if __name__ == "__main__":
    # Use 'kube-system' as the namespace
    backup_resources('kube-system', 'output-directory')
