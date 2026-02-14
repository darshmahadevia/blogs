from fastapi import APIRouter

from schemas import UserIn


router = APIRouter()

# CRUD on users


# creating user add hasing to password
@router.post("/users")
def create_user(user: UserIn) -> dict[str, str]:
    return {"email": user.email, "password": user.password}


@router.get("/users")
def get_users() -> dict[str, str]:
    return {"message": "returned all user info"}
