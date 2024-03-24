from fastapi import APIRouter

router = APIRouter()

@router.get("/Books")
def get_books():
    return {"Topic": "Books"}