from kubernetes import client, config
import pandas as pd
from collections import defaultdict

def get_roles_and_bindings(api_instance):
    roles = api_instance.list_cluster_role()
    role_bindings = api_instance.list_cluster_role_binding()
    return roles.items, role_bindings.items

def get_namespaced_roles(api_instance, namespace):
    roles = api_instance.list_namespaced_role(namespace)
    return roles.items

def get_namespaced_role_bindings(api_instance, namespace):
    role_bindings = api_instance.list_namespaced_role_binding(namespace)
    return role_bindings.items

def get_cluster_roles_and_bindings(api_instance):
    cluster_roles = api_instance.list_cluster_role()
    cluster_role_bindings = api_instance.list_cluster_role_binding()
    return cluster_roles.items, cluster_role_bindings.items

def extract_permissions(roles, role_bindings, cluster_roles, cluster_role_bindings):
    permissions = defaultdict(lambda: defaultdict(list))
    
    for role in roles:
        role_name = role.metadata.name
        namespace = role.metadata.namespace
        if not role_name.startswith("system:") and namespace not in ["kube-public", "kube-system"]:
            if role.rules:
                for rule in role.rules:
                    if rule.resources:
                        for resource in rule.resources:
                            for verb in rule.verbs:
                                resource_prefix = resource.split("/")[0]
                                permissions[role_name][resource_prefix].append(verb)
    
    for binding in role_bindings:
        namespace = binding.metadata.namespace
        if namespace not in ["kube-node-lease", "kube-public", "kube-system"]:
            if binding.subjects:
              for subject in binding.subjects:
                role_name = binding.role_ref.name  # Accessing the role name directly
                if not role_name.startswith("system:"):
                    for rule in binding.role_ref.rules:
                        if rule and rule.resources:
                            for resource in rule.resources:
                                for verb in rule.verbs:
                                    resource_prefix = resource.split("/")[0]
                                    permissions[role_name][resource_prefix].append(verb)
    
    for cluster_role in cluster_roles:
        role_name = cluster_role.metadata.name
        namespace = cluster_role.metadata.namespace or "cluster-wide"
        if not role_name.startswith("system:") and namespace not in ["kube-public", "kube-system"]:
            if cluster_role.rules:
                for rule in cluster_role.rules:
                    if rule.resources:
                        for resource in rule.resources:
                            for verb in rule.verbs:
                                resource_prefix = resource.split("/")[0]
                                permissions[role_name][resource_prefix].append(verb)
    
    for binding in cluster_role_bindings:
        namespace = binding.metadata.namespace or "cluster-wide"
        if namespace not in ["kube-node-lease", "kube-public", "kube-system"]:
            if binding.subjects:
              for subject in binding.subjects:
                role_name = binding.role_ref.name  # Accessing the role name directly
                if not role_name.startswith("system:"):
                    for rule in binding.role_ref.rules:
                        if rule and rule.resources:
                            for resource in rule.resources:
                                for verb in rule.verbs:
                                    resource_prefix = resource.split("/")[0]
                                    permissions[role_name][resource_prefix].append(verb)
    
    return permissions

def create_excel_sheet(permissions):
    flattened_permissions = []
    for role_name, resources in permissions.items():
        for resource_prefix, verbs in resources.items():
            flattened_permissions.append((
                role_name,
                "Role",
                ", ".join(verbs),
                resource_prefix,
                ", ".join(sorted(set(verbs)))
            ))
    
    df = pd.DataFrame(flattened_permissions, columns=['Role/Binding Name', 'Type', 'Subject', 'Resource', 'Verb'])
    df.to_excel('kubernetes_permissions.xlsx', index=False)

def main():
    config.load_kube_config()
    v1 = client.RbacAuthorizationV1Api()

    roles, role_bindings = get_roles_and_bindings(v1)
    cluster_roles, cluster_role_bindings = get_cluster_roles_and_bindings(v1)

    permissions = extract_permissions(roles, role_bindings, cluster_roles, cluster_role_bindings)
    create_excel_sheet(permissions)

if __name__ == "__main__":
    main()
