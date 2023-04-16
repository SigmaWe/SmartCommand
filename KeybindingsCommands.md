# Keybinding Commands

## Explanation of the JSON files
AllKeybindingCommands.json - Contains all the commands found in keybindings.json with their associated titles (if they have titles, otherwise the title is an empty string)
CommandsWithTitle.json - All the commands from AllKeybindingCommands.json that have available titles
CommandsWithoutTitle.json - All the commands from AllKeybindingCommands.json that don't have titles (their titles are empty strings)
CommandsWithoutTitleFound.json - All the commands from CommandsWithoutTitle.json that can be found in vscode_cloned
CommandsWithoutTitleNotFound.json - All the commands from CommandsWithoutTitle.json that cannot be found in vscode_cloned

## How AllKeybindingCommands.json was created
`clean_commands.py` was used to initialize the files with the command_ids of all the commands in keybindings.json and their titles were all initialized as empty strings. Then, for each command_id in the file, that command_id was entered into the Keyboard Shortcuts Editor, and the corresponding title was entered into the command_title field for that command. Many commands were found in the Keyboard Shortcuts editor, but they did not have an associated title, while some commands couldn't even be found in the Keyboard Shortcuts editor. For these commands, the command_title field is left empty.

## The similarity between Keyboard Shortcuts Editor and vscode_cloned
If a command can be found in the Keyboard Shortcuts Editor but has no title, then it can also be found in vscode_cloned but is not registered with a title. If a command cannot be found using the Keyboard Shortcuts Editor, then it also can't be found in the vscode_cloned source code.
