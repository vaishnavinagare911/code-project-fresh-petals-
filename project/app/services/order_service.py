from app.extensions import mongo
from bson import ObjectId
from datetime import datetime

def place_order(user_id):
    """
    Convert the user's cart into an order and clear the cart.
    Returns (message, 400) if the cart is empty; otherwise returns a
    success message.
    """
    cart = mongo.db.cart.find_one({"user_id": user_id})
    if not cart:
        return {"message": "Cart empty"}, 400

    order = {
        "user_id": user_id,
        "items": cart["items"],
        "payment_status": "Paid",
        "order_status": "Processing",
        "created_at": datetime.utcnow()
    }

    mongo.db.orders.insert_one(order)
    mongo.db.cart.delete_one({"user_id": user_id})

    return {"message": "Order placed successfully"}

def get_my_orders(user_id):
    """
    Return all orders for the user, most recent first. Each order's items
    are enriched with product name and price. Returns {"orders": [...]}.
    """
    orders = list(mongo.db.orders.find({"user_id": user_id}).sort("created_at", -1))
    for o in orders:
        o["_id"] = str(o["_id"])
        enriched = []
        for item in o.get("items", []):
            product = mongo.db.products.find_one({"_id": ObjectId(item["product_id"])})
            if product:
                enriched.append({
                    "product_id": item["product_id"],
                    "name": product.get("name", ""),
                    "price": float(product.get("price", 0)),
                    "quantity": item.get("quantity", 1)
                })
        o["items"] = enriched
    return {"orders": orders}