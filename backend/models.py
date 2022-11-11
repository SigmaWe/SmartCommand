from sqlalchemy import Column, String, Integer,Enum
from database import Base
import enum


class VSQuery(Base):
    __tablename__ = "vsqueries"

    id = Column(Integer, primary_key = True)
    query = Column(String)
    model_name = Column(String)
    #0
    first_pred = Column(String)
    #1
    second_pred = Column(String)
    #2
    third_pred = Column(String)
    #3
    fourth_pred = Column(String)
    #4
    fifth_pred = Column(String)
    # -2: No response from the user
    ground_truth = Column(Integer,default=-2)