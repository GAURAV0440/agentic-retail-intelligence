def match_keywords(product, keywords):
    text = (product.get("title", "") + " " + " ".join(product.get("tags", []))).lower()
    return any(keyword.lower() in text for keyword in keywords)


def is_size_available(product, size):
    size = str(size)

    sizes = [str(s) for s in product.get("sizes_available", [])]
    stock = product.get("stock_per_size", {})

    return size in sizes and stock.get(size, 0) > 0


def search_products(filters, products):
    candidates = []

    for product in products:

        score = 0

        # Price filter (strict)
        if filters.get("max_price") is not None:
            if product.get("price", 0) > filters["max_price"]:
                continue

        # Size handling (soft)
        if filters.get("size"):
            if is_size_available(product, filters["size"]):
                score += 3
            else:
                score -= 1

        # Tag matching (flexible)
        if filters.get("tags"):
            product_tags = product.get("tags", [])
            tag_matches = sum(
                1 for tag in filters["tags"]
                for pt in product_tags
                if tag.lower() in pt.lower() or pt.lower() in tag.lower()
            )
            score += tag_matches * 2

        # Keyword scoring
        if filters.get("keywords"):
            if match_keywords(product, filters["keywords"]):
                score += 2

        # Sale preference
        if filters.get("prefer_sale") and product.get("is_sale"):
            score += 2

        # Bestseller normalization (IMPORTANT FIX)
        score += product.get("bestseller_score", 0) / 20

        # Copy product
        p = product.copy()
        p["score"] = score

        candidates.append(p)

    if not candidates:
        return []

    candidates.sort(key=lambda x: x["score"], reverse=True)

    return candidates[:5]