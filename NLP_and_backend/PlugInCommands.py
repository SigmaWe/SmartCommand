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

def main():
    extension_folder = get_extension_folder()
    extension_json_files = glob.glob(f'{extension_folder}/**/package.json', recursive=True)

    all_extensions = {}

    for file in extension_json_files:
        with open(file, 'r', encoding='utf-8') as f:
            package = json.load(f)
            try:
              extension_name = package['name']
              extension_version = package['version']  # Read the version from package.json

              if 'contributes' in package and 'commands' in package['contributes']:
                  commands = package['contributes']['commands']

                  # Group commands by extension name and version
                  key = f"{extension_name}@{extension_version}"
                  if key not in all_extensions:
                      all_extensions[key] = {
                          "source": extension_name,
                          "version": extension_version,
                          "commands": []
                      }

                  for command in commands:
                      all_extensions[key]['commands'].append(command)
            except:
                pass

    output_file = "plugInCommandsOutput.json"
    print("Commands and titles have been successfully extracted and saved to plugInCommandsOutput.json.")

    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(list(all_extensions.values()), outfile, indent=2)

    return list(all_extensions.values())

if __name__ == '__main__':
    main()
