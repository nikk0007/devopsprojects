import subprocess
import json

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

def ppp():
    # Define the kubectl command
    kubectl_command = "kubectl get pods --all-namespaces -o jsonpath='{..image}' | tr -s '[[:space:]]' '\n' | sort | uniq"

    # Execute the command and capture the output
    output = subprocess.check_output(kubectl_command, shell=True, text=True)

    # Print the output
    print(output)
    
# Run the script
if __name__ == "__main__":
    ppp()
    print("======================================")