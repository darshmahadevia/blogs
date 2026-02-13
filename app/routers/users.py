from fastapi import APIRouter


router = APIRouter()

@router.get("/users")
def get_users() -> dict[str, str]:
    return {"message": "returned all user info"}

