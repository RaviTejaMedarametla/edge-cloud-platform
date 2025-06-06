from fastapi import FastAPI, HTTPException
from typing import List
from .models import Payment

app = FastAPI()

payments: List[Payment] = []

@app.get("/payments", response_model=List[Payment])
def list_payments():
    return payments

@app.post("/payments", response_model=Payment)
def create_payment(payment: Payment):
    payments.append(payment)
    return payment

@app.get("/payments/{payment_id}", response_model=Payment)
def get_payment(payment_id: int):
    for p in payments:
        if p.id == payment_id:
            return p
    raise HTTPException(status_code=404, detail="Payment not found")

@app.put("/payments/{payment_id}", response_model=Payment)
def update_payment(payment_id: int, updated: Payment):
    for idx, p in enumerate(payments):
        if p.id == payment_id:
            payments[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Payment not found")

@app.delete("/payments/{payment_id}")
def delete_payment(payment_id: int):
    for idx, p in enumerate(payments):
        if p.id == payment_id:
            del payments[idx]
            return {"status": "deleted"}
    raise HTTPException(status_code=404, detail="Payment not found")
