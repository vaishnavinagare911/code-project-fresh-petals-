from app.extensions import mongo
from bson import ObjectId
from datetime import datetime


def _product_brief(product_doc):
    if not product_doc:
        return None
    return {
        "product_id": str(product_doc["_id"]),
        "name": product_doc.get("name", ""),
        "price": float(product_doc.get("price", 0) or 0),
        "image": (product_doc.get("images") or [""])[0],
        "category": product_doc.get("category", ""),
        "stock": int(product_doc.get("stock", 0) or 0),
    }


def get_wishlist(user_id: str):
    wishlist = mongo.db.wishlists.find_one({"user_id": user_id}) or {"items": []}
    items = wishlist.get("items", []) or []

    products = []
    for item in items:
        pid = item.get("product_id")
        if not pid:
            continue
        try:
            product = mongo.db.products.find_one({"_id": ObjectId(pid)})
        except Exception:
            product = None
        brief = _product_brief(product)
        if brief:
            products.append(brief)

    return {"items": products}


def add_to_wishlist(user_id: str, product_id: str):
    try:
        product = mongo.db.products.find_one({"_id": ObjectId(product_id)})
    except Exception:
        product = None
    if not product:
        return {"message": "Product not found"}, 404

    existing = mongo.db.wishlists.find_one(
        {"user_id": user_id, "items.product_id": product_id},
        {"_id": 1},
    )
    if existing:
        return {"message": "Already in wishlist"}

    mongo.db.wishlists.update_one(
        {"user_id": user_id},
        {
            "$set": {"user_id": user_id},
            "$push": {
                "items": {"product_id": product_id, "created_at": datetime.utcnow()}
            },
        },
        upsert=True,
    )
    return {"message": "Added to wishlist"}


def remove_from_wishlist(user_id: str, product_id: str):
    mongo.db.wishlists.update_one(
        {"user_id": user_id},
        {"$pull": {"items": {"product_id": product_id}}},
    )
    return {"message": "Removed from wishlist"}

