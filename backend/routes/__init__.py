from .users import user_bp
from .orders import order_bp
from .categories import category_bp
from .products import product_bp
from .order_items import order_item_bp
from .payments import payment_bp
from .reviews import review_bp
from .carts import cart_bp

def register_routes(app):
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(order_bp, url_prefix='/api/orders')
    app.register_blueprint(category_bp, url_prefix='/api/categories')
    app.register_blueprint(product_bp, url_prefix='/api/products')
    app.register_blueprint(order_item_bp, url_prefix='/api/order_items')
    app.register_blueprint(payment_bp, url_prefix='/api/payments')
    app.register_blueprint(review_bp, url_prefix='/api/reviews')
    app.register_blueprint(cart_bp, url_prefix='/api/carts')
