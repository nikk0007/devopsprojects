from kubernetes import client, config
import pandas as pd
from collections import defaultdict

def get_roles_and_bindings(api_instance):
    roles = api_instance.list_cluster_role()
    return roles.items

def extract_permissions(roles):
    permissions = defaultdict(dict)
    
    for role in roles:
        print(role.metadata)
        print("====================================================")
        role_name = role.metadata.name
        if not role_name.startswith("system:") and role.metadata.namespace not in ["kube-node-lease", "kube-public", "kube-system"]:
            for rule in role.rules:
                if rule.resources:
                    for resource in rule.resources:
                        for verb in rule.verbs:
                            resource_prefix = resource.split("/")[0]
                            permissions[role_name][resource_prefix] = permissions[role_name].get(resource_prefix, set()) | {verb}
    # print(permissions)
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

    roles = get_roles_and_bindings(v1)

    permissions = extract_permissions(roles)
    create_excel_sheet(permissions)

if __name__ == "__main__":
    main()
