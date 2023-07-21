import json

def main():
    with open("AllKeybindingCommands.json") as f_b:
        builtin_commands = json.load(f_b)
    with open("plugInCommandsOutput.json") as f_p:
        plugin_commands = json.load(f_p)
    
    plugin_commands_sim = []
    for package in plugin_commands:
        for command_p in package["commands"]:
            plugin_commands_sim.append({"command_id": command_p["command"], "command_title": command_p["title"]})

    all_commands = builtin_commands + plugin_commands_sim
    temp = []
    all_commands_final = []

    num_e = 0
    for command_dic in all_commands:
        if command_dic["command_id"] not in temp:
            temp.append(command_dic["command_id"])
            all_commands_final.append(command_dic)
            if command_dic["command_title"] == "":
                num_e += 1
    
    print(num_e, len(all_commands_final))
    
    with open('AllCommands.json', 'w', encoding='utf-8') as outfile:
        json.dump(all_commands_final, outfile, indent=2)

if __name__ == '__main__':
    main()