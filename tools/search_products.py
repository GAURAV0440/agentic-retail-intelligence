from core.search import search_products


def run(filters, products):
    if not isinstance(filters, dict):
        return []
    return search_products(filters, products)