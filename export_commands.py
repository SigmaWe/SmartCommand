import json
import glob
import os

def get_extension_folder():
    if os.name == 'nt':
        return os.path.join(os.getenv('USERPROFILE'), '.vscode', 'extensions')
    else:
        return os.path.join(os.path.expanduser('~'), '.vscode', 'extensions')

def get_default_keybindings_file():
    return 'package.json'

def export_commands():
    extension_folder = get_extension_folder()
    extension_json_files = glob.glob(f'{extension_folder}/**/package.json', recursive=True)

    all_commands = []

    for file in extension_json_files:
        with open(file, 'r', encoding='utf-8') as f:
            package = json.load(f)
            extension_name = package['name']

            if 'contributes' in package and 'commands' in package['contributes']:
                commands = package['contributes']['commands']

                for command in commands:
                    command['source'] = extension_name
                    all_commands.append(command)

    # Add default commands
    default_keybindings_file = get_default_keybindings_file()

    with open(default_keybindings_file, 'r', encoding='utf-8') as f:
        package = json.load(f)

        if 'contributes' in package and 'commands' in package['contributes']:
            commands = package['contributes']['commands']

            for command in commands:
                command['source'] = 'default'
                all_commands.append(command)

    output_file = "all_commands_full_info.json"

    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(all_commands, outfile, indent=2)

    print(f"All command information for all extensions and default commands have been exported to '{output_file}'.")

if __name__ == "__main__":
    export_commands()
