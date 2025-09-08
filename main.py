from fastapi import FastAPI

from Book import Book

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