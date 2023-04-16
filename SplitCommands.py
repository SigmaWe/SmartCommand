import json

with open('AllKeybindingCommands.json', 'r') as read_file:
  all_commands = json.load(read_file)

commands_title = []
commands_no_title = []

for command in all_commands:
  if command["command_title"] != "":
    commands_title.append(command)
  else:
    commands_no_title.append(command)

print("Number of commands:", len(all_commands))
print("Number of commands with title:", len(commands_title))
print("Number of commands without title:", len(commands_no_title))

with open('CommandsWithTitle.json', 'w') as f_out:
  json.dump(commands_title, f_out, indent=2)

with open('CommandsWithoutTitle.json', 'w') as f_out:
  json.dump(commands_no_title, f_out, indent=2)