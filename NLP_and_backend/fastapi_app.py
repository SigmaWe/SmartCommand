import fastapi
import os

import search_commands


### Configurations 
import config 
method = config.method 
model =  config.model 
command_dict_list_json = config.command_dict_list_json
command_embedding_pickle = config.command_embedding_pickle
### End of Configurations

### Load the data at the beginning of the app
command_embeddings = search_commands.load_command_embeddings(command_embedding_pickle)
command_dict_list = search_commands.load_command_dict_list(command_dict_list_json)
### End of loading data

### Define a function that does the search and combine
def search_main(query, command_embeddings, command_dict_list, method, model, k, p):
      # search 
      scores = search_commands.semantic_search(query, command_embeddings, method, model)
   
      # combine 
      results = search_commands.combine_results(scores, command_dict_list, k, p)
      # list of tuples: (command, score)

      # Pack into the return per our documentation 
      results = [command for (command, score) in results]
   
      return results
### End of search and combine functions

# Start out app 
app = fastapi.FastAPI()

@app.get("/search")
def search(q:str="insert cursor above", k:int=15, p:float=0.7):
    return search_main(q, command_embeddings, command_dict_list, method, model, k, p)