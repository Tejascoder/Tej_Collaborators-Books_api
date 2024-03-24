
from fastapi import APIRouter
from main import app as Book


router = APIRouter()

@router.get("/Books")
def get_books():
    return {"Topic": "Books"}
