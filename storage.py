import json
import os

ORDERS_FILE = "orders.json"

def load_orders():
    if not os.path.exists(ORDERS_FILE):
        return []
    with open(ORDERS_FILE, 'r') as f:
        return json.load(f)

def save_orders(data):
    with open(ORDERS_FILE, 'w') as f:
        json.dump(data, f, indent=2)
