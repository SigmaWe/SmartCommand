data_root = "./"
method = "sbert"
model = 'all-MiniLM-L6-v2'
# model = './pre_trained_models/multi-qa-mpnet-base-dot-v1'
# model = './pre_trained_models/all-MiniLM-L6-v2'

# If you change the model above, be sure to change accordingly in run_all.sh as well

import os
model_name_base=os.path.basename(model)
command_dict_list_json = os.path.join(data_root, "command_title_list.json")
command_embedding_pickle = os.path.join(data_root, f"embeddings_commands_{method}_{model_name_base}.pickle")
command_embedding_pickle_title = os.path.join(data_root, f"embeddings_titles_{method}_{model_name_base}.pickle")