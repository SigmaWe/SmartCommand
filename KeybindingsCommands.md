# Keybinding Commands

## Explanation of the JSON files
`AllKeybindingCommands.json` - Contains all the commands found in keybindings.json with their associated titles (if they have titles, otherwise the title is an empty string)

`CommandsWithTitle.json` - All the commands from `AllKeybindingCommands.json` that have available titles

`CommandsWithoutTitle.json` - All the commands from `AllKeybindingCommands.json` that don't have titles (their titles are empty strings)

`CommandsWithoutTitleFound.json` - All the commands from `CommandsWithoutTitle.json` that can be found in vscode_cloned (and the Keyboard Shortcuts editor)

`CommandsWithoutTitleNotFound.json` - All the commands from `CommandsWithoutTitle.json` that cannot be found in vscode_cloned (and the Keyboard Shortcuts editor)

## How AllKeybindingCommands.json was created
`clean_commands.py` was used to initialize the files with the command_ids of all the commands in keybindings.json and their titles were all initialized as empty strings. Then, for each command_id in the file, that command_id was entered into the Keyboard Shortcuts Editor, and the corresponding title was entered into the command_title field for that command. Many commands were found in the Keyboard Shortcuts editor, but they did not have an associated title, while some commands couldn't even be found in the Keyboard Shortcuts editor. For these commands, the command_title field is left empty.

## Why searching the Keyboard Shortcuts Editor is the same as searching the VSCode source code
If a command can be found in the Keyboard Shortcuts Editor but has no title, then it can also be found in vscode_cloned but is not registered with a title. If a command cannot be found using the Keyboard Shortcuts Editor, then it also can't be found in the vscode_cloned source code. This was also manually verified by searching for every command ID (that didn't have a title or wasn't found) in the vscode_cloned folder using the VSCode search function.

## Why the commands were manually searched instead of writing a script to scan the source code
1. Even if we wrote a script that automates this process, we have no way of being sure if the script was working correctly. The only way to check if the output of the script is correct, is to  search every command ID to make sure the command_title recorded by the script is the correct command title found in the source code / keyboard shortcut editor. Otherwise, we could end up missing some important information. For example, there were some bugs in clean_commands where command IDs that included hyphens, numbers at the end, or spaces, were not recorded and we could not have detected that unless we manually searched the command IDs. So, we decided to go ahead and just create a "correct" output file that we can use to check the correctness of our future script.

2. We still plan to write a script that automates this process but at least the project isn't being held up anymore and we can proceed to the next stage.
