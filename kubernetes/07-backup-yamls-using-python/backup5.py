import os
import subprocess

def backup_kube_system_resources(output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get all resource types in the kube-system namespace
    resource_types = subprocess.check_output(["kubectl", "api-resources", "--namespace=kube-system", "--verbs=list", "--no-headers", "--output=name"]).decode("utf-8").split("\n")

    # Remove empty strings from the list
    resource_types = list(filter(None, resource_types))

    # Backup each resource type
    for resource_type in resource_types:
        resource_type = resource_type.strip()
        resource_filename = f"{output_dir}/{resource_type.replace('/', '_')}_backup.yaml"

        # Use kubectl to get resources of the specified type in YAML format
        command = f"kubectl get {resource_type} --namespace=kube-system -o yaml > {resource_filename}"
        subprocess.run(command, shell=True)

        # Add '---' between different YAML documents in the same file
        with open(resource_filename, 'a') as file:
            file.write("\n---\n")

        print(f"Backup for {resource_type} saved to {resource_filename}")

if __name__ == "__main__":
    output_directory = "kube_system_backup"
    backup_kube_system_resources(output_directory)
 