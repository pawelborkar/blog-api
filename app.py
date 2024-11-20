from datetime import timezone

from fastapi import FastAPI, status
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    image_name: str
    url: HttpUrl


class Item(BaseModel):
    name: str
    description: str
    quantity: int
    inventory: int | None = 1
    images: list[Image] | None = None

class User(BaseModel):
    id: int
    fullname: str
    username: str
    password: str
    created_at: timezone




@app.get("/home", status_code=status.HTTP_200_OK)
async def home() -> dict:
    return {"message": "Welcome to home"}

