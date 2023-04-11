# **All Commands**
This Python script merges the data from `plugInCommands.py` and `builtInCommands.py` and saves the combined data in a JSON file called `AllCommands.json`. You can run this script in two different ways:

### *Option 1: Run the code directly:*
To run the code directly, simply execute the `AllCommands.py` script in your terminal:
```
python3 AllCommands.py
```
This will create an `AllCommands.json` file in the same directory, containing the combined data from `plugInCommands.py` and `builtInCommands.py`.

### *Option 2: Call the file from a different Python script:*
You can also use the `AllCommands.py` script as a module and call its `ExportCommands()` function from a different Python script. To do this, follow these steps:

1. 1. Import the main function from `AllCommands.py` in your new Python script:
2. ```
3. from AllCommands import ExportCommands
4. ```
5. 2. Call the ExportCommands() function in your new script:
6. ```
7. merged_data = ExportCommands()
8. ```
9. This will execute the merging process and return the combined data as a dictionary. The `AllCommands.json` file will also be created in the same directory as `AllCommands.py`.

Here's an example of how to use the ExportCommands() function from a different Python script:
```
from AllCommands import ExportCommands

def process_merged_data():
    merged_data = ExportCommands()
    # Perform additional processing on merged_data if needed

if __name__ == "__main__":
    process_merged_data()
```
In this example, the `process_merged_data()` function imports and calls the `ExportCommands()` function from `AllCommands.py`. You can perform additional processing on the returned merged_data dictionary as needed.
