import json
import plugInCommands
import builtInCommands

def ExportCommands():
    plugin_data = plugInCommands.main()
    builtin_data = builtInCommands.main()

    merged_data = {'plugin_commands': plugin_data, 'builtin_commands': builtin_data}

    with open("AllCommands.json", 'w', encoding='utf-8') as f_out:
        json.dump(merged_data, f_out, indent=2)

    return merged_data

if __name__ == "__main__":
    ExportCommands()
