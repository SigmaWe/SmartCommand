## **Plug-in Commands:**
This Python script, `PlugInCommands.py`, exports all plug-in commands information for Visual Studio Code (VSCode) into a JSON file named `PlugInCommandsOutput.json`.

### *Description:*
The script goes through the installed extensions in the user's `.vscode/extensions` folder, extracts command information from the `package.json` files of each extension. The result is a list of all available commands, including the source and version information.

### *Usage:*
* Ensure you have Python 3.x installed on your system.
* Run the script by executing python `PlugInCommands.py` in your terminal or command prompt.
```
python3 PlugInCommands.py
```
* The script will output a file named "PlugInCommandsOutput.json" in the same directory containing all the command information.

### *Code Explanation:*
import json, glob, os: Import required libraries for file manipulation and path handling.
```
pip install json glob2 os
```

* `extension_folder`: Retrieves the path to the `.vscode/extensions` folder using `get_extension_folder()` function.
* `extension_json_files`: Finds all `package.json` files within the extensions folder using the `glob.glob()` function.
* `all_commands`: List to store all commands found.
* Loop through `extension_json_files` then Open and read each `package.json` file.
* Extract extension name and version from package.
* Check if the file contains command contributions.
* Loop through commands and add source (extension name) and version information.
* Append each command to `all_commands`.
* Write `all_commands` to the `PlugInCommandsOutput.json` file.

##### *Functions:*
* `get_extension_folder()`: Returns the path to the `.vscode/extensions` folder based on the OS (Windows or Unix-based).
* `get_default_keybindings_file()`: Returns the file name of the default keybindings file, which is `package.json`.
* `PlugInCommands()`: Main function to collect all command information and save it to a JSON file.

### *Files and Paths:*

extension_folder: Path to the `.vscode/extensions` folder.
package.json: Default keybindings file in the same directory as the script.
`PlugInCommandsOutput.json`: Output file containing all command information.
