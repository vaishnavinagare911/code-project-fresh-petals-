from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.order_service import place_order, get_my_orders

order_bp = Blueprint("order", __name__)

@order_bp.post("/payment")
@jwt_required()
def payment():
    """
    Convert the current user's cart into an order, then clear the cart.
    Returns an error if the cart is empty. Requires JWT.
    """
    user_id = get_jwt_identity()
    return place_order(user_id)

@order_bp.get("/my-orders")
@jwt_required()
def my_orders():
    """Return all orders for the current user, most recent first. Requires JWT."""
    user_id = get_jwt_identity()
    return get_my_orders(user_id)