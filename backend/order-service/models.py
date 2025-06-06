from pydantic import BaseModel
from typing import Optional

class Order(BaseModel):
    id: int
    item: str
    quantity: int
    price: float
    status: str = "pending"
