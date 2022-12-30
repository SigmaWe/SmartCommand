from sqlalchemy import Column, String, Integer,Enum, ForeignKey
from database import Base
import enum
from MLmodels.helper import recover_command

class VSQuery(Base):
    __tablename__ = "vsqueries"

    id = Column(Integer, primary_key = True)
    query = Column(String, index=True)
    model_name = Column(String,index=True)
    selected_command = Column(Integer,ForeignKey("commands.command_id"), default=1)

class VSCommand(Base):
    __tablename__ = "commands"
    command = Column(String,unique=True)
    command_id = Column(Integer, primary_key=True)