from fastapi import APIRouter, Depends, HTTPException
from security import get_current_user
from scraper import scrape_books
from curd import insert_book, get_books

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/scrape")
def scrape_and_save(current_user: dict = Depends(get_current_user)):

    if not current_user.get("is_admin"):
        raise HTTPException(status_code=403, detail="Admins only")

    books = scrape_books()

    for book in books:
        insert_book(book)   # ✅ pass dict directly

    return {"message": f"{len(books)} books saved successfully"}



@router.get("/")
def list_books():
    return get_books()





