from fastapi import APIRouter


router = APIRouter()


@router.get("/blogs")
def get_blogs() -> dict[str, str]:
    return {"message": "all blogs"}