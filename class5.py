from enum import Enum
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


# List is store multiple values in a one variable
@app.get("/items/")
async def read_items(q: list[str] | None = Query(None, max_length=10, min_length=3)): # Means that list acceptable in 3 items min and 10 items
    result = {"items": [{"item_a": "pencil"},{"item_b": "paper"}]}
    if q:
        result.update({"q": q})
    return result

@app.get("/items_inc/")
async def read_items(q: list[str] = Query(["foo", "bar"])): #  Incremental
    result = {"items": [{"item_a": "pencil"},{"item_b": "paper"}]}
    if q:
        result.update({"q": q})
    return result

@app.get("/items_alias/")
async def read_items(q: list[str] | None = Query(None, alias="item-q", include_in_schema=False)): #  item_alias/?item-q=foo(Use of alias)
    result = {"items": [{"item_a": "pencil"},{"item_b": "paper"}]}                                 # if want to hide schema
    if q:
        result.update({"q": q})
    return result


