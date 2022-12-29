import json, pickle, typing 

import sentence_transformers
import numpy

def load_commands(command_json):
    with open(command_json, 'r') as f:
        commands = json.load(f)
    return commands

def emb_sbert(sentences: typing.List[str], model:str):
    """Embed a list of sentences using Sentence-transformers/SBERT 
    """

    embedder = sentence_transformers.SentenceTransformer(model)
    embedder.encode(sentences)

    return embedder

def embed_commands(command_dict_list, method:str, model:str):
    """Embed command strings 

    command_dict_list: list of dicts of keys: "key", "command", "when", "to_ebd"
    """
    command_strings = [c["to_ebd"] for c in command_dict_list]
    if method == "sbert":
        embeddings = emb_sbert(command_strings, model)
    else:
        print ("other embedding methods not implemented yet")
        exit() 

    return embeddings

def pickle_embeddings(embeddings:numpy.ndarray, pickle_file):
    with open(pickle_file, 'wb') as f:
        pickle.dump(embeddings, f)


def main(command_json, pickle_file, method, model):
    commands = load_commands(command_json)
    embeddings= embed_commands(commands, method, model)
    pickle_embeddings(embeddings, pickle_file)

if __name__ == "__main__":
    command_json = "commands_processed.json"
    method = "sbert"
    model = 'all-MiniLM-L6-v2'
    pickle_file = f"command_embeddings_{method}_{model}.pickle"
    main(command_json, pickle_file, method, model)