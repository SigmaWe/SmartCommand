from pydantic import BaseModel
from typing import List

class QueryBase(BaseModel):
    #TODO: ensure the query to be longer than 5 characters
    query: str


class QueryCreate(QueryBase):
    pass


class QuerySave(QueryBase):
    first_pred: str
    ground_truth: int


class Prediction(BaseModel):
    id:int
    predictions: List[str]


class PredSelection(BaseModel):
    id:int
    selection:str


class ReceivedConfirmation(BaseModel):
    status: int


class Command(BaseModel):
    command: str
    command_id: int