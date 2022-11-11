import torch
import sentence_transformers
import typing
import os

FOLDER = './MLmodels/'
FILE_NAME = 'cleaned_commands.txt'

embedder = sentence_transformers.SentenceTransformer('all-MiniLM-L6-v2')

def semantic_search(query:str, documents:typing.List[str], embedder, number_of_matches = 5):
    """Search a list of _documents_ against a query
    """

    query_embedding = embedder.encode(query, convert_to_tensor=True)
    document_embeddings = embedder.encode(documents, convert_to_tensor=True)
    cos_scores = sentence_transformers.util.cos_sim(query_embedding, document_embeddings)[0]
    top_matches = torch.topk(cos_scores, k=number_of_matches)
    
    top_matching_documents = [(documents[idx], score) for score, idx in zip(top_matches[0], top_matches[1]) ]

    # for document, score in top_matching_documents:
    #     print (document.ljust(40, "-"), " {:.2f}% match".format(score*100))

    return top_matching_documents


f = open(os.path.join(FOLDER, FILE_NAME),'r')
VS_COMMANDS = []
for this_command in f.readlines():
    this_command = this_command.strip().split('.')[-1].split('_')
    this_command = " ".join(this_command)
    VS_COMMANDS.append(this_command)

def sentenceBERT(query):
    top_matching_documents = semantic_search(query,VS_COMMANDS,embedder)
    result = []
    for document, score in top_matching_documents:
        result.append(document)
    return result
