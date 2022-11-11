from sqlalchemy.orm import Session
import models, schemas
from typing import List

def create_query(db:Session, query: schemas.QueryCreate, model_name: str, predictions: List[str]):
    db_query = models.VSQuery(query=query.query,
                            model_name = model_name,
                            first_pred=predictions[0],
                            second_pred=predictions[1],
                            third_pred=predictions[2],
                            fourth_pred=predictions[3],
                            fifth_pred=predictions[4])
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query


def update_query(db: Session, selection: schemas.PredSelection):
    result = db.query(models.VSQuery).filter(models.VSQuery.id == selection.id).\
            update({'ground_truth': selection.selection})
    db.commit()
    return result