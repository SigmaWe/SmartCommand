# Generate the VS Code command file

It is surprisingly hard to find the list of built-in commands of VS Code, so I generate the commands based on the keyboard shortcuts.

To reproduce the same result (on macOS, the steps on Windows/Linux could be a bit different):

1. Download and install the latest Visual Studo Code, the version that I use is `1.72.0`;
1. Open the VS Code Palette by `view->Command Palette`;
2. In the palette, search `Open Default Keyboard Shortcuts (JSON)`, then a file will open;
3. Copy and paste all the contents into `raw_commands.txt`;
4. Run `python3 clean_command.py`, it will return `cleaned_commands.txt`.

# Caveats

1. The commands are not exactly the same as you see when searching in the palette. For example, when you search `add cursor above`, in the palette, it shows as `Add Cursor Above`, but the command is `editor.action.insertCursorAbove`. `Add Cursor Above` is called `label` of the command, `editor.action.insertCursorAbove` is called `id` of the command. The reason that I use `id` instead of `label` is I cannot find the command list using labels.