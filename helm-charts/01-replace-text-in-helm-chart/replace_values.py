import os
import sys
import yaml

def replace_values_in_file(file_path, replacements):
    with open(file_path, 'r') as file:
        content = file.read()

    for key, value in replacements.items():
        content = content.replace(key, value)

    with open(file_path, 'w') as file:
        file.write(content)

def process_helm_chart(chart_path, replacements):
    for subdir, _, files in os.walk(chart_path):
        for file in files:
            if file.endswith('.yaml') or file.endswith('.yml'):
                file_path = os.path.join(subdir, file)
                replace_values_in_file(file_path, replacements)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <path_to_helm_chart> <path_to_replacement_file>")
        sys.exit(1)

    helm_chart_path = sys.argv[1]
    replacement_file_path = sys.argv[2]

    # Read replacement key-value pairs from the file
    with open(replacement_file_path, 'r') as replacement_file:
        replacements_raw = replacement_file.readlines()

    replacements = {}
    for line in replacements_raw:
        key, value = map(str.strip, line.split(':'))
        replacements[key] = value

    process_helm_chart(helm_chart_path, replacements)
    print("Replacement completed successfully.")
