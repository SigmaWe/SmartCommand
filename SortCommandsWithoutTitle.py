import json

with open('CommandsWithoutTitle.json', 'r') as read_file:
  commands_no_title = json.load(read_file)

command_id_no_title = []

for command in commands_no_title:
  command_id_no_title.append(command["command_id"])

command_id_no_title.sort()

commands_no_title_sorted = []

for command_id in command_id_no_title:
  commands_no_title_sorted.append({"command_id": command_id,
                                   "command_title": ""})

with open('CommandsWithoutTitle.json', 'w') as f_out:
  json.dump(commands_no_title_sorted, f_out, indent=2)

print(len(commands_no_title_sorted))