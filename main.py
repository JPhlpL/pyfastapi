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
    return {"message":"post", "item_name": item.item_name}


@app.put("/{item}")
async def put(item):
    return {"message": "put", "item": item}
