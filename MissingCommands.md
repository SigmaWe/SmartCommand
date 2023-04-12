# **Missing Commands**
This Python script goes through each command in `keybindings.json`, checks if it is present in `AllCommands.json`, and compiles its results in `MissingCommands.json` and `FoundCommands.json`

### *How To Run the script:*
To run the code directly, simply execute the `MissingCommands.py` script in your terminal:
```
python3 MissingCommands.py
```
This will create an `MissingCommands.json` and `FoundCommands.json` file in the same directory. Inside the `MissingCommands.json` file, the `num_missing_commands` key shows the number of missing commands (i.e. the number of commands present in `keybindings.json` but not present in `AllCommands.json`) and the `missing_commands` key is a list of the missing command IDs. Inside the `FoundCommands.json` file, the `num_found_commands` key shows the number of commands that were found (i.e. the number of commands present in both `keybindings.json` and `AllCommands.json`) and the `found_commands` key is a list of the found command IDs.
