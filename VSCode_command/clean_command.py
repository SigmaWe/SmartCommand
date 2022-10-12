import re
import os

with open('raw_commands.txt') as f:
    lines = f.read()
f.close()

def splitCommand(commands):
    cleaned_commands = []
    for this_command in commands:
        splited_command = this_command.split('.')
        this_cleaned_command = re.split('(?=[A-Z])',splited_command[-1])
        this_cleaned_command = [this_str.lower() for this_str in this_cleaned_command]
        this_cleaned_command = '_'.join(this_cleaned_command)
        if len(splited_command) > 1:
            splited_command[-1] = this_cleaned_command
            this_cleaned_command = ".".join(splited_command)
        # In case there are duplicated commands
        if this_cleaned_command not in cleaned_commands:
            cleaned_commands.append(this_cleaned_command)
    return cleaned_commands

# test regex: https://regex101.com/
# regex1 extracts those commands that have a key with it
regex1 = '(?<="command": ")([a-zA-Z0-9\.]*)'
# regex2 extracts those commands that have no key with it
regex2 = '(?<=\/\/ - )([a-zA-Z0-9\.]*)'
commands_1st_half = re.findall(regex1, lines)
commands_2nd_half = re.findall(regex2, lines)
cleaned_commands_1st_half = splitCommand(commands_1st_half)
cleaned_commands_2nd_half = splitCommand(commands_2nd_half)

clean_command_file_name = "cleaned_commands.txt"
try:
    os.remove(clean_command_file_name)
except OSError:
    pass

with open(clean_command_file_name,'a') as f:
    for this_command in cleaned_commands_1st_half:
        f.write(f"{this_command}\n")
    for this_command in cleaned_commands_2nd_half:
        f.write(f"{this_command}\n")
f.close()