import os
from fastapi import FastAPI, Response
from contextlib import asynccontextmanager
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4
from orjson import dumps
from sqlmodel import Field, Session, SQLModel, create_engine, select
from dotenv import load_dotenv 
import logging
from src.database import create_db_and_tables, get_session
from src.auth.router import router as auth_router
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    logger.info("Creating database and tables...")
    create_db_and_tables()       # same logic as before
    yield                        # app runs here
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)


app.include_router(auth_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}