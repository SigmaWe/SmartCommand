import json, pickle, typing
import requests
import sentence_transformers
import numpy

# Function to fetch JSON data from the given URL
def load_commands(command_url):
    response = requests.get(command_url)
    response.raise_for_status()
    commands = response.json()
    return commands

# Function to remove duplicate commands from the two JSON files with different formats
def remove_duplicates(commands1, commands2, json_format1=1, json_format2=2):
    # Helper function to get the command ID based on the JSON format
    def get_command_id(command, json_format):
        if json_format == 1:
            return command["command_id"]
        elif json_format == 2:
            return command["command"]
        else:
            raise ValueError("Invalid JSON format")

    # Combine commands from both JSON files
    combined_commands = commands1 + [cmd for plugin in commands2 for cmd in plugin["commands"]]
    seen = set()
    unique_commands = []

    # Iterate over combined_commands and keep track of unique command IDs
    for command in combined_commands:
        cmd_id = get_command_id(command, json_format1 if command in commands1 else json_format2)

        if cmd_id not in seen:
            seen.add(cmd_id)
            unique_commands.append(command)

    return unique_commands

# Function to encode sentences using the SBERT method
# We chose this method because it generates high-quality sentence embeddings
# and is suitable for semantic similarity tasks.
def emb_sbert(sentences: typing.List[str], model:str):
    embedder = sentence_transformers.SentenceTransformer(model)
    embeddings = embedder.encode(sentences, 
                    convert_to_numpy=True, 
                    normalize_embeddings=True)

    return embeddings

# Function to generate embeddings for command titles and command IDs
def embed_commands(command_dict_list, method:str, model:str):
    command_strings = []
    title_strings = []
    
    # Extract command titles and command IDs from the unique_commands list
    for command in command_dict_list:
        if "command_id" in command:
            command_strings.append(command["command_id"])
            title_strings.append(command["command_title"])
        elif "command" in command:
            command_strings.append(command["command"])
            title_strings.append(command["title"])
        else:
            raise ValueError("Invalid command format")

    # Generate embeddings using the SBERT method
    if method == "sbert":
        command_embeddings = emb_sbert(command_strings, model)
        title_embeddings = emb_sbert(title_strings, model)
        embeddings = {
            "command_id": command_strings,
            "command_id_embeddings": command_embeddings,
            "command_title": title_strings,
            "command_title_embeddings": title_embeddings,
        }
    else:
        print("other embedding methods not implemented yet")
        exit()

    return embeddings

# Function to save embeddings as a pickle file
def pickle_embeddings(embeddings: dict, pickle_file):
    with open(pickle_file, 'wb') as f:
        pickle.dump(embeddings, f)

# Main function to execute the entire process
def main(command_url1, command_url2, Builtincommand_pickle, Plugincommand_pickle, combined_pickle, method, model):
    commands1 = load_commands(command_url1)
    commands2 = load_commands(command_url2)
    unique_commands = remove_duplicates(commands1, commands2, json_format1=1, json_format2=2)
    embeddings1 = embed_commands(unique_commands, method, model)
    pickle_embeddings(embeddings1, Builtincommand_pickle)

# Run the script
if __name__ == "__main__":
    command_url1 = "https://raw.githubusercontent.com/parthiv2048/SmartCommand/refactor/NLP_and_backend/AllKeybindingCommands.json"
    command_url2 = "https://raw.githubusercontent.com/Aljbab14/SmartCommand/refactor/PlugInCommandsOutput.json"

    Builtincommand_embedding_pickle = 'PickleBuiltinCommands.pkl'
    Plugincommand_embedding_pickle = 'PicklePluginCommands.pkl'
    combined_pickle = 'CombinedPickleCommands.pkl'
    method = 'sbert'
    model = 'sentence-transformers/paraphrase-distilroberta-base-v1'

    main(command_url1,
         command_url2,
         Builtincommand_embedding_pickle,
         Plugincommand_embedding_pickle,
         combined_pickle,
         method,
         model)
