from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.wishlist_service import (
    get_wishlist,
    add_to_wishlist,
    remove_from_wishlist,
)


wishlist_bp = Blueprint("wishlist", __name__)


@wishlist_bp.get("/wishlist")
@jwt_required()
def list_wishlist():
    user_id = get_jwt_identity()
    return get_wishlist(user_id)


@wishlist_bp.post("/wishlist/<product_id>")
@jwt_required()
def add_item(product_id):
    user_id = get_jwt_identity()
    return add_to_wishlist(user_id, product_id)


@wishlist_bp.delete("/wishlist/<product_id>")
@jwt_required()
def remove_item(product_id):
    user_id = get_jwt_identity()
    return remove_from_wishlist(user_id, product_id)

