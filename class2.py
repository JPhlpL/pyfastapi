from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetable = "vegetables"

@app.get('/foods/{food_name}')
async def get_food(foodname: FoodEnum):
    if foodname == FoodEnum.vegetable:
        return {"foodname": "food", "message": "you ar eeating vegetable"}

    elif foodname == FoodEnum.fruits:
        return {"foodname": "food", "message": "you ar eeating fruits"}



