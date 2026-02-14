from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.core import init_db
from app.routers import users


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "home page, lol !"}


app.include_router(users.router)
