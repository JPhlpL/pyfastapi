from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#create BaseModel using Class
class Item(BaseModel):
    item_name: str  # type: ignore

@app.get("/{desc}", description='get sample') #, deprecated=True)
async def get(desc: str):
    return {"message": "get", "item": desc}

@app.post("/")
#use class item basemodel for post
def post(item:Item):
    return {"message": {"first": ["hello","amigo"], "second": "hola"}, "item_name": item.item_name}


@app.put("/{item}")
async def put(item):
    return {"message": "put", "item": item}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetable = "vegetables"

@app.get('/foods/{food_name}')
async def get_food(foodname: FoodEnum):
    if foodname == FoodEnum.vegetable:
        return {"foodname": "food", "message": "you ar eeating vegetable"}

    elif foodname == FoodEnum.fruits:
        return {"foodname": "food", "message": "you ar eeating fruits"}
