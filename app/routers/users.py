from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.db.core import get_db
from app.schemas import UserIn, UserOut
from app.services.users import create_db_user, get_db_users, get_db_user_id


router = APIRouter()


@router.post("/users", response_model=UserOut)
def create_user(user: UserIn, db: Session = Depends(get_db)) -> UserOut:
    return create_db_user(user, db)


@router.get("/users", response_model=list[UserOut])
def get_users(db: Session = Depends(get_db)) -> list[UserOut]:
    return get_db_users(db)


@router.get("/users/{id}", response_model=UserOut)
def get_user_id(id: int, db: Session = Depends(get_db))-> UserOut:
    return get_db_user_id(id, db)
