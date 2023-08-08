# List of All Command Files

## command_title_list.json
Contains a list of all commands found in  Default Keybindings json file, along with their corresponding titles (if they have one). These contain all of the built in core, and built in extension commands. These titles were obtained using the `get_commands_using_gui.py` script. To create the command_title_list.json file, follow the steps below. 
1. Press Ctrl-Shift-P and select "Preferences: Open Default Keyboard Shortcuts (JSON)"
2. Copy the JSON list from the file and paste it into `default_keybindings.json`
3. Copy the series of comments under the JSON list and paste it into `default_commands_not_bound.txt`
4. Open the `get_command_using_gui.py` script and find the comment that tells you to copy the test string
5. Press Ctrl-Shift-P again and select "Open Keyboard Shortcuts"
6. Open a Terminal within the VSCode editor and run the `get_commands_using_gui.py` script.

## plugInCommandsOutput.json
Contains a list of all VSCode extension commands installed on the system. This only includes plug in commands from plug ins that were installed by the user, from the Marketplace. This file was obtained by running `PlugInCommands.py`.