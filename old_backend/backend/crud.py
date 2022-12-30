from sqlalchemy.orm import Session
import models, schemas
from typing import List

def create_query(db:Session, query: schemas.QueryCreate, model_name: str):
    db_query = models.VSQuery(query=query.query,
                            model_name = model_name,
                            selected_command=1)
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query


def update_query(db: Session, selection: schemas.PredSelection):
    command_id = db.query(models.VSCommand).filter(models.VSCommand.command==selection.selection).first().command_id
    result = db.query(models.VSQuery).filter(models.VSQuery.id == selection.id).\
            update({'selected_command': command_id})
    db.commit()
    return result


def insert_command(db: Session, command: schemas.Command):
    db_command = models.VSCommand(command=command.command,
                                command_id=command.command_id)
    db.add(db_command)
    db.commit()
    db.refresh(db_command)


def count_command(db: Session):
    total_commands = db.query(models.VSCommand).count()
    return total_commands