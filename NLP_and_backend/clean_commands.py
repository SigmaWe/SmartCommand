import re
import os
import json

def remove_repeat_commands(command_dict_list:list[dict]) -> list[dict]:
    """Remove commands that have the same command string

    command_dict_list: a list of commands, 
                       each a dict: 
                    {"command_id":str, "command_title":str, "command_id_normalized":str}
    """
    command_strings = [c['command_id'] for c in command_dict_list]
    unique_commands = []
    for i, command in enumerate(command_dict_list):
        if command_strings[i] not in command_strings[:i]:
            unique_commands.append(command)
    return unique_commands

def load_all_commands(jsonfile):
    with open(jsonfile) as c_f:
      all_commands = json.load(c_f)
    print ("total commands before removing repeats: ", len(all_commands))
    all_commands = remove_repeat_commands(all_commands)
    print ("total commands after removing repeats: ", len(all_commands))
    return all_commands


# %%

def normalize_a_command(s):
    """
    A command_id itself can be dot-separated, underline_separated, or in CamelCase
    """
    s = s.replace(".", " ")
    # TODO: we may need to preserve dots 
    s = s.replace("_", " ")
    s = re.findall('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', s)
    # from https://stackoverflow.com/a/29920015  
    s = " ".join(s)
    s = s.lower()
    return s


def normalize_commands(command_dict_list):
    """
    command_dict_list: a list of commands, 
                       each a dict: 
                    {"command_id":str, "command_title":str, "command_id_normalized":str}
    """
    for command_dict in command_dict_list:
        command_dict["command_id_normalized"] = normalize_a_command(command_dict['command_id'])

    return command_dict_list

#%% 

def pickle_commands(command_dict_list, save_file):
    with open(save_file, 'w') as f:
        json.dump(command_dict_list, f, indent=2)

#%% 
def main(jsonfile="command_title_list.json", savefile="commands_processed.json"):
    commands = load_all_commands(jsonfile)
    commands = normalize_commands(commands)
    pickle_commands(commands, savefile)


if __name__ == "__main__":
    main()
