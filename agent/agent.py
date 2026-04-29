import json
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("BASE_URL")
)

MODEL = os.getenv("MODEL")


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_products",
            "description": "Search products based on filters",
            "parameters": {
                "type": "object",
                "properties": {
                    "max_price": {"type": "number"},
                    "tags": {"type": "array", "items": {"type": "string"}},
                    "keywords": {"type": "array", "items": {"type": "string"}},
                    "size": {"type": "string"},
                    "prefer_sale": {"type": "boolean"}
                },
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_order",
            "description": "Fetch order details using order_id",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {"type": "string"}
                },
                "required": ["order_id"]
            }
        }
    }
]


def run_agent(user_input, products, orders):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a retail AI assistant. "
                "Use tools for all decisions. "
                "Do not guess or hallucinate. "
                "For shopping queries → use search_products. "
                "For order queries → use get_order."
            )
        },
        {"role": "user", "content": user_input}
    ]

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            max_tokens=800  # 🔥 IMPORTANT FIX
        )

        msg = response.choices[0].message

        # ✅ If tool is called
        if msg.tool_calls:
            tool_call = msg.tool_calls[0]
            name = tool_call.function.name
            args = json.loads(tool_call.function.arguments or "{}")

            # 🔍 DEBUG (add here)
            print("\n--- DEBUG TOOL CALL ---")
            print("TOOL:", name)
            print("ARGS:", args)
            print("-----------------------\n")

            # 🔍 Product Search
            if name == "search_products":
                from tools.search_products import run
                results = run(args, products)

                return {
                    "type": "product_results",
                    "data": results
                }

            # 📦 Order Handling + Return Logic
            elif name == "get_order":
                from tools.get_order import run as get_order
                from tools.get_product import run as get_product
                from tools.evaluate_return import run as evaluate_return

                order = get_order(args.get("order_id"), orders)

                if not order:
                    return {
                        "type": "error",
                        "message": "Order not found. Please check the order ID."
                    }

                product = get_product(order["product_id"], products)

                if not product:
                    return {
                        "type": "error",
                        "message": "Associated product not found."
                    }

                decision = evaluate_return(order, product)

                return {
                    "type": "return_decision",
                    "order": order,
                    "product": product,
                    "decision": decision
                }

        # ⚠️ No tool used (fallback)
        return {
            "type": "message",
            "message": msg.content or "I couldn't process your request."
        }

    except Exception as e:
        return {
            "type": "error",
            "message": f"Something went wrong: {str(e)}"
        }