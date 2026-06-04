from flask import Blueprint, request
from app.services.product_service import get_home_data, search_products, get_details

product_bp = Blueprint("product", __name__)

@product_bp.get("/home-data")
def home():
    """Return a limited set of products for the home/landing page."""
    return get_home_data()

@product_bp.get("/search")
def search():
    """Search products by name (case-insensitive). Query param: q."""
    return search_products(request.args.get("q"))

@product_bp.get("/details/<id>")
def details(id):
    """Return a single product by id. Responds with 404 if not found."""
    return get_details(id)