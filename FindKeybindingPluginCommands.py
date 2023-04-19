import json

with open("PlugInCommandsOutput.json", 'r') as read_file:
  plugInCommands = json.load(read_file)

plugInCommandsID = []
plugInCommandsProc = []

for package in plugInCommands:
  for command_info in package["commands"]:
    plugInCommandsID.append(command_info["command"])
    plugInCommandsProc.append(command_info)

with open("CommandsWithTitle.json", 'r') as read_file:
  keybindingCommands = json.load(read_file)

keybindingCommandsID = []

for command_info in keybindingCommands:
  keybindingCommandsID.append(command_info["command_id"])

# for plugInCommandID in plugInCommandsID:
#   if plugInCommandID in keybindingCommandsID:
#     print(plugInCommandID)

differences = []
num_matched = 0

for plugin_command_info in plugInCommandsProc:
  for keybinding_command_info in keybindingCommands:
    if keybinding_command_info["command_id"] == plugin_command_info["command"]:
      num_matched += 1
      differences.append({"command": keybinding_command_info["command_id"],
                          "keyboard_shortcuts_editor": keybinding_command_info["command_title"],
                          "plugInCommands.py": plugin_command_info["title"]})

with open('Differences.json', 'w') as f_out:
  json.dump(differences, f_out, indent=2)

print(num_matched)