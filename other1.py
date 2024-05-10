from typing import List
from fastapi import FastAPI
from uuid import UUID, uuid4
from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("e108cc64-674a-4572-86e8-3be003689703"), 
        first_name="John", 
        middle_name="O",
        last_name="Philip",
        gender=Gender.male,
        roles=[Role.admin]
    ),
    User(
        id=UUID("9b575130-bd44-42a6-9dc6-ccfaa7886df5"), 
        first_name="Alex", 
        middle_name="O",
        last_name="Margo",
        gender=Gender.female,
        roles=[Role.user]
    )
]

@app.get("/")

async def root():
    return {"Hello": "World"}

@app.get("/api/v1/users")

async def fetch_user():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id:": user.id}