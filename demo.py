#!/usr/bin/env python3
import subprocess
import time
import httpx

SERVICES = [
    ("backend.order-service.main:app", 8000),
    ("backend.user-service.main:app", 8001),
    ("backend.payment-service.main:app", 8002),
]

procs = [subprocess.Popen(["uvicorn", module, "--port", str(port)], stdout=subprocess.DEVNULL) for module, port in SERVICES]

time.sleep(2)

client = httpx.Client()
try:
    print("Enter a new user")
    user = {
        "id": int(input("User id: ")),
        "name": input("Name: "),
        "email": input("Email: ")
    }
    print("Creating user:", client.post("http://localhost:8001/users", json=user).json())

    print("\nEnter a new order")
    order = {
        "id": int(input("Order id: ")),
        "item": input("Item: "),
        "quantity": int(input("Quantity: ")),
        "price": float(input("Price: ")),
        "status": "pending",
    }
    print("Creating order:", client.post("http://localhost:8000/orders", json=order).json())

    print("\nEnter a new payment")
    payment = {
        "id": int(input("Payment id: ")),
        "order_id": order["id"],
        "amount": order["price"] * order["quantity"],
        "status": "completed",
    }
    print("Creating payment:", client.post("http://localhost:8002/payments", json=payment).json())

    print("\nAll users:", client.get("http://localhost:8001/users").json())
    print("All orders:", client.get("http://localhost:8000/orders").json())
    print("All payments:", client.get("http://localhost:8002/payments").json())
finally:
    for p in procs:
        p.terminate()
    for p in procs:
        p.wait()
