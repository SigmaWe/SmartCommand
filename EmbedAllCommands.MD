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
Data loaded from pickle file:
{'command_id': array(['undo', 'workbench.action.navigatePreviousInNavigationLocations',
       'workbench.action.terminal.newWithProfile', ...,
       'testExplorerConverter.useNativeTesting',
       'testExplorerConverter.activate', 'smart-command.NLPSearch'],
      dtype='<U107'), 'command_id_embeddings': array([[ 0.01486425,  0.00208701,  0.01102797, ..., -0.03393227,
         0.0001364 , -0.02323117],
       [-0.0154143 , -0.04124983,  0.044486  , ..., -0.03028861,
         0.02760038,  0.04028783],
       [-0.02140618, -0.04775995,  0.03444268, ..., -0.07405331,
         0.02556558,  0.02403491],
       ...,
       [-0.03324559, -0.01929064,  0.01733424, ..., -0.01186709,
        -0.00933071, -0.00137364],
       [-0.02407619, -0.03647603,  0.02864844, ..., -0.04563014,
        -0.01414619,  0.02959919],
       [ 0.03549776, -0.02587044,  0.0058332 , ..., -0.05260216,
         0.02893867,  0.03373425]], dtype=float32), 'command_title': array(['Undo', 'Go Previous in Navigation Locations',      
       'Terminal: Create New Terminal (With Profile)', ...,
       'Use Native Testing', 'Activate Test Adapter Converter',
       'NLPSearch'], dtype='<U71'), 'command_title_embeddings': array([[ 0.01829119,  0.00625119,  0.03220959, ...,  0.00763984,
         0.01767007, -0.02951007],
       [ 0.01121256, -0.00498447,  0.02305573, ...,  0.03427046,
         0.03123944, -0.03002878],
       [ 0.00410265, -0.00141695,  0.05156548, ..., -0.00399274,
        -0.02027933,  0.01998521],
       ...,
       [-0.03046872, -0.02360568,  0.02859264, ...,  0.05634124,
        -0.00787647, -0.02920213],
       [-0.01708015,  0.04616084,  0.00767357, ...,  0.02391962,
         0.02148743,  0.01386273],
       [ 0.01945179, -0.02693897,  0.04717004, ..., -0.03340817,
         0.04534249, -0.00312393]], dtype=float32)}
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
