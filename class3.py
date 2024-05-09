from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Query Parameters
fake_items_db = [{"item":"pencil"},{"item":"ballpen"},{"item":"paper"}]

@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

@app.get("/items/{item_id}")
async def get_items(item_id: str, q: str | None = None, Description: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if Description:
        item.update({"description": "true"})
    return item

@app.get("/users/{user_id}")
async def read_user_email(user_id: str, email: str | None = None):
    user = {"user_id": user_id, "user_email": email}
    if email == None:
        user.update({"Status": {"HTTP STATUS": 204, "Message": "Email Not Found"}})
    else:
        user.update({"Status": {"HTTP STATUS": 200, "Message": "Done"}})
    return user
