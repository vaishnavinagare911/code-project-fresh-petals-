from app.extensions import mongo
from bson import ObjectId

def get_home_data():
    """
    Fetch up to 10 products from the products collection. Converts each _id
    to string and returns {"products": [...]}.
    """
    products = list(mongo.db.products.find())
    for p in products:
        p["_id"] = str(p["_id"])
    return {"products": products}

def search_products(query):
    """
    Find products whose name matches the given query (case-insensitive).
    Returns {"results": [...]} with _id converted to string per product.
    """
    products = list(mongo.db.products.find({"name": {"$regex": query, "$options": "i"}}))
    for p in products:
        p["_id"] = str(p["_id"])
    return {"results": products}

def get_details(product_id):
    """
    Return one product by id. Converts _id to string.
    Returns (message, 404) if the product is not found or id is invalid.
    """
    product = mongo.db.products.find_one({"_id": ObjectId(product_id)})
    if not product:
        return {"message": "Product not found"}, 404
    product["_id"] = str(product["_id"])
    return product