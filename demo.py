#!/usr/bin/env python3
import subprocess
import time
import httpx


def prompt_user():
    print("Enter a new user")
    return {
        "id": int(input("User id: ")),
        "name": input("Name: "),
        "email": input("Email: "),
    }


def prompt_order():
    print("\nEnter a new order")
    return {
        "id": int(input("Order id: ")),
        "item": input("Item: "),
        "quantity": int(input("Quantity: ")),
        "price": float(input("Price: ")),
        "status": "pending",
    }


def prompt_payment(order_id, amount):
    print("\nEnter a new payment")
    return {
        "id": int(input("Payment id: ")),
        "order_id": order_id,
        "amount": amount,
        "status": "completed",
    }

SERVICES = [
    ("backend.order-service.main:app", 8000),
    ("backend.user-service.main:app", 8001),
    ("backend.payment-service.main:app", 8002),
]

procs = [
    subprocess.Popen(
        ["uvicorn", module, "--port", str(port)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    for module, port in SERVICES
]

time.sleep(2)

client = httpx.Client()
try:
    while True:
        user = prompt_user()
        print("Creating user:", client.post("http://localhost:8001/users", json=user).json())

        order = prompt_order()
        print("Creating order:", client.post("http://localhost:8000/orders", json=order).json())

        payment = prompt_payment(order["id"], order["price"] * order["quantity"])
        print("Creating payment:", client.post("http://localhost:8002/payments", json=payment).json())

        print("\nCurrent users:", client.get("http://localhost:8001/users").json())
        print("Current orders:", client.get("http://localhost:8000/orders").json())
        print("Current payments:", client.get("http://localhost:8002/payments").json())

        if input("\nAdd another set? [y/N]: ").lower() != "y":
            break
finally:
    for p in procs:
        p.terminate()
    for p in procs:
        p.wait()
