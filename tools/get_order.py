def run(order_id, orders):
    if not order_id:
        return None

    for o in orders:
        if o.get("order_id") == order_id:
            return o

    return None