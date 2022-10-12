def semantic_search(query:str, documents:typing.List[str], number_of_matches = 5):
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


