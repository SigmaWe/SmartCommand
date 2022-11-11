from pydantic import BaseModel

class QueryBase(BaseModel):
    #TODO: ensure the query to be longer than 5 characters
    query: str


class QueryCreate(QueryBase):
    pass


class QuerySave(QueryBase):
    first_pred: str
    second_pred: str
    third_pred: str
    fourth_pred: str
    fifth_pred: str
    ground_truth: int


class Prediction(BaseModel):
    id:int
    first_pred: str
    second_pred: str
    third_pred: str
    fourth_pred: str
    fifth_pred: str


class PredSelection(BaseModel):
    id:int
    selection:int


class ReceivedConfirmation(BaseModel):
    status: int
