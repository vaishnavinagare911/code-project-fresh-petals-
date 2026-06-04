from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash
from bson import ObjectId
from datetime import datetime

from app.extensions import mongo

admin_bp = Blueprint("admin", __name__)

def _require_admin():
    user_id = get_jwt_identity()
    try:
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    except Exception:
        user = None
    if not user or user.get("role") != "admin":
        return None, ({"message": "Admin access required"}, 403)
    return user, None

@admin_bp.get("/stats")
@jwt_required()
def stats():
    
    _, err = _require_admin()
    if err:
        return err

    total_products = mongo.db.products.count_documents({})
    total_users = mongo.db.users.count_documents({})
    total_orders = mongo.db.orders.count_documents({})

    revenue_estimate = 0.0
    orders = mongo.db.orders.find({}, {"items": 1})
    for o in orders:
        for item in o.get("items", []) or []:
            try:
                product = mongo.db.products.find_one(
                    {"_id": ObjectId(item.get("product_id"))},
                    {"price": 1},
                )
                price = float((product or {}).get("price", 0) or 0)
            except Exception:
                price = 0.0
            qty = int(item.get("quantity", 0) or 0)
            revenue_estimate += price * qty

    return {
        "total_products": int(total_products),
        "total_users": int(total_users),
        "total_orders": int(total_orders),
        "revenue_estimate": round(float(revenue_estimate), 2),
    }


def _product_to_json(p):
    p["_id"] = str(p["_id"])
    return p


def _user_to_json(u):
    return {
        "_id": str(u["_id"]),
        "name": u.get("name", ""),
        "email": u.get("email", ""),
        "role": u.get("role", "user"),
        "created_at": u.get("created_at"),
    }


@admin_bp.get("/products")
@jwt_required()
def list_products():
    _, err = _require_admin()
    if err:
        return err

    query = (request.args.get("query") or "").strip()
    limit = min(max(int(request.args.get("limit") or 50), 1), 200)
    skip = max(int(request.args.get("skip") or 0), 0)

    mongo_query = {}
    if query:
        mongo_query = {
            "$or": [
                {"name": {"$regex": query, "$options": "i"}},
                {"category": {"$regex": query, "$options": "i"}},
            ]
        }

    products = list(
        mongo.db.products.find(mongo_query).sort("created_at", -1).skip(skip).limit(limit)
    )
    return {"products": [_product_to_json(p) for p in products]}


@admin_bp.post("/products")
@jwt_required()
def create_product():
    _, err = _require_admin()
    if err:
        return err

    data = request.json or {}
    name = (data.get("name") or "").strip()
    description = (data.get("description") or "").strip()
    if not name or not description:
        return {"message": "Name and description are required"}, 400

    product = {
        "name": name,
        "description": description,
        "price": float(data.get("price", 0) or 0),
        "stock": int(data.get("stock", 0) or 0),
        "category": (data.get("category") or "").strip(),
        "images": data.get("images") if isinstance(data.get("images"), list) else [],
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }

    res = mongo.db.products.insert_one(product)
    product["_id"] = str(res.inserted_id)
    return {"product": product}, 201


@admin_bp.put("/products/<product_id>")
@jwt_required()
def update_product(product_id):
    _, err = _require_admin()
    if err:
        return err

    data = request.json or {}
    patch = {"updated_at": datetime.utcnow()}
    for k in ["name", "description", "category"]:
        if k in data:
            patch[k] = (data.get(k) or "").strip()
    for k in ["price", "stock"]:
        if k in data:
            try:
                patch[k] = float(data.get(k)) if k == "price" else int(data.get(k))
            except Exception:
                return {"message": f"Invalid {k}"}, 400
    if "images" in data:
        patch["images"] = data.get("images") if isinstance(data.get("images"), list) else []

    try:
        oid = ObjectId(product_id)
    except Exception:
        return {"message": "Invalid product id"}, 400

    mongo.db.products.update_one({"_id": oid}, {"$set": patch})
    product = mongo.db.products.find_one({"_id": oid})
    if not product:
        return {"message": "Product not found"}, 404
    return {"product": _product_to_json(product)}


@admin_bp.delete("/products/<product_id>")
@jwt_required()
def delete_product(product_id):
    _, err = _require_admin()
    if err:
        return err
    try:
        oid = ObjectId(product_id)
    except Exception:
        return {"message": "Invalid product id"}, 400
    res = mongo.db.products.delete_one({"_id": oid})
    if res.deleted_count == 0:
        return {"message": "Product not found"}, 404
    return {"message": "Product deleted"}


@admin_bp.get("/users")
@jwt_required()
def list_users():
    _, err = _require_admin()
    if err:
        return err

    query = (request.args.get("query") or "").strip()
    limit = min(max(int(request.args.get("limit") or 50), 1), 200)
    skip = max(int(request.args.get("skip") or 0), 0)

    mongo_query = {}
    if query:
        mongo_query = {
            "$or": [
                {"name": {"$regex": query, "$options": "i"}},
                {"email": {"$regex": query, "$options": "i"}},
                {"role": {"$regex": query, "$options": "i"}},
            ]
        }

    users = list(
        mongo.db.users.find(mongo_query).sort("created_at", -1).skip(skip).limit(limit)
    )
    return {"users": [_user_to_json(u) for u in users]}


@admin_bp.post("/users")
@jwt_required()
def create_user():
    _, err = _require_admin()
    if err:
        return err

    data = request.json or {}
    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip().lower()
    password = data.get("password") or ""
    role = (data.get("role") or "user").strip()

    if not name or not email or not password:
        return {"message": "Name, email, and password are required"}, 400
    if role not in ["user", "admin"]:
        return {"message": "Invalid role"}, 400
    if mongo.db.users.find_one({"email": email}):
        return {"message": "User already exists"}, 400

    user = {
        "name": name,
        "email": email,
        "password": generate_password_hash(password),
        "role": role,
        "created_at": datetime.utcnow(),
    }
    res = mongo.db.users.insert_one(user)
    user["_id"] = str(res.inserted_id)
    return {"user": _user_to_json(user)}, 201


@admin_bp.put("/users/<user_id>")
@jwt_required()
def update_user(user_id):
    _, err = _require_admin()
    if err:
        return err

    data = request.json or {}
    patch = {}
    if "name" in data:
        patch["name"] = (data.get("name") or "").strip()
    if "email" in data:
        patch["email"] = (data.get("email") or "").strip().lower()
    if "role" in data:
        role = (data.get("role") or "").strip()
        if role not in ["user", "admin"]:
            return {"message": "Invalid role"}, 400
        patch["role"] = role

    try:
        oid = ObjectId(user_id)
    except Exception:
        return {"message": "Invalid user id"}, 400

    if "email" in patch:
        existing = mongo.db.users.find_one({"email": patch["email"], "_id": {"$ne": oid}})
        if existing:
            return {"message": "Email already in use"}, 400

    mongo.db.users.update_one({"_id": oid}, {"$set": patch})
    user = mongo.db.users.find_one({"_id": oid})
    if not user:
        return {"message": "User not found"}, 404
    return {"user": _user_to_json(user)}


@admin_bp.delete("/users/<user_id>")
@jwt_required()
def delete_user(user_id):
    _, err = _require_admin()
    if err:
        return err
    try:
        oid = ObjectId(user_id)
    except Exception:
        return {"message": "Invalid user id"}, 400
    res = mongo.db.users.delete_one({"_id": oid})
    if res.deleted_count == 0:
        return {"message": "User not found"}, 404
    return {"message": "User deleted"}