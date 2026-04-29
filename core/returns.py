from datetime import datetime


def evaluate_return(order, product):
    today = datetime.now()
    days_since = (today - order["order_date"]).days

    if product["is_clearance"]:
        return {
            "eligible": False,
            "reason": "Clearance item is final sale"
        }

    if product["vendor"] == "Aurelia Couture":
        return {
            "eligible": True,
            "type": "exchange_only",
            "reason": "Vendor policy allows only exchanges"
        }

    if product["vendor"] == "Nocturne":
        allowed_days = 21
    elif product["is_sale"]:
        allowed_days = 7
    else:
        allowed_days = 14

    if days_since > allowed_days:
        return {
            "eligible": False,
            "reason": "Return window expired"
        }

    if product["is_sale"]:
        return {
            "eligible": True,
            "type": "store_credit",
            "reason": "Sale item eligible for store credit"
        }

    return {
        "eligible": True,
        "type": "full_refund",
        "reason": "Eligible for full refund"
    }