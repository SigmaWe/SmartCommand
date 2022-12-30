from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost:5432/postgres"
# SQLALCHEMY_DATABASE_URL = "postgresql://service:password@pgsql:5432/database"

if 'USE_REMOTE_POSTGRESQL' in os.environ:
    DB_HOST=os.environ['AZURE_POSTGRESQL_HOST']
    DB_NAME=os.environ['AZURE_POSTGRESQL_DATABASE']
    DB_USER=os.environ['AZURE_POSTGRESQL_USERNAME']
    DB_PASS=os.environ['AZURE_POSTGRESQL_PASSWORD']
else:
    DB_HOST=os.environ['LOCAL_HOST']
    DB_NAME=os.environ['LOCAL_DATABASE']
    DB_USER=os.environ['LOCAL_USERNAME']
    DB_PASS=os.environ['LOCAL_PASSWORD']


SQLALCHEMY_DATABASE_URL = 'postgresql://{dbuser}:{dbpass}@{dbhost}:5432/{dbname}'.format(
    dbuser=DB_USER,
    dbpass=DB_PASS,
    dbhost=DB_HOST,
    dbname=DB_NAME
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Sessionlocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()