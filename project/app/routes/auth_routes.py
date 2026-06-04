from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.auth_service import register_user, login_user, get_profile

auth_bp = Blueprint("auth", __name__)

@auth_bp.post("/register")
def register():
    """Accept JSON with name, email, password; create user and return success or error."""
    return register_user(request.json)

@auth_bp.post("/login")
def login():
    """Accept JSON with email and password; return a JWT or invalid-credentials error."""
    return login_user(request.json)

@auth_bp.get("/profile")
@jwt_required()
def profile():
    """
    Return the current user's profile (name, email, role). Requires a valid
    JWT in the Authorization header; the user id is taken from the token.
    """
    user_id = get_jwt_identity()
    return get_profile(user_id)