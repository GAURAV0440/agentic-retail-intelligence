from core.loader import load_products, load_orders
from agent.agent import run_agent


products = load_products()
orders = load_orders()


while True:
    query = input("\nEnter query (or type 'exit' to quit): ")

    if query.lower() in ["exit", "quit"]:
        print("Exiting... 👋")
        break

    result = run_agent(query, products, orders)

    # 🛍️ Product Recommendations
    if result.get("type") == "product_results":
        products_list = result.get("data", [])

        if not products_list:
            print("\nNo matching products found. Try adjusting your preferences.")
        else:
            print("\nRecommended Products:")

            for p in products_list:
                print(f"\n{p['title']} - ₹{p['price']}")

                reasons = []

                if p.get("is_sale"):
                    reasons.append("currently on sale")

                if p.get("bestseller_score", 0) >= 4:
                    reasons.append("high customer popularity")

                if p.get("price"):
                    reasons.append(f"within your budget")

                if p.get("sizes_available"):
                    reasons.append("available in your requested size")

                if not reasons:
                    reasons.append("relevant to your preferences")

                print("Reason:", ", ".join(reasons))

    # 📦 Return Decision
    elif result.get("type") == "return_decision":
        decision = result.get("decision", {})

        print("\nReturn Decision:")
        print(f"Eligible: {decision.get('eligible')}")

        if decision.get("type"):
            print(f"Type: {decision.get('type')}")

        print(f"Reason: {decision.get('reason')}")

    # ❌ Errors
    elif result.get("type") == "error":
        print(f"\nError: {result.get('message')}")

    # 💬 Fallback Message
    else:
        print(f"\n{result.get('message', 'Something went wrong.')}")