from fastapi import FastAPI, Path
app = FastAPI()

@app.get("/hello/{name}")

async def hello(name:str=Path(...,min_length=3,max_length=10)):
   return {"name": name}