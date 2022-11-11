from evaluate import load
import numpy as np
import re
import os

FOLDER = './MLmodels/'
FILE_NAME = 'cleaned_commands.txt'

def BERTScore(query):
    f = open(os.path.join(FOLDER, FILE_NAME),'r')
    lines = f.readlines()
    bertscore = load("bertscore")
    predictions = [re.sub(r'[._]', " ", x.replace("\n", "")) for x in lines]
    references = [query]*len(predictions)
    results = bertscore.compute(predictions=predictions, references=references, model_type="distilbert-base-uncased", idf=False)
    f1_scores = results['f1']
    ranks = sorted(range(len(f1_scores)), key=lambda k: f1_scores[k], reverse=True)
    result = []
    for i in range(5):
        result.append(predictions[ranks[i]])
    return result
