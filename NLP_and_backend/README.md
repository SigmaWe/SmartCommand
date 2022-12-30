# NLP and backend 

The following instruction assumes that you are doing everything under this folder, `NLP_and_backend`. 

## Dependencies

In `requirements.txt`. 

## Getting the commands 

It is surprisingly hard to find the list of built-in commands of VS Code, so we generate the commands based on the keyboard shortcuts. To access of keyboard shortcuts, 
1. Open the VS Code Palette by `View->Command Palette` or `Ctrl/Cmd Shift P`.
2. In the Command Palette, search for `Open Default Keyboard Shortcuts (JSON)` and press Enter, then a file will open.
4. Save the file using default name `keybindings.json`.

## Preprocessing and pre-embed the commands 

```shell
python3 clean_commands.py
python3 embed_commands.py
```

All configurations for the two scripts above are at the bottom of them. You can select what model to use, for example. Currently we only support Sentence-Transformer/SBERT-based embedding because we love dot-products. 

## Starting the backend server

It's just like starting a normal FastAPI app: 

```shell
uvicorn app:app --reload
```

## Endpoints and query formats

Please see [project README](../README.md#nlp-and-backend). 

## Caveats

1. The commands are not exactly the same as you see when searching in the palette. For example, when you search `add cursor above`, in the palette, it shows as `Add Cursor Above`, but the command is `editor.action.insertCursorAbove`. `Add Cursor Above` is called `label` of the command, `editor.action.insertCursorAbove` is called `id` of the command. We are still working on extracting all commands provided by VSCode and extensions. 

## File structure

### Scripts

* `run_all.sh`: The shell script to do everything preparing the data and files, and even packing the zip file for Google Cloud Functions hosting. To save clod-start time, we pack the language model into the package. 
* `config.py`: The central location of all configurations, used by many other scripts. 
* `clean_commands.py`: Preprocessing VSCode commands accessible via `keybindings.json` file
* `embed_commands.py`: Pre-embed all commands using a model specified.
* `search_commands.py`: Command search functions and a demo which accepts a query and parameters from `sys.argv`. Needed by fastAPI and GCP `functions_framework` apps. 
* `fastapi_app.py`: A fastAPI app to do command search locally. 
* `main.py`: The app in `functions_framework` for hosting in Google Cloud Functions (GCF) service. We hate to call it `main.py` but it seems GCF has bugs. 

### Data files
* `keybindings.json`: Command shortcut configuration file in VSCode, resaved. Some commands have shortcut keys while others do not. 
* `commands_processed.json`: Commands normalized from above using `clean_commands.py`. 
* `command_embeddings_{approach}_{model}.py`: Embeddings of commands by `embed_commands.py` using a model specified in `config.py`.
