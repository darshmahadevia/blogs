from fastapi import FastAPI, APIRouter
from .routers import blogs


app = FastAPI()

@app.get("/")
def root():
    return {"message" : "home page, lol !"}

app.include_router(blogs.router)