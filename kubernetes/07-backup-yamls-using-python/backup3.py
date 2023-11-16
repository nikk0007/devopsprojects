import os
import subprocess
import yaml

def get_resource_name(resource):
    metadata = resource.get("metadata", {})
    name = metadata.get("name")
    if not name:
        # If the resource doesn't have a specific name, use a generic one
        name = f"resource_{metadata.get('uid')}"
    return name

def backup_kube_system_resources(output_directory):
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Use kubectl to get all resources in kube-system namespace
    kubectl_command = [
        "kubectl",
        "get",
        "all,configmaps,secrets,daemonsets,deployments,statefulsets,replicasets,pods,services",
        "--namespace=kube-system",
        "-o=yaml"
    ]

    # Run the kubectl command
    try:
        resources_yaml = subprocess.check_output(kubectl_command, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running kubectl command: {e}")
        return

    # Save each resource to a separate YAML file with "---" between them
    resource_list = yaml.safe_load_all(resources_yaml)
    for idx, resource in enumerate(resource_list):
        if resource:  # Skip empty resources
            # Get resource type and name
            resource_type = resource["kind"].lower()
            resource_name = get_resource_name(resource)

            # Create a directory for each resource type if it doesn't exist
            resource_type_directory = os.path.join(output_directory, resource_type)
            os.makedirs(resource_type_directory, exist_ok=True)

            # Save the resource to a YAML file with "---" between different resources
            file_name = os.path.join(resource_type_directory, f"{resource_name}.yaml")
            with open(file_name, "a") as file:
                yaml.dump(resource, file)
                file.write("---\n")  # Add "---" as a separator between YAML documents

    print(f"Backup completed. YAML files saved in {output_directory}")

if __name__ == "__main__":
    # Specify the directory where YAML files will be saved
    backup_directory = "kube_system_backup"

    # Run the backup script
    backup_kube_system_resources(backup_directory)
