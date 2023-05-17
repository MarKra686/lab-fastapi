from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}



class ItStudentCreateSchema(BaseModel):
    first_name: str
    last_name: str


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item