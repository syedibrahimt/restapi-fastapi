from typing import Optional

from pydantic import BaseModel, Field


class BookRequest(BaseModel):
    id: Optional[int] = Field(description="id is not needed", default=None)
    name: str = Field(min_length=3)
    author: str = Field(min_length=3)
    rating: int = Field(gt=0, lt=6)
    price: int = Field(gt=0, lt=1000)
    description: str = Field(min_length=10)

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "A new book",
                "author": "A new Author",
                "rating": 3,
                "price": 500,
                "description": "A sample description"
            }
        }
    }