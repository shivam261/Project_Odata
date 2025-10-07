from fastapi import FastAPI, Response
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4
from orjson import dumps


class OrsonResponse(Response):
    media_type = "application/octet-stream"

    def render(self, content: any) -> bytes:
        return dumps(content)  # Serialize using Orson


app = FastAPI(default_response_class=OrsonResponse)


@app.get("/")
async def root():
    return {"message": "Hello World"}