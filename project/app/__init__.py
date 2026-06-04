from flask import Flask
from .config import Config
from .extensions import mongo, jwt
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)
    mongo.init_app(app)
    jwt.init_app(app)

    from .routes.auth_routes import auth_bp
    from .routes.product_routes import product_bp
    from .routes.cart_routes import cart_bp
    from .routes.order_routes import order_bp
    from .routes.admin_routes import admin_bp
    from .routes.wishlist_routes import wishlist_bp

    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(product_bp, url_prefix="/api")
    app.register_blueprint(cart_bp, url_prefix="/api")
    app.register_blueprint(order_bp, url_prefix="/api")
    app.register_blueprint(wishlist_bp, url_prefix="/api")
    app.register_blueprint(admin_bp, url_prefix="/api/admin")

    return app