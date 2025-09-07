from fastapi import FastAPI
from fastapi.params import Body

BOOKS = [
        {"id": 1, "name": "Welcome to Python", "author": "Syed Ibrahim"},
        {"id": 2, "name": "Welcome to Java", "author": "Syed Hakeem"},
        {"id": 3, "name": "Welcome to JavaScript", "author": "Afrin Fathima"},
        {"id": 4, "name": "Welcome to MySql", "author": "Ibrahim"},
        {"id": 5, "name": "Welcome to Postgresql", "author": "Hakeem"},
    ]

app = FastAPI()

@app.get("/")
async def hello():
    return {
        "message": "The Books API is working"
    }

@app.get("/books")
def get_books():
    return BOOKS

@app.get("/books/{author_name}")
def get_book_by_author_name(author_name: str):
    for book in BOOKS:
        if book.get("author").casefold() == author_name.casefold():
            return book
    return {"message": "No Book found"}

@app.get("/books/")
def get_book_by_id(id: int):
    for book in BOOKS:
        if book.get('id') == id:
            return book
    return {"message": "No Book found"}

@app.post("/books/create")
def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return BOOKS

@app.put("/books/update")
def update_book(book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i]['id'] == book.get("id"):
            BOOKS[i] = book
            return BOOKS
    return f"No Book found with id {book.get('id')}"

@app.delete("/books/delete/{book_id}")
def delete_book_by_id(book_id: int):
    for index, book in enumerate(BOOKS):
        if book.get("id") == book_id:
            BOOKS.pop(index)
    return BOOKS