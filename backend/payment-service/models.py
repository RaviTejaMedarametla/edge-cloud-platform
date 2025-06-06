from pydantic import BaseModel
from typing import Optional

class Payment(BaseModel):
    id: int
    order_id: int
    amount: float
    status: str = "pending"
