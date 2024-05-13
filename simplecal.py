from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Math(BaseModel):
    number1: float
    number2: float
    operator: str

@app.post("/add")
async def add_twonum(item_math: Math):
    math_dict = item_math.dict()
    if math_dict["operator"] == '+':
        return {"result": item_math.number1 + item_math.number2 }
    elif math_dict["operator"] == '-':
        return {"result": item_math.number1 - item_math.number2 }
    elif math_dict["operator"] == '*':
        return {"result": item_math.number1 * item_math.number2 }
    elif math_dict["operator"] == '/':
        return {"result": item_math.number1 / item_math.number2 }
    else:
        return {"result": "Not a math operator" }
    



