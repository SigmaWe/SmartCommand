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

# Function to encode sentences using the SBERT method
def emb_sbert(sentences: typing.List[str], model:str):
    embedder = sentence_transformers.SentenceTransformer(model)
    embeddings = embedder.encode(sentences, 
                    convert_to_numpy=True, 
                    normalize_embeddings=True)

    return embeddings

# Function to generate embeddings for command titles and command IDs
def embed_commands(command_dict_list, method:str, model:str, json_format=1):
    # Extract command titles and command IDs depending on the JSON format
    if json_format == 1:
        command_strings = [c["command_id"] for c in command_dict_list]
        title_strings = [c["command_title"] for c in command_dict_list]
    elif json_format == 2:
        command_strings = [cmd["command"] for plugin in command_dict_list for cmd in plugin["commands"]]
        title_strings = [cmd["title"] for plugin in command_dict_list for cmd in plugin["commands"]]
    else:
        raise ValueError("Invalid JSON format")

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

# Function to combine two pickle files into a single pickle file
def combine_pickles(pickle_file1, pickle_file2, combined_pickle):
    with open(pickle_file1, 'rb') as f1, open(pickle_file2, 'rb') as f2:
        embeddings1 = pickle.load(f1)
        embeddings2 = pickle.load(f2)
    
    combined_embeddings = {key: numpy.concatenate((embeddings1[key], embeddings2[key])) for key in embeddings1}
    
    with open(combined_pickle, 'wb') as f:
        pickle.dump(combined_embeddings, f)

# Main function to execute the entire process
def main(command_url1, command_url2, Builtincommand_pickle, Plugincommand_pickle, combined_pickle, method, model):
    commands1 = load_commands(command_url1)
    commands2 = load_commands(command_url2)
    embeddings1 = embed_commands(commands1, method, model, json_format=1)
    embeddings2 = embed_commands(commands2, method, model, json_format=2)
    pickle_embeddings(embeddings1, Builtincommand_pickle)
    pickle_embeddings(embeddings2, Plugincommand_pickle)
    combine_pickles(Builtincommand_pickle, Plugincommand_pickle, combined_pickle)

# Run the script
if __name__ == "__main__":
    command_url1 = "https://raw.githubusercontent.com/parthiv2048/SmartCommand/refactor/NLP_and_backend/AllKeybindingCommands.json"
    command_url2 = "https://raw.githubusercontent.com/Aljbab14/SmartCommand/refactor/PlugInCommandsOutput.json"

    # Set the names for the output pickle files
    Builtincommand_embedding_pickle = 'PickleBuiltinCommands'
    Plugincommand_embedding_pickle = 'PicklePluginCommands'
    combined_pickle = 'CombinedPickleCommands'
    method = 'sbert'
    model = 'sentence-transformers/paraphrase-distilroberta-base-v1'

    main(command_url1,
         command_url2,
         Builtincommand_embedding_pickle,
         Plugincommand_embedding_pickle,
         combined_pickle,
         method,
         model)
