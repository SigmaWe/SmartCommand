import re
import os
import json


#%% 
def load_commands_w_shortcuts(json_file):
    """Load commands that have a keyboard shortcut
    """
    with open(json_file,'r') as s:
        lines = s.read()
        commands = json.loads(re.sub("^//.*",
                                     "",
                                     lines ,
                                     flags=re.MULTILINE)
                             )
    return commands 
    
def load_commands_wo_shortcuts(json_file):
    commands = []
    with open(json_file,'r') as s:
        for line in s.readlines():
            matches = re.match(r'^//\ -\ ([a-zA-Z\._]+)', line)
            if matches != None: 
                commands.append({"command":matches.group(1)})
    return commands 

def load_all_commands(jsonfile):
    commands_w_shortcuts = load_commands_w_shortcuts(jsonfile)
    commands_wo_shortcuts = load_commands_wo_shortcuts(jsonfile)
    return commands_w_shortcuts + commands_wo_shortcuts

# %%

def normalize_a_command(s):
    """
    A command itself can be dot-separated, underline_separated, or in CamelCase
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
                    {"key":str, "command":str, "when":str, "to-ebd": str}
                    to-ebd is the string to embed the command itself or its label
    """
    for command_dict in command_dict_list:
        command_dict["to_ebd"] = normalize_a_command(command_dict['command'])

    return command_dict_list

#%% 

def pickle_commands(command_dict_list, save_file):
    with open(save_file, 'w') as f:
        json.dump(command_dict_list, f, indent=2)

#%% 
def main(jsonfile="keybindings.json", savefile="commands_processed.json"):
    commands = load_all_commands(jsonfile)
    commands = normalize_commands(commands)
    pickle_commands(commands, savefile)




if __name__ == "__main__":
    main()
