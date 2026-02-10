from fastapi import APIRouter


router = APIRouter()


@router.get("/blogs")
def get_posts():
    return {"message": "all blogs"}