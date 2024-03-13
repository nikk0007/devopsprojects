import subprocess
import json

# Function to list all Docker images
def list_all_docker_images():
    output = subprocess.check_output(["docker", "images", "--format", "{{.Repository}}:{{.Tag}}"])
    # Split the output by lines and remove any empty lines
    images = output.decode("utf-8").split('\n')
    images = [image for image in images if image.strip()]
    print(images)
    print(len(images))
    return images

# Function to list all container images in the cluster
def list_container_images():
    output = subprocess.check_output(["kubectl", "get", "pods", "-o", "json"])
    pods = json.loads(output)
    images = set()
    for item in pods['items']:
        for container in item['spec']['containers']:
            images.add(container['image'])
    print(images)
    print(len(images))
    return images

# Function to list all container images used by deployments
def list_deployments_images():
    output = subprocess.check_output(["kubectl", "get", "deployments", "-o", "json"])
    deployments = json.loads(output)
    images = set()
    for item in deployments['items']:
        for container in item['spec']['template']['spec']['containers']:
            images.add(container['image'])
    print(images)
    print(len(images))
    return images

# Function to find orphaned images
def find_orphaned_images():
    all_docker_images = set(list_all_docker_images())
    # When you use the | operator between two sets, it performs a union operation, which combines the elements of both sets, removing duplicates
    used_images = list_container_images() | list_deployments_images()
    orphaned_images = all_docker_images - used_images
    print(orphaned_images)
    print(len(orphaned_images))
    return orphaned_images

# Main function to delete orphaned images
def delete_orphaned_images():
    orphaned_images = find_orphaned_images()
    for image in orphaned_images:
        subprocess.run(["docker", "rmi", image])

# Run the script
if __name__ == "__main__":
    # delete_orphaned_images()
    # find_orphaned_images()
    # list_all_docker_images()
    # list_container_images()
    # list_deployments_images()
    find_orphaned_images()
    print("======================================")