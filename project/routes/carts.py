from flask import Blueprint, request, jsonify
from models import db, Cart
from flask_login import current_user, login_required

cart_bp = Blueprint('carts', __name__)

@cart_bp.route('/', methods=['POST'])
@login_required
def add_to_cart():
    data = request.get_json()
    cart_item = Cart.query.filter_by(user_id=current_user.id, product_id=data['product_id']).first()
    if cart_item:
        cart_item.quantity += data['quantity']
    else:
        cart_item = Cart(user_id=current_user.id, product_id=data['product_id'], quantity=data['quantity'])
        db.session.add(cart_item)
    db.session.commit()
    return jsonify({'message': 'Item added to cart'})

@cart_bp.route('/', methods=['GET'])
@login_required
def get_cart():
    cart_items = Cart.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        'id': cart_item.id,
        'product_id': cart_item.product_id,
        'quantity': cart_item.quantity
    } for cart_item in cart_items])
