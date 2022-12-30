# Pre-embed commands extracted by clean_commands.py
# You can select the approach and models at the end


import json, pickle, typing 

import sentence_transformers
import numpy

def load_commands(command_json):
    with open(command_json, 'r') as f:
        commands = json.load(f)
    return commands

def emb_sbert(sentences: typing.List[str], model:str):
    """Embed a list of sentences using Sentence-transformers/SBERT 

    Return is a 2D numpy array. 

    """

    embedder = sentence_transformers.SentenceTransformer(model)
    embeddings = embedder.encode(sentences, 
                    convert_to_numpy=True, 
                    normalize_embeddings=True)

    return embeddings

def embed_commands(command_dict_list, method:str, model:str):
    """Embed command strings 

        command_dict_list: a list of commands, 
                       each a dict: 
                    {"key":str, "command":str, "when":str, "to-ebd": str}
                    to-ebd is the string to embed the command itself or its label


    Depending on the approach, the embeddings are of different shapes. 
    For SBERT, the embedding is at the sentence level. Hence, 
    the embeddings are 2D arrays, with axis-0 for each command. 
    For BERTScore, the embedding is at the token level. Hence, the 
    embeddings are 3D arrays, with axis 0 for each command, and 
    axis 1 for each token. 

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
    import config 

    main(config.command_dict_list_json, 
         config.command_embedding_pickle, 
         config.method, config.model)