from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

import os

# all models should share this Base
Base = declarative_base()

load_dotenv()

# configure connection to postgre
DATABASE_URL = os.getenv("DB_CONNECTION_STRING")

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autoflush=True, bind=engine)


# Inject a fresh db session into each api request
def get_db():
    db = SessionLocal()  # Opens session
    try:
        yield db  #
    finally:
        db.close()
