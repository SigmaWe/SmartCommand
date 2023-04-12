import glob
import re
import json
import subprocess
import os

def clone_vscode_repository(repo_url, target_dir):
    if not os.path.exists(target_dir):
        subprocess.run(["git", "clone", repo_url, target_dir])
    else:
        print(f"Target directory {target_dir} already exists. Skipping cloning.")

# Regular expression patterns
command_pattern = re.compile(r'"(?:command|id)":\s*"([^"]+)"')
title_pattern = re.compile(r'"(?:title|original)":\s*"([^"]+)"')
category_pattern = re.compile(r'"category":\s*"([^"]+)"')
source_pattern = re.compile(r'"source":\s*"([^"]+)"')

# Updated TypeScript patterns
ts_command_pattern = re.compile(r'id:\s*(?:\'|\")(.+?)(?:\'|\")')
ts_title_pattern = re.compile(r'title:\s*nls\.localize\((?:\'|\")([^"]+)(?:\'|\")')

def extract_commands_and_titles(file_path, file_type):
    commands_and_titles = []
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

        if file_type == "json":
            commands = command_pattern.findall(content)
            titles = title_pattern.findall(content)
            categories = category_pattern.findall(content)
            sources = source_pattern.findall(content)
        else:  # file_type == "typescript"
            commands = ts_command_pattern.findall(content)
            titles = ts_title_pattern.findall(content)
            categories = []
            sources = []

        for i, command in enumerate(commands):
            title = titles[i] if i < len(titles) else None
            category = categories[i] if i < len(categories) else None
            source = sources[i] if i < len(sources) else None
            commands_and_titles.append({
                "command": command,
                "title": title,
                "category": category,
                "source": source,
                "file_path": file_path  # Add the file path to the dictionary
            })

    return commands_and_titles



def find_missing_info(target_dir, unique_commands):
    source_path = f"{target_dir}/**/*.json"
    typescript_files = f"{target_dir}/**/*.ts"

    for file_path in glob.glob(source_path, recursive=True):
        commands_and_titles = extract_commands_and_titles(file_path, "json")
        for item in commands_and_titles:
            command_id = item["command"]
            if command_id in unique_commands:
                unique_commands[command_id].update({k: v for k, v in item.items() if v is not None and k not in unique_commands[command_id]})

    for file_path in glob.glob(typescript_files, recursive=True):
        commands_and_titles = extract_commands_and_titles(file_path, "typescript")
        for item in commands_and_titles:
            command_id = item["command"]
            if command_id in unique_commands:
                unique_commands[command_id].update({k: v for k, v in item.items() if v is not None and k not in unique_commands[command_id]})

def main():
    repo_url = "https://github.com/microsoft/vscode.git"
    target_dir = "vscode_cloned"
    clone_vscode_repository(repo_url, target_dir)

    source_path = f"{target_dir}/**/*.json"
    typescript_files = f"{target_dir}/**/*.ts"

    unique_commands = {}
    for file_path in glob.glob(source_path, recursive=True):
        commands_and_titles = extract_commands_and_titles(file_path, "json")
        for item in commands_and_titles:
            command_id = item["command"]
            if command_id in unique_commands:
                unique_commands[command_id].update({k: v for k, v in item.items() if v is not None})
            else:
                unique_commands[command_id] = item

    for file_path in glob.glob(typescript_files, recursive=True):
        commands_and_titles = extract_commands_and_titles(file_path, "typescript")
        for item in commands_and_titles:
            command_id = item["command"]
            if command_id in unique_commands:
                unique_commands[command_id].update({k: v for k, v in item.items() if v is not None})
            else:
                unique_commands[command_id] = item

    find_missing_info(target_dir, unique_commands)

    combined_data = list(unique_commands.values())

    # Write the combined data to output.json
    with open("AllCommands.json", "w", encoding="utf-8") as output_file:
        json.dump(combined_data, output_file, ensure_ascii=False, indent=2)

    # print("Commands and titles have been successfully extracted and saved to AllCommands.json.")

    return combined_data

if __name__ == "__main__":
    main()
