from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db.models import Users
from app.schemas import UserOut

def create_db_user(user, session : Session):
    new_user = Users(email=str(user.email), password_hash=user.password)

    session.add(new_user)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="email already exists",
        )
    session.refresh(new_user)
    return new_user

def get_db_users(session : Session):
    query = select(Users)
    # using .scalars() makes it so that it returns 1 obj per row 
    users = session.scalars(query).all()
    return users

def get_db_user_id(id:int, session : Session)->UserOut:

    query = select(Users).where(Users.id == id)
    user = session.scalar(query)
    if user:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")