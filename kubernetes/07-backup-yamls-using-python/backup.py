from kubernetes import client, config
import os
import yaml

def backup_kubernetes_resources(namespace, output_directory):
    # Load Kubernetes configuration from the default kubeconfig file
    config.load_kube_config()

    # Create Kubernetes API client
    api_instance = client.CoreV1Api()

    # List all resources in the specified namespace
    resources = api_instance.list_namespaced_pod(namespace)

    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Loop through each resource and save its YAML representation to a file
    for resource in resources.items:
        resource_type = resource.kind.lower() if resource.kind else "unknown"
        resource_name = resource.metadata.name
        file_path = os.path.join(output_directory, f"{resource_type}_{resource_name}.yaml")

        # Convert resource to YAML format
        resource_yaml = client.ApiClient().sanitize_for_serialization(resource)
        yaml_content = yaml.dump(resource_yaml, default_flow_style=False)

        # Save YAML content to file
        with open(file_path, 'w') as file:
            file.write(yaml_content)

        print(f"Backup of {resource_type} '{resource_name}' saved to {file_path}")

if __name__ == "__main__":
    # Specify the namespace and output directory for the backups
    namespace_to_backup = "kube-system"
    backup_output_directory = "backup_output"

    # Execute the backup function
    backup_kubernetes_resources(namespace_to_backup, backup_output_directory)
