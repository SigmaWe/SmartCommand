import json
import PlugInCommands
import builtInCommands

def main():
    plugin_data = PlugInCommands.main()
    builtin_data = builtInCommands.main()

    merged_data = {'plugin_commands': plugin_data, 'builtin_commands': builtin_data}

    with open("AllCommands.json", 'w', encoding='utf-8') as f_out:
        json.dump(merged_data, f_out, indent=2)

    return merged_data

if __name__ == "__main__":
    main()
