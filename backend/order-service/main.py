from fastapi import FastAPI, HTTPException
from typing import List
from .models import Order

app = FastAPI()

orders: List[Order] = []

@app.get("/orders", response_model=List[Order])
def list_orders():
    return orders

@app.post("/orders", response_model=Order)
def create_order(order: Order):
    orders.append(order)
    return order

@app.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: int):
    for o in orders:
        if o.id == order_id:
            return o
    raise HTTPException(status_code=404, detail="Order not found")

@app.put("/orders/{order_id}", response_model=Order)
def update_order(order_id: int, updated: Order):
    for idx, o in enumerate(orders):
        if o.id == order_id:
            orders[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Order not found")

@app.delete("/orders/{order_id}")
def delete_order(order_id: int):
    for idx, o in enumerate(orders):
        if o.id == order_id:
            del orders[idx]
            return {"status": "deleted"}
    raise HTTPException(status_code=404, detail="Order not found")
