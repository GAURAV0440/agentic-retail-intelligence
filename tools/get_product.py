def run(product_id, products):
    if not product_id:
        return None

    for p in products:
        if p.get("product_id") == product_id:
            return p

    return None