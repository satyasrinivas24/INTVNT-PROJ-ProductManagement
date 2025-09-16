from fastapi import FastAPI, APIRouter
from routes.index import user
from config.db import meta, engine

app = FastAPI()

meta.create_all(engine)

app.include_router(user)


app = FastAPI()
@app.get('/')
def root():
    return{"message":"Backend is running!.."}
