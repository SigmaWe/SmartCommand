import json, pickle, typing
import requests
import sentence_transformers
import numpy

# Replace these with the appropriate values
command_embedding_pickle = 'PickleCommands'
method = 'sbert'
model = 'sentence-transformers/paraphrase-distilroberta-base-v1'

def load_commands(command_url):
    response = requests.get(command_url)
    response.raise_for_status()
    commands = response.json()
    return commands

def emb_sbert(sentences: typing.List[str], model:str):
    embedder = sentence_transformers.SentenceTransformer(model)
    embeddings = embedder.encode(sentences, 
                    convert_to_numpy=True, 
                    normalize_embeddings=True)

    return embeddings

def embed_commands(command_dict_list, method:str, model:str):
    command_strings = [c["command_id"] for c in command_dict_list]
    title_strings = [c["command_title"] for c in command_dict_list]
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

def pickle_embeddings(embeddings: dict, pickle_file):
    with open(pickle_file, 'wb') as f:
        pickle.dump(embeddings, f)

def main(command_url, pickle_file, method, model):
    commands = load_commands(command_url)
    embeddings = embed_commands(commands, method, model)
    pickle_embeddings(embeddings, pickle_file)

if __name__ == "__main__":
    command_url = "https://raw.githubusercontent.com/parthiv2048/SmartCommand/refactor/NLP_and_backend/AllKeybindingCommands.json"

    main(command_url,
         command_embedding_pickle,
         method,
         model)
