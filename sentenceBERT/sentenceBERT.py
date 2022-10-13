import torch
import sentence_transformers
import typing
import os

FOLDER = '../VSCode_command/'
FILE_NAME = 'cleaned_commands.txt'
NL_COMMANDS = ['preview markdown file',
               'open another VS code',
               'create an empty file',
               'close all windows']

embedder = sentence_transformers.SentenceTransformer('all-MiniLM-L6-v2')

def semantic_search(query:str, documents:typing.List[str], embedder, number_of_matches = 5):
    """Search a list of _documents_ against a query
    """

    query_embedding = embedder.encode(query, convert_to_tensor=True)
    document_embeddings = embedder.encode(documents, convert_to_tensor=True)
    cos_scores = sentence_transformers.util.cos_sim(query_embedding, document_embeddings)[0]
    top_matches = torch.topk(cos_scores, k=number_of_matches)
    
    top_matching_documents = [(documents[idx], score) for score, idx in zip(top_matches[0], top_matches[1]) ]

    for document, score in top_matching_documents:
        print (document.ljust(80, "-"), " {:.2f}% match".format(score*100))

    return top_matching_documents


f = open(os.path.join(FOLDER, FILE_NAME),'r')
commands = []
for this_command in f.readlines():
    this_command = this_command.split('.')[-1].split('_')
    this_command = " ".join(this_command)
    commands.append(this_command)
f.close()
for this_query in NL_COMMANDS:
    print(f"Current command:{this_query}")
    _ = semantic_search(this_query, commands, embedder, number_of_matches=5)
    print('-'*80)
