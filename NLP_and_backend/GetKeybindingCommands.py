import clean_commands
import json

def main():
    commands_dir = clean_commands.load_all_commands("keybindings.json")
    commands_json_list = []
    for command_info in commands_dir:
        commands_json_list.append({"command_id": command_info['command'],
                                   "command_title": ""})
    with open('AllKeybindingCommands.json', 'w', encoding='utf-8') as outfile:
        json.dump(commands_json_list, outfile, indent=2)

if __name__ == '__main__':
    main()