from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    number1: float
    number2: float

@app.post("/add")
async def add_twonum(item: Item):
    return {"result": item.number1 + item.number2 }



