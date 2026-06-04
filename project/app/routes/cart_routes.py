from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.services.cart_service import (
    add_to_cart,
    get_cart,
    update_cart_item,
    remove_cart_item,
    clear_cart,
    generate_payment_qr
)

cart_bp = Blueprint("cart", __name__)


@cart_bp.get("/cart")
@jwt_required()
def view_cart():

    user_id = get_jwt_identity()
    return get_cart(user_id)


@cart_bp.post("/add-to-cart")
@jwt_required()
def add_item():

    user_id = get_jwt_identity()
    data = request.json

    return add_to_cart(user_id, data)


@cart_bp.put("/cart/update")
@jwt_required()
def update_item():

    user_id = get_jwt_identity()
    data = request.json

    product_id = data.get("product_id")
    quantity = data.get("quantity")

    return update_cart_item(user_id, product_id, quantity)


@cart_bp.delete("/cart/remove/<product_id>")
@jwt_required()
def remove_item(product_id):

    user_id = get_jwt_identity()

    return remove_cart_item(user_id, product_id)


@cart_bp.delete("/cart/clear")
@jwt_required()
def clear():

    user_id = get_jwt_identity()

    return clear_cart(user_id)


@cart_bp.get("/cart/get_qr")
@jwt_required()
def get_qr():

    user_id = get_jwt_identity()

    return generate_payment_qr(user_id)