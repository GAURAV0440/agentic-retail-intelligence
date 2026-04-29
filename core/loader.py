import pandas as pd
from datetime import datetime
import json


def load_products(path="data/product_inventory.csv"):
    df = pd.read_csv(path)

    products = []

    for _, row in df.iterrows():
        product = {
            "product_id": str(row.get("product_id", "")),
            "title": str(row.get("title", "")),
            "vendor": str(row.get("vendor", "")),
            "price": safe_float(row.get("price")),
            "compare_at_price": safe_float(row.get("compare_at_price")),
            "tags": parse_tags(row.get("tags")),
            "sizes_available": parse_sizes(row.get("sizes_available")),
            "stock_per_size": parse_stock(row.get("stock_per_size")),
            "is_sale": parse_bool(row.get("is_sale")),
            "is_clearance": parse_bool(row.get("is_clearance")),
            "bestseller_score": safe_float(row.get("bestseller_score"))
        }
        products.append(product)

    return products


def parse_tags(value):
    if not value or str(value).strip() == "":
        return []
    return [v.strip().lower() for v in str(value).split(",")]


def parse_sizes(value):
    if not value or str(value).strip() == "":
        return []
    return [v.strip() for v in str(value).split("|")]


def parse_stock(stock_str):
    try:
        if not stock_str or str(stock_str).strip() == "":
            return {}
        return json.loads(str(stock_str).replace("'", '"'))
    except:
        return {}


def parse_bool(value):
    return str(value).strip().lower() == "true"


def safe_float(value):
    try:
        return float(value)
    except:
        return 0.0


def load_orders(path="data/orders.csv"):
    df = pd.read_csv(path)

    orders = []

    for _, row in df.iterrows():
        order = {
            "order_id": str(row.get("order_id", "")),
            "order_date": parse_date(row.get("order_date")),
            "product_id": str(row.get("product_id", "")),
            "size": str(row.get("size", "")),
            "price_paid": safe_float(row.get("price_paid")),
            "customer_id": str(row.get("customer_id", ""))
        }
        orders.append(order)

    return orders


def parse_date(date_str):
    try:
        return datetime.strptime(str(date_str), "%Y-%m-%d")
    except:
        return datetime.now()


def load_policy(path="data/policy.txt"):
    with open(path, "r") as f:
        return f.read()