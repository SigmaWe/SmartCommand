# Generate the VS Code command file

It is surprisingly hard to find the list of built-in commands of VS Code, so we generate the commands based on the keyboard shortcuts.

To reproduce the same result (on macOS, the steps on Windows/Linux could be a bit different):

1. Download and install the latest Visual Studo Code (`1.72.0` we used).
2. Open the VS Code Palette by `View->Command Palette`.
3. In the palette, search `Open Default Keyboard Shortcuts (JSON)` and press Enter, then a file will open.
4. Save the file using default name `keybindings.json`.
5. Run `python3 clean_commands.py` to get `commands_processed.json`.

# Caveats

1. The commands are not exactly the same as you see when searching in the palette. For example, when you search `add cursor above`, in the palette, it shows as `Add Cursor Above`, but the command is `editor.action.insertCursorAbove`. `Add Cursor Above` is called `label` of the command, `editor.action.insertCursorAbove` is called `id` of the command. We are still working on extracting all commands provided by VSCode and extensions. 