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