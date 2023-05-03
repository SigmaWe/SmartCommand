## **Built-in Commands:**

This Python script `BuiltInCommands.py` extracts the commands, titles, categories, sources, and file paths from the Visual Studio Code [VSCode repository](https://github.com/microsoft/vscode). It scans through the JSON and TypeScript files in the repository and collects the required information, then saves it in a single JSON file called `builtInCommandsOutput.json`.

### *Features:*

- Clone the VSCode repository.
- Extract command information from JSON and TypeScript files.
- Save the extracted information in a JSON file.

### *Prerequisites:*

Before running this script, make sure you have Python 3.x installed on your system.

## #*How to Use:*

1. Clone this repository or download the script file.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the script using the following command:

```bash
python BuiltInCommands.py
```
4. The script will clone the VSCode repository, extract the command information, and save it to `builtInCommandsOutput.json`.

### *Output:*
The output file, AllCommands.json, contains a list of dictionaries with the following keys:

command: The command ID.
title: The command title.
category: The command category.
source: The command source.
file_path: The file path where the command is defined.


### *Code Explanation:*
* The provided code is a Python script that extracts command information from the Visual Studio Code (VSCode) repository. It searches for commands in both JSON and TypeScript files and then saves the extracted data in a JSON file. The following sections explain the main functions of the script:
* Importing Required Libraries
The script imports the following libraries:
`glob:` To search for files matching a specified pattern.
`re:` To work with regular expressions.
`json:` To handle JSON data.
`subprocess:` To run shell commands.
`os:` To interact with the operating system.
```
pip install os json subprocess glob re
```


##### *Functions:*
* `clone_vscode_repository(repo_url, target_dir):` This function takes the repository URL and target directory as arguments. It clones the VSCode repository if the target directory doesn't already exist. If the target directory exists, it prints a message indicating that the cloning process is skipped.

* `extract_commands_and_titles(file_path, file_type):` This function takes a file path and file type (either "json" or "typescript") as arguments. It reads the content of the specified file and extracts command information such as command ID, title, category, source, and file path using regular expressions. The extracted information is returned as a list of dictionaries.

* `find_missing_info(target_dir, unique_commands):` This function takes the target directory and a dictionary of unique commands as arguments. It searches for JSON and TypeScript files in the target directory and updates the unique_commands dictionary with any missing information found in those files.

* `main():` This is the main function of the script. It performs the following steps:

  * Define the repository URL and target directory.
  * Clone the VSCode repository using the `clone_vscode_repository()` function.
  * Define the search patterns for JSON and TypeScript files.
  * Create an empty dictionary to store unique commands.
  * Iterate through the JSON and TypeScript files, extract the command information using the `extract_commands_and_titles()` function, and store it in the unique_commands dictionary.
  * Update the `unique_commands` dictionary with any missing information using the `find_missing_info()` function.
  * Convert the `unique_commands` dictionary to a list of values.
  * Save the combined data to a JSON file named `builtInCommandsOutput.json`.
