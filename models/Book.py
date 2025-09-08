class Book:
    id: int
    name: str
    author: str
    rating: int
    price: int
    description: str

    def __init__(self, id: int, name: str, author: str, rating: int, price: int, description: str):
        self.id = id
        self.name = name
        self.author = author
        self.price = price
        self.rating = rating
        self.description = description
