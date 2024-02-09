Ensure you have the kubernetes module installed (pip install kubernetes) and proper kubeconfig setup for authentication. This script fetches the roles, rolebindings, clusterroles, and clusterrolebindings from your Kubernetes cluster using the kubernetes Python client, extracts the relevant information (role name, type, subject, resource, and verb) and creates an Excel sheet named kubernetes_permissions.xlsx.

pip install openpyxl
