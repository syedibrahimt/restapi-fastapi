from fastapi import FastAPI

from models.Book import Book
from pydantic_models.BookRequest import BookRequest
from utils.BookUtils import get_book_with_id

app = FastAPI()

BOOK_LIST = [
    Book(1, "Learn Java", "Java Author", 5, 500, "this is the description of the java book"),
    Book(2, "Learn Python", "Java Author", 5, 500, "this is the description of the java book"),
    Book(3, "Learn JavaScript", "Java Author", 4, 500, "this is the description of the java book"),
    Book(4, "Learn Rust", "Java Author", 4, 500, "this is the description of the java book"),
    Book(5, "Learn C++", "Java Author", 3, 400, "this is the description of the java book"),
]
@app.get("/")
def test():
    return "Book API is working fine"

@app.get("/books")
def get_all_books():
    return BOOK_LIST

@app.post("/books/create")
def create_book(new_book: BookRequest):
    book = get_book_with_id(Book(**new_book.model_dump()), BOOK_LIST)
    BOOK_LIST.append(book)
    return BOOK_LIST

@app.get("/book/{book_id}")
def get_book_by_id(book_id: int):
    for book in BOOK_LIST:
        if book.id == book_id:
            return book
    return None

@app.get("/book/")
def get_books_by_rating(book_rating: int):
    books_to_return = []
    for book in BOOK_LIST:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

@app.put('/book/')
def update_book(book: BookRequest):
    for i, b in enumerate(BOOK_LIST):
        if b.id == book.id:
            BOOK_LIST[i] = book
            break
    return BOOK_LIST

@app.delete("/book/")
def delete_book_by_id(book_id: int):
    for i, b in enumerate(BOOK_LIST):
        if b.id == book_id:
            BOOK_LIST.pop(i)
    return BOOK_LIST