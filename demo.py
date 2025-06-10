#!/usr/bin/env python3
import subprocess
import time
import httpx

SERVICES = [
    ("backend.order-service.main:app", 8000),
    ("backend.user-service.main:app", 8001),
    ("backend.payment-service.main:app", 8002),
]

procs = [subprocess.Popen(["uvicorn", module, "--port", str(port)]) for module, port in SERVICES]

time.sleep(2)

client = httpx.Client()
try:
    user = {"id": 1, "name": "Alice", "email": "alice@example.com"}
    order = {"id": 1, "item": "Book", "quantity": 1, "price": 12.99, "status": "pending"}
    payment = {"id": 1, "order_id": 1, "amount": 12.99, "status": "completed"}

    print("Creating user:", client.post("http://localhost:8001/users", json=user).json())
    print("Creating order:", client.post("http://localhost:8000/orders", json=order).json())
    print("Creating payment:", client.post("http://localhost:8002/payments", json=payment).json())

    print("All users:", client.get("http://localhost:8001/users").json())
    print("All orders:", client.get("http://localhost:8000/orders").json())
    print("All payments:", client.get("http://localhost:8002/payments").json())
finally:
    for p in procs:
        p.terminate()
    for p in procs:
        p.wait()
