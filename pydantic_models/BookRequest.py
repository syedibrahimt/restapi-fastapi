from typing import Optional

from pydantic import BaseModel, Field


class BookRequest(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=3)
    author: str = Field(min_length=3)
    rating: int = Field(gt=0, lt=6)
    price: int = Field(gt=0, lt=1000)
    description: str = Field(min_length=10)