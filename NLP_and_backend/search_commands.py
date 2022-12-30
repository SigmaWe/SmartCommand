# given a query, find matching commands. 

import pickle 
import json
import numpy 

#%%
def semantic_search_sbert(query:str, command_embeddings, model:str):
    import sentence_transformers
    
    embedder = sentence_transformers.SentenceTransformer(model)
    query_embedding = embedder.encode(query, 
                                      convert_to_numpy=True, 
                                      normalize_embeddings=True)

    return sentence_transformers.util.semantic_search(query_embedding,
                                                      command_embeddings,
                                                      top_k=20000, # this k needs to be very big 
                                                      score_function=sentence_transformers.util.dot_score
                                                      )[0] # index 0 because we have only one query 

    # cosine_scores = sentence_transformers.util.dot_score(
    #                        query_embedding, command_embeddings)
    # return cosine_scores

# %% 
def semantic_search(query:str, command_embeddings, method:str, model:str):
    """Return commands machine a query 

    Depending on the approach, the embeddings are of different shapes. 
    For SBERT, the embedding is at the sentence level. Hence, 
    the embeddings are 2D arrays, with axis-0 for each command. 
    For BERTScore, the embedding is at the token level. Hence, the 
    embeddings are 3D arrays, with axis 0 for each command, and 
    axis 1 for each token. 

    command_dict_list: a list of commands, 
                    each a dict: 
                {"key":str, "command":str, "when":str, "to-ebd": str}
                to-ebd is the string to embed the command itself or its label

    """

    if method == "sbert":
        scores = semantic_search_sbert(query, command_embeddings, model)

    return scores 

#%%
def filter_results(num_array: numpy.ndarray, k:int, p:float):
    """Filter results using a combination of top-k and top-p.

    num_array is already sorted 
    """
    cum_sum = numpy.cumsum(num_array)
    total_score = numpy.sum(num_array)
    cum_sum = cum_sum / total_score
    top_p = numpy.where(cum_sum >= p)[0][0]
    print ("p cutoff index: ", top_p)
    index = min(k, top_p)
    return index

def combine_results(scores:dict[list], command_dict_list, k, p):
    """Combine results from semantic search with command dict list with filters,
    such as top-p. 

    scores: list of dicts, each dict has keys: corpus_id and score. 

    """
    results = []

    cutoff_index = filter_results([s['score'] for s in scores], k, p)

    for score in scores[:cutoff_index]:
        command_id = score['corpus_id']
        command = command_dict_list[command_id]['command']
        results.append((command, score['score']))
    return results

# %%
def load_command_embeddings(pickle_file):
    with open(pickle_file, 'rb') as f:
        command_embeddings = pickle.load(f)
    return command_embeddings

def load_command_dict_list(command_json):
    """To save a slight amount of time, load the command list that has no to_ebd field
    Thus, the command_processed.json file 
    """
    with open(command_json, 'r') as f:
        commands = json.load(f)
    return commands

#%% 
def main(query, command_embedding_pickle, command_dict_list_json, method, model, k, p):

    # load 
    command_embeddings = load_command_embeddings(command_embedding_pickle)
    command_dict_list = load_command_dict_list(command_dict_list_json)

    # search 
    scores = semantic_search(query, command_embeddings, method, model)

    # combine 
    results = combine_results(scores, command_dict_list, k, p)

    return results

if __name__ == "__main__":
    import sys, os
    query = sys.argv[1]   
    k, p = 20, 0.8
    [k, p] = sys.argv[2:4]
    k, p = int(k), float(p)

    import config
    results = main(query, 
                   config.command_embedding_pickle, 
                   config.command_dict_list_json, 
                   config.method, 
                   config.model, k, p)
    for (command, score) in results:
        print (command.ljust(40), f"{score:.3f}")
