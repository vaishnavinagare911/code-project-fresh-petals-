from app.extensions import mongo
from bson import ObjectId
import qrcode
import io
import base64


# ADD ITEM TO CART
def add_to_cart(user_id, data):

    mongo.db.cart.update_one(
        {"user_id": user_id},
        {
            "$set": {"user_id": user_id},
            "$push": {
                "items": {
                    "product_id": data["product_id"],
                    "quantity": data["quantity"]
                }
            }
        },
        upsert=True
    )

    return {"message": "Added to cart"}


# GET CART
def get_cart(user_id):

    cart = mongo.db.cart.find_one({"user_id": user_id})

    if not cart or not cart.get("items"):
        return {"items": [], "total": 0}

    items = []
    total = 0

    for item in cart["items"]:

        product = mongo.db.products.find_one(
            {"_id": ObjectId(item["product_id"])}
        )

        if product:

            qty = item.get("quantity", 1)
            price = float(product.get("price", 0))

            subtotal = price * qty
            total += subtotal

            items.append({
                "product_id": str(product["_id"]),
                "name": product.get("name"),
                "price": price,
                "quantity": qty,
                "subtotal": round(subtotal, 2),
                "image": product.get("images", [""])[0],
                "net_content": product.get("net_content", "")
            })

    return {
        "items": items,
        "total": round(total, 2)
    }


# UPDATE CART ITEM
def update_cart_item(user_id, product_id, quantity):

    mongo.db.cart.update_one(
        {
            "user_id": user_id,
            "items.product_id": product_id
        },
        {
            "$set": {
                "items.$.quantity": quantity
            }
        }
    )

    return {"message": "Cart item updated"}


# REMOVE ITEM
def remove_cart_item(user_id, product_id):

    mongo.db.cart.update_one(
        {"user_id": user_id},
        {
            "$pull": {
                "items": {"product_id": product_id}
            }
        }
    )

    return {"message": "Item removed"}


# CLEAR CART
def clear_cart(user_id):

    mongo.db.cart.update_one(
        {"user_id": user_id},
        {
            "$set": {"items": []}
        }
    )

    return {"message": "Cart cleared"}


# GENERATE PAYMENT QR
def generate_payment_qr(user_id):

    cart = mongo.db.cart.find_one({"user_id": user_id})

    if not cart or not cart.get("items"):
        return {"message": "Cart empty"}, 400

    total = 0

    for item in cart["items"]:

        product = mongo.db.products.find_one(
            {"_id": ObjectId(item["product_id"])}
        )

        if product:

            qty = item.get("quantity", 1)
            price = float(product.get("price", 0))

            total += price * qty

    total = round(total, 2)

    upi_id = "vaishnavinagare911@oksbi"
    payee_name = "Vaishnavi nagare".replace(" ", "%20")

    note = "Freshpetals Order Payment"

    upi_link = f"upi://pay?pa={upi_id}&pn={payee_name}&am={total}&cu=INR&tn={note}"

    qr = qrcode.make(upi_link)

    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")

    qr_base64 = base64.b64encode(buffer.getvalue()).decode()

    return {
        "total_amount": total,
        "upi_link": upi_link,
        "qr_code": qr_base64
    }