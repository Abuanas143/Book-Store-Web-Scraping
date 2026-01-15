from fastapi import FastAPI
from books import router as book_router
from auth import router as auth_router

app = FastAPI(title="Book Data System")

app.include_router(auth_router)
app.include_router(book_router)
