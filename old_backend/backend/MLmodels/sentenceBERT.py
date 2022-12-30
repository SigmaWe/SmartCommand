import torch
import sentence_transformers
import typing
import os
import re
from .helper import recover_command, FOLDER, FILE_NAME


embedder = sentence_transformers.SentenceTransformer('all-MiniLM-L6-v2')


def pre_embedding(embedder,vs_commands):
    document_embeddings = embedder.encode(vs_commands, convert_to_tensor=True)
    torch.save(document_embeddings, os.path.join(FOLDER, 'command_embedding.pt'))


def semantic_search(query:str, documents:typing.List[str], embedder, number_of_matches = 50):
    """Search a list of _documents_ against a query
    """
    query_embedding = embedder.encode(query, convert_to_tensor=True)
    # document_embeddings = embedder.encode(documents, convert_to_tensor=True)
    document_embeddings = torch.load(os.path.join(FOLDER, 'command_embedding.pt'))
    cos_scores = sentence_transformers.util.cos_sim(query_embedding, document_embeddings)[0]
    top_matches = torch.topk(cos_scores, k=number_of_matches)
    
    top_matching_documents = [(idx, score) for score, idx in zip(top_matches[0], top_matches[1]) ]

    # for document, score in top_matching_documents:
    #     print (document.ljust(40, "-"), " {:.2f}% match".format(score*100))

    return top_matching_documents


f = open(os.path.join(FOLDER, FILE_NAME),'r')
VS_COMMANDS_FULL = []
VS_COMMANDS_SHORT = []
for this_command in f.readlines():
    this_command_short = this_command.strip().split('.')[-1].split('_')
    this_command_short = " ".join(this_command_short)
    this_command_full = re.sub(r'[._]', " ", this_command.replace("\n", ""))
    VS_COMMANDS_FULL.append(this_command_full)
    VS_COMMANDS_SHORT.append(this_command_short)

def sentenceBERT(query,number_of_matches):
    original_command = recover_command(FOLDER,FILE_NAME)
    top_matching_documents = semantic_search(query,VS_COMMANDS_FULL,embedder,number_of_matches)
    result = []
    for document_idx, score in top_matching_documents:
        result.append(original_command[document_idx])
    return result
