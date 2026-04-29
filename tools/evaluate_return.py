from core.returns import evaluate_return


def run(order, product):
    if not order or not product:
        return {
            "eligible": False,
            "reason": "Invalid order or product data"
        }

    return evaluate_return(order, product)