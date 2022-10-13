from evaluate import load
import numpy as np
import re

if __name__ == '__main__':
    # Replace the '.' and '_' with space.
    input_str = input()
    with open('../VSCode_command/cleaned_commands.txt', 'r') as f:
        lines = f.readlines()
    bertscore = load("bertscore")
    # predictions = [x.replace("\n", "").split('.')[-1].replace("_"," ") for x in lines]
    predictions = [re.sub(r'[._]', " ", x.replace("\n", "")) for x in lines]
    references = [input_str]*len(predictions)
    results = bertscore.compute(predictions=predictions, references=references, model_type="distilbert-base-uncased", idf=False)
    f1_scores = results['f1']
    ranks = sorted(range(len(f1_scores)), key=lambda k: f1_scores[k], reverse=True)
    print("query: "+input_str)
    for i in range(5):
        print(predictions[ranks[i]]+":"+str(np.round(f1_scores[ranks[i]],2)))