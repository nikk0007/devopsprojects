from kubernetes import client, config
import pandas as pd

def get_roles_and_bindings(api_instance):
    roles = api_instance.list_cluster_role()
    role_bindings = api_instance.list_cluster_role_binding()
    return roles.items, role_bindings.items

def get_cluster_roles_and_bindings(api_instance):
    cluster_roles = api_instance.list_cluster_role()
    cluster_role_bindings = api_instance.list_cluster_role_binding()
    return cluster_roles.items, cluster_role_bindings.items

def extract_permissions(roles, role_bindings, cluster_roles, cluster_role_bindings):
    permissions = []
    
    for role in roles:
        role_name = role.metadata.name
        if not role_name.startswith("system:") and role.metadata.namespace not in ["kube-node-lease", "kube-public", "kube-system"]:
          for rule in role.rules:
            print(role.metadata.namespace)
            if rule.resources:
                for resource in rule.resources:
                    for verb in rule.verbs:
                        permissions.append((role.metadata.namespace, role_name, "Role", "", resource, verb))
    
    for binding in role_bindings:
        if binding.metadata.namespace not in ["kube-node-lease", "kube-public", "kube-system"]:
          if binding.subjects:
            for subject in binding.subjects:
                role_name = binding.role_ref.name  # Accessing the role name directly
                if not role_name.startswith("system:"):
                 for rule in role.rules:
                    if rule.resources:
                        for resource in rule.resources:
                            for verb in rule.verbs:
                                permissions.append((binding.metadata.namespace, role_name, "RoleBinding", subject.name, resource, verb))
    
    for cluster_role in cluster_roles:
        role_name = cluster_role.metadata.name
        if not role_name.startswith("system:") and cluster_role.metadata.namespace not in ["kube-node-lease", "kube-public", "kube-system"]:
          for rule in cluster_role.rules:
            if rule.resources:
                for resource in rule.resources:
                    for verb in rule.verbs:
                        permissions.append((cluster_role.metadata.namespace or "cluster-wide", role_name, "ClusterRole", "", resource, verb))
    
    for binding in cluster_role_bindings:
        if binding.metadata.namespace not in ["kube-node-lease", "kube-public", "kube-system"]:
          if binding.subjects:
            for subject in binding.subjects:
                role_name = binding.role_ref.name  # Accessing the role name directly
                if not role_name.startswith("system:"):
                  for rule in cluster_role.rules:
                    if rule.resources:
                        for resource in rule.resources:
                            for verb in rule.verbs:
                                permissions.append((binding.metadata.namespace or "cluster-wide", role_name, "ClusterRoleBinding", subject.name, resource, verb))
    
    return permissions


def create_excel_sheet(permissions):
    df = pd.DataFrame(permissions, columns=['Namespace', 'Role/Binding Name', 'Type', 'Subject', 'Resource', 'Verb'])
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
