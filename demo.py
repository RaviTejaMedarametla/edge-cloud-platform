#!/usr/bin/env python3
import subprocess
import time
import httpx
from textwrap import dedent


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


def show_endpoints():
    print(
        dedent(
            """
            Available API endpoints:
              Users   -> http://localhost:8001/users
              Orders  -> http://localhost:8000/orders
              Payments-> http://localhost:8002/payments
            """
        )
    )

print("Launching services...\n")
procs = [
    subprocess.Popen(
        ["uvicorn", module, "--port", str(port)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    for module, port in SERVICES
]
time.sleep(2)
show_endpoints()

client = httpx.Client()
users = []
orders = []
payments = []

try:
    while True:
        user = prompt_user()
        resp = client.post("http://localhost:8001/users", json=user).json()
        users.append(resp)
        print("Creating user:", resp)

        order = prompt_order()
        resp = client.post("http://localhost:8000/orders", json=order).json()
        orders.append(resp)
        print("Creating order:", resp)

        payment = prompt_payment(order["id"], order["price"] * order["quantity"])
        resp = client.post("http://localhost:8002/payments", json=payment).json()
        payments.append(resp)
        print("Creating payment:", resp)

        print("\nCurrent users:", client.get("http://localhost:8001/users").json())
        print("Current orders:", client.get("http://localhost:8000/orders").json())
        print("Current payments:", client.get("http://localhost:8002/payments").json())

        if input("\nAdd another set? [y/N]: ").lower() != "y":
            break
finally:
    print("\nSummary: {} users, {} orders, {} payments".format(len(users), len(orders), len(payments)))
    for p in procs:
        p.terminate()
    for p in procs:
        p.wait()
