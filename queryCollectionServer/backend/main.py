from fastapi import Depends, FastAPI
import crud, models, schemas
from typing import List, Dict
from sqlalchemy.orm import Session
from database import Sessionlocal, engine
from fastapi.middleware.cors import CORSMiddleware
from MLmodels.sentenceBERT import sentenceBERT
from MLmodels.BERTScore import BERTScore
from MLmodels.helper import recover_command, FOLDER,FILE_NAME
import random
import contextlib


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:30",
    "localhost:30",
    "http://127.0.0.1:30"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)



def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

get_db_wrapper = contextlib.contextmanager(get_db)

def fake_model(query: str) -> dict:
    # fake_prediction_BERTScore = ['this_is_prediction1','this_is_prediction2','this_is_prediction3',
    #                     'this_is_prediction4','this_is_prediction5']
    # fake_prediction_SentenceBERT = ['this_is_prediction1','this_is_prediction2','this_is_prediction3',
    #                     'this_is_prediction4','this_is_prediction5']
    # predictions = {"BERTScore":fake_prediction_BERTScore,"sentenceBERT":fake_prediction_SentenceBERT}
    model_name = random.choice(['BERTScore','sentenceBERT'])
    if model_name == 'BERTScore':
        model_predictions = BERTScore(query,50)
    elif model_name == 'sentenceBERT':
        model_predictions = sentenceBERT(query,50)
    model_predictions.append('None of above')
    predictions = {model_name:model_predictions}
    return predictions


@app.on_event("startup")
async def startup_event():
    with get_db_wrapper() as db:
        commands_needed = recover_command(FOLDER,FILE_NAME)
        commands_have = crud.count_command(db)
        if commands_have == 0:
            this_command_db = schemas.Command(command="Not selected yet",command_id=1)
            crud.insert_command(db,this_command_db)
            this_command_db = schemas.Command(command="None of above",command_id=2)
            crud.insert_command(db,this_command_db)
            for idx, this_command in enumerate(commands_needed):
                this_command_db = schemas.Command(command=this_command,command_id=idx+2+1)
                crud.insert_command(db, this_command_db)
        # -2: 1 for not selected yet, 1 for none of the returned command
        elif len(commands_needed) > commands_have - 2:
            for idx,this_command in enumerate(commands_needed[commands_have - 2:]):
                this_command_db = schemas.Command(command=this_command,command_id=commands_have+1+idx)
                crud.insert_command(db, this_command_db)
        elif len(commands_needed) == commands_have - 2:
            pass
        else:
            raise ValueError("The number of commands in the database is not aligned with what we have.")


@app.post("/createquery/",response_model = Dict[str,schemas.Prediction])
def create_query(query: schemas.QueryCreate, db: Session=Depends(get_db)):
    db_prediction_dict = {}
    this_query = query.query
    predictions = fake_model(this_query)
    for model_name, this_prediction in predictions.items():
        db_query = crud.create_query(db, query, model_name)
        db_prediction = schemas.Prediction(id=db_query.id,
                                            predictions=this_prediction)
        db_prediction_dict[model_name] = db_prediction
    return db_prediction_dict


@app.put("/updatequery/",response_model = Dict[int,schemas.ReceivedConfirmation])
def update_query(selection: List[schemas.PredSelection],db: Session=Depends(get_db)):
    result = {}
    for this_this_selection in selection:
        id = this_this_selection.id
        db_result = crud.update_query(db,this_this_selection)
        return_obj = schemas.ReceivedConfirmation(status=db_result)
        result[id] = return_obj
    return result
    