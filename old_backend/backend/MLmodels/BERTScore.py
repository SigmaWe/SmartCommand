from evaluate import load
import numpy as np
import re
import os
from .helper import recover_command,FOLDER,FILE_NAME

FOLDER = './MLmodels/'
FILE_NAME = 'cleaned_commands.txt'

def BERTScore(query,number_of_matches=50):
    original_command = recover_command(FOLDER,FILE_NAME)
    f = open(os.path.join(FOLDER, FILE_NAME),'r')
    lines = f.readlines()
    bertscore = load("bertscore")
    predictions = [re.sub(r'[._]', " ", x.replace("\n", "")) for x in lines]
    references = [query]*len(predictions)
    results = bertscore.compute(predictions=predictions, references=references, model_type="distilbert-base-uncased", idf=False)
    f1_scores = results['f1']
    ranks = sorted(range(len(f1_scores)), key=lambda k: f1_scores[k], reverse=True)
    result = []
    for i in range(number_of_matches):
        result.append(original_command[ranks[i]])
    return result
