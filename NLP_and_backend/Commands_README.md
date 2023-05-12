# List of All Command Files

## AllKeybindingCommands.json
Contains a list of all commands found in keybindings.json, along with their corresponding titles (if they have one). These contain all of the built in core, and built in extension commands. These titles were obtained using a combination of a script and a manual process. First, the `GetKeybindings.py` script was used to fetch all the commands from keybindings.json, and create the `AllKeybindingCommands.json` file. At this stage, the file was a list of JSON objects, each looking like this -
```
{
  "command_id": <command taken from keybindings.json>,
  "command_title": ""
},
```
After that, the corresponding title for each command was manually found using the keyboard shortcuts editor. The specific method looked like this (for each command object in the file) -
1. Copy the command_id of the object from the AllKeybindingCommands.json file
2. Paste the command_id into the search bar of the Keyboard Shortcuts Editor
3. Copy the returned title by right clicking on the result and selecting "Copy Command Title" (this doesn't require highlighting and therefore removes the chance of a copying error)
4. Paste the title into the command_title field of the corresponding command object

## plugInCommandsOutput.json
Contains a list of all VSCode extension commands installed on the system. So this includes both built in extension commands and plug in commands from plug ins that were installed by the user. This file was obtained by running `PlugInCommands.py`.