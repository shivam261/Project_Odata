import logging
import os
from sqlmodel import Session, SQLModel, create_engine
from dotenv import load_dotenv

load_dotenv()

POSTGRES_SERVICE_URL = os.getenv("POSTGRES_SERVICE_URL")
engine = create_engine(POSTGRES_SERVICE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
