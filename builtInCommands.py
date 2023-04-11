import os
import json
import subprocess
import glob
import re

def find_package_nls_files(path):
    package_nls_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if file == "package.nls.json":
                package_nls_files.append(os.path.join(root, file))
    return package_nls_files

def process_subfolders(path):
    subfolder_data = []

    for entry in os.scandir(path):
        if entry.is_dir():
            subfolder_data.extend(process_subfolders(entry.path))
        else:
            if entry.path.endswith(".contribution.ts"):
                subfolder_name = os.path.basename(os.path.dirname(entry.path))
                ts_file = entry.path

                with open(ts_file, "r") as file:
                    typescript_code = file.read()

                id_pattern = r'id:\s*[\'"](.+?)[\'"]'
                original_pattern = r'original:\s*[\'"](.+?)[\'"]'

                ids = re.findall(id_pattern, typescript_code)
                originals = re.findall(original_pattern, typescript_code)

                subfolder_data = []

                for command_value, title_value in zip(ids, originals):
                    subfolder_data.append({
                        "category": title_value,
                        "command": command_value,
                        "title": title_value,
                        "source": command_value.split('.')[0]  # Extract the prefix before the first dot as the source
                    })

    return subfolder_data



def process_package_nls_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        package_nls = json.load(file)

    command_data = []
    for key, value in package_nls.items():
        if isinstance(value, str):
            command_id = key
            parts = command_id.split('.')
            if len(parts) >= 2:
                source = parts[0]
                category = parts[1]
                command_data.append({
                    "category": category,
                    "command": command_id,
                    "title": value,
                    "source": source
                })

    return command_data

def get_subfolders(path):
    subfolders = [os.path.basename(f.path) for f in os.scandir(path) if f.is_dir()]
    return subfolders


def clone_vscode_repository(repo_url, target_dir):
    if not os.path.exists(target_dir):
        subprocess.run(["git", "clone", repo_url, target_dir])

def orig_Extension(path):
    package_nls_files = find_package_nls_files(path)
    command_data_list = []
    for package_nls_file in package_nls_files:
        command_data_list.extend(process_package_nls_file(package_nls_file))
    return command_data_list


def main():
    repo_url = "https://github.com/microsoft/vscode.git"
    target_dir = "vscode_cloned"
    output_json_file = "builtInCommandsOutput1.json"
    output_subfolders_json_file = "builtInCommandsOutput2.json"
    output_orig_extension_json_file = "origExtensionOutput.json"

    clone_vscode_repository(repo_url, target_dir)

    vscode_main_path = os.path.join(target_dir, "extensions")

    package_nls_files = find_package_nls_files(vscode_main_path)

    command_data_list = []
    for package_nls_file in package_nls_files:
        command_data_list.extend(process_package_nls_file(package_nls_file))

    with open(output_json_file, 'w', encoding='utf-8') as file:
        json.dump(command_data_list, file, ensure_ascii=False, indent=2)

    workbench_contrib_path = os.path.join(target_dir, "src", "vs", "workbench", "contrib")
    subfolder_data = process_subfolders(workbench_contrib_path)

    with open(output_subfolders_json_file, 'w', encoding='utf-8') as file:
        json.dump(subfolder_data, file, ensure_ascii=False, indent=2)

    # Call orig_Extension function and save the results to origExtensionOutput.json
    orig_extension_data = orig_Extension(vscode_main_path)
    with open(output_orig_extension_json_file, 'w', encoding='utf-8') as file:
        json.dump(orig_extension_data, file, ensure_ascii=False, indent=2)

    # Load the data from builtInCommandsOutput1.json, builtInCommandsOutput2.json and origExtensionOutput.json
    with open(output_json_file, 'r', encoding='utf-8') as file:
        data_output1 = json.load(file)
    with open(output_subfolders_json_file, 'r', encoding='utf-8') as file:
        data_output2 = json.load(file)
    with open(output_orig_extension_json_file, 'r', encoding='utf-8') as file:
        data_output3 = json.load(file)

    # Combine the data
    combined_data = data_output1 + data_output2 + data_output3

    # Write the combined data to output.json
    with open("builtInCommandsOutput.json", 'w', encoding='utf-8') as file:
        json.dump(combined_data, file, ensure_ascii=False, indent=2)

    return combined_data
