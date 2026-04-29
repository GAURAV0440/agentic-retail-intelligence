def compute_product_score(product, filters):
    score = 0

    # 1. Sale priority (revenue optimization)
    if filters.get("prefer_sale") and product.get("is_sale"):
        score += 3

    # 2. Bestseller importance (customer preference)
    score += float(product.get("bestseller_score", 0)) * 2

    # 3. Tag relevance (matching user intent)
    user_tags = filters.get("tags", [])
    product_tags = product.get("tags", [])

    tag_matches = sum(1 for tag in user_tags if tag in product_tags)
    score += tag_matches * 1.5

    # 4. Price efficiency (closer to budget = better)
    if filters.get("max_price") is not None:
        price = product.get("price", 0)
        max_price = filters["max_price"]

        if price <= max_price and max_price > 0:
            score += (max_price - price) / max_price

    return score


def rank_products(products, filters):
    scored_products = []

    for product in products:
        p = product.copy()  # ✅ avoid mutating original
        p["score"] = compute_product_score(product, filters)
        scored_products.append(p)

    return sorted(scored_products, key=lambda x: x["score"], reverse=True)