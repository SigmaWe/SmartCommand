## **Built-in Commands:**
This Python script, `BuiltInCommands.py`, exports all built-in command information for Visual Studio Code (VSCode) into a JSON file named `builtInCommandsOutput.json`.



### *Description:*
The script clones the [VSCode repository](https://github.com/microsoft/vscode), processes the `package.nls.json` files from the `vscode_cloned\extensions\*` subfolders, and `*.contribution.ts` files from the contrib folder located `~\vscode\src\vs\workbench\contrib\*` to extract built-in command information. 
The results are saved into three separate JSON files, which are then combined into a final JSON file containing all the command information.



### *Usage:*
* Ensure you have Python 3.x and Git installed on your system.
* Run the script by executing python `BuiltInCommands.py` in your terminal or command prompt.

 ```
 python3 BuiltInCommands.py
 ``` 
* The script will output a file named `builtInCommandsOutput.json` in the same directory containing all the built-in command information.



### *Code Explanation:*
* import os, json, subprocess, glob, re: Import required libraries for file manipulation, Git, and regular expressions.
```
pip install os json subprocess glob re
```
* Clone the VSCode repository.
* Find and process `package.nls.json` files.
* Save the processed data to the first output JSON file.
* Process `*.contribution.ts` files in the workbench contrib folder `~\vscode\src\vs\workbench\contrib\*`.
* Save the processed data to the second output JSON file.
* Call `orig_Extension` function and save the results to the third output JSON file.
* Load data from all three output JSON files.
* Combine the data and save it to the final output JSON file.


##### *Functions:*
* `find_package_nls_files(path)`: Returns a list of `package.nls.json` file paths found in the given path.
* `process_subfolders(path)`: Processes `*.contribution.ts` files in subfolders, extracting built-in command information.
* `process_package_nls_file(file_path)`: Processes a `package.nls.json` file, extracting built-in command information.
* `get_subfolders(path)`: Returns a list of subfolder names in the given path.
* `clone_vscode_repository(repo_url, target_dir)`: Clones the VSCode repository from the specified URL to the target directory.
* `orig_Extension(path)`: Extracts all command ids and their titles from the `package.nls.json` files located in the `vscode_cloned\extensions\*` subfolders.
