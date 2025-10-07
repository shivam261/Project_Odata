from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}