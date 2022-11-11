from fastapi import Depends, FastAPI
import crud, models, schemas
from typing import List, Dict
from sqlalchemy.orm import Session
from database import Sessionlocal, engine
from fastapi.middleware.cors import CORSMiddleware
from MLmodels.sentenceBERT import sentenceBERT
from MLmodels.BERTScore import BERTScore


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


def fake_model(query: str) -> dict:
    # fake_prediction_BERTScore = ['this_is_prediction1','this_is_prediction2','this_is_prediction3',
    #                     'this_is_prediction4','this_is_prediction5']
    # fake_prediction_SentenceBERT = ['this_is_prediction1','this_is_prediction2','this_is_prediction3',
    #                     'this_is_prediction4','this_is_prediction5']
    predictions_BERTScore = BERTScore(query)
    predictions_sentenceBERT = sentenceBERT(query)
    predictions = {"BERTScore":predictions_BERTScore,"sentenceBERT":predictions_sentenceBERT}
    return predictions


@app.post("/createquery/",response_model = Dict[str,schemas.Prediction])
def create_query(query: schemas.QueryCreate, db: Session=Depends(get_db)):
    db_prediction_dict = {}
    this_query = query.query
    predictions = fake_model(this_query)
    for model_name, this_prediction in predictions.items():
        db_query = crud.create_query(db, query, model_name,this_prediction)
        db_prediction = schemas.Prediction(id=db_query.id,
                                            first_pred=db_query.first_pred,
                                            second_pred=db_query.second_pred,
                                            third_pred=db_query.third_pred,
                                            fourth_pred=db_query.fourth_pred,
                                            fifth_pred=db_query.fifth_pred)
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
    