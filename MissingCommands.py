import json
from NLP_and_backend import clean_commands

EXACT_MATCH = False

with open('AllCommands.json', 'r') as read_file:
  commands_extracted = json.load(read_file)

commands_keybindings = clean_commands.load_commands_w_shortcuts("NLP_and_backend/keybindings.json")
commands_keybindings += clean_commands.load_commands_wo_shortcuts("NLP_and_backend/keybindings.json")

command_id_extracted = []
command_id_keybindings = []

for command in commands_extracted["builtin_commands"]:
  command_id_extracted.append(command['command'])

for plugin in commands_extracted["plugin_commands"]:
  for command_info in plugin["commands"]:
    command_id_extracted.append(command_info["command"])

for command in commands_keybindings:
  command_id_keybindings.append(command["command"])

command_id_extracted = [*set(command_id_extracted)]
command_id_keybindings = [*set(command_id_keybindings)]

missing_commands_list = []
found_commands_list = []

for command_k in command_id_keybindings:
  command_found = False
  for command_e in command_id_extracted:
    if EXACT_MATCH:
      if command_k == command_e:
        found_commands_list.append(command_k)
        command_found = True
        break
    elif (command_k in command_e) or (command_e in command_k):
      found_commands_list.append(command_k)
      command_found = True
      break
  if not(command_found):
    missing_commands_list.append(command_k)

found_commands_list = [*set(found_commands_list)]
missing_commands_list = [*set(missing_commands_list)]

missing_commands_dic = {"num_missing_commands": len(missing_commands_list),
                    "missing_commands": missing_commands_list}

found_commands_dic = {"num_found_commands": len(found_commands_list),
                      "found_commands": found_commands_list}

with open('MissingCommands.json', 'w') as f_out:
  json.dump(missing_commands_dic, f_out, indent=2)

with open('FoundCommands.json', 'w') as f_out:
  json.dump(found_commands_dic, f_out, indent=2)