data_root = "./"
method = "sbert"
#    model = 'all-MiniLM-L6-v2'
model = './pre_trained_models/multi-qa-mpnet-base-dot-v1'

# If you change the model above, be sure to change accordingly in run_all.sh as well

import os
model_name_base=os.path.basename(model)
command_dict_list_json = os.path.join(data_root, "commands_processed.json")
command_embedding_pickle = os.path.join(data_root, f"command_embeddings_{method}_{model_name_base}.pickle")
