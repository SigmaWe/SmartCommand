
# Configuration, need to be consistent with the one in config.py
method=sbert
# model=./pre_trained_models/multi-qa-mpnet-base-dot-v1
model=./pre_trained_models/all-MiniLM-L6-v2
### If you change here, be sure to change in config.py as well
# End of configuration

python3 clean_commands.py
python3 embed_commands.py
python3 search_commands.py "move cursor up" 10 0.6

# the command below packs all cloud function files into a zip file
model_name_base=$(basename $model)
zip cloud_function_$method\_$model_name_base.zip \
    main.py config.py search_commands.py \
    requirements.txt \
    commands_processed.json \
    command_embeddings_$method\_$model_name_base.pickle \
    $model -r