import json
import glob

def search_str(file_path, word):
  with open(file_path, 'r') as file:
    # read all content of a file
    content = file.read()
    # check if string present in a file
    return (word in content)

with open('CommandsWithoutTitle.json', 'r') as read_file:
  commands_no_title = json.load(read_file)

commands_exist_id = []
commands_no_exist_id = []

for command_info in commands_no_title:
  for file_path in glob.iglob("vscode_cloned/**/*.ts", recursive=True):
    try:
      if search_str(file_path, command_info["command_id"]):
        commands_exist_id.append(command_info["command_id"])
        break
    except:
      pass

for command in commands_no_title:
  if command["command_id"] not in commands_exist_id:
    commands_no_exist_id.append(command["command_id"])

commands_exist_dic = []
commands_no_exist_dic = []

for command_id in commands_exist_id:
  commands_exist_dic.append({"command_id": command_id,
                             "command_title": ""})

for command_id in commands_no_exist_id:
  commands_no_exist_dic.append({"command_id": command_id,
                             "command_title": ""})

with open('CommandsWithoutTitleFound.json', 'w') as f_out:
  json.dump(commands_exist_dic, f_out, indent=2)

with open('CommandsWithoutTitleNotFound.json', 'w') as f_out:
  json.dump(commands_no_exist_dic, f_out, indent=2)

print(len(commands_exist_dic))
print(len(commands_no_exist_dic))
