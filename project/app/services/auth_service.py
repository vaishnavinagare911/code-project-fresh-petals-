from app.extensions import mongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from datetime import datetime

def register_user(data):
    """
    Create a new user from data (name, email, password).
    Returns (message, 201) on success, or (message, 400) if email already exists.
    """
    if mongo.db.users.find_one({"email": data["email"]}):
        return {"message": "User already exists"}, 400

    user = {
        "name": data["name"],
        "email": data["email"],
        "password": generate_password_hash(data["password"]),
        "role": "user",
        "created_at": datetime.utcnow()
    }

    mongo.db.users.insert_one(user)
    return {"message": "User registered successfully"}, 201

def login_user(data):
    """
    Authenticate with email and password. Returns {"token": <jwt>} on success,
    or (message, 401) if the user is not found or the password is wrong.
    """
    user = mongo.db.users.find_one({"email": data["email"]})
    if not user or not check_password_hash(user["password"], data["password"]):
        return {"message": "Invalid credentials"}, 401

    token = create_access_token(identity=str(user["_id"]))
    return {"token": token}

def get_profile(user_id):
    """
    Return the profile for the given user_id (name, email, role).
    Returns (message, 404) if the user is not found.
    """
    from bson import ObjectId
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        return {"message": "User not found"}, 404
    return {
        "name": user.get("name", ""),
        "email": user.get("email", ""),
        "role": user.get("role", "user")
    }