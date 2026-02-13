from fastapi import FastAPI, APIRouter
from .routers import blogs, users


app = FastAPI()

@app.get("/")
def root():
    return {"message" : "home page, lol !"}

app.include_router(blogs.router)
app.include_router(users.router)