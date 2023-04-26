# Embedding-Generator
This repository contains a Python script that generates sentence embeddings for command titles and command IDs from two different JSON files, processes the data using the SBERT method, and saves the embeddings as separate pickle files. It also combines the embeddings into a single pickle file.

## Input:
* The script takes two JSON files as input with the following command URLs::
  * A built-in commands file: `AllKeybindingCommands.json`
  ```
  command_url1 = "https://raw.githubusercontent.com/parthiv2048/SmartCommand/refactor/NLP_and_backend/AllKeybindingCommands.json"
  ```
  
  * A plugin commands file: `PlugInCommandsOutput.json`
  ```
  command_url2 = "https://raw.githubusercontent.com/Aljbab14/SmartCommand/refactor/PlugInCommandsOutput.json"
  ```


## Processing:
* Load the JSON files from the specified URLs.
* Encode the sentences using the SBERT method.
* Generate embeddings for command titles and command IDs, depending on the JSON format.


## Output:
The generated embeddings are saved in separate pickle files, and the script also combines the embeddings from both JSON files into a single pickle file:

* `PickleBuiltinCommands`
* `PicklePluginCommands`
* `CombinedPickleCommands`

#### Results:
```

```

## Requirements:
To run the script, you need to have the following packages installed:

* numpy
* requests
* sentence_transformers

You can install these packages using pip:

Copy code:
```
pip install numpy requests sentence_transformers
```
Usage
Run the main function to execute the entire process. The script will generate separate pickle files for built-in commands and plugin commands, and also combine the embeddings into a single pickle file.
