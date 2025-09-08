from pydantic import BaseModel

class BookRequest(BaseModel):
    id: int
    name: str
    author: str
    rating: int
    price: int
    description: str