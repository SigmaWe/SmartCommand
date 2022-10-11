import re
import os

with open('raw_commands.txt') as f:
    lines = f.read()
f.close()

# test regex: https://regex101.com/
# regex1 extracts those commands that have a key with it
regex1 = '(?<="command": ")([a-zA-Z0-9\.]*)'
# regex2 extracts those commands that have no key with it
regex2 = '(?<=\/\/ - )([a-zA-Z0-9\.]*)'
commands_1st_half = re.findall(regex1, lines)
commands_2nd_half = re.findall(regex2, lines)

clean_command_file_name = "cleaned_commands.txt"
try:
    os.remove(clean_command_file_name)
except OSError:
    pass

with open(clean_command_file_name,'a') as f:
    for this_command in commands_1st_half:
        f.write(f"{this_command}\n")
    for this_command in commands_2nd_half:
        f.write(f"{this_command}\n")
f.close()