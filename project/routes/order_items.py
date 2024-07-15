from flask import Blueprint, request, jsonify
from models import db, OrderItem

order_item_bp = Blueprint('order_items', __name__)

@order_item_bp.route('/', methods=['POST'])
def create_order_item():
    data = request.get_json()
    new_order_item = OrderItem(order_id=data['order_id'], product_id=data['product_id'], quantity=data['quantity'], price=data['price'])
    db.session.add(new_order_item)
    db.session.commit()
    return jsonify({'message': 'Order item created successfully'})

@order_item_bp.route('/', methods=['GET'])
def get_order_items():
    order_items = OrderItem.query.all()
    return jsonify([{
        'id': order_item.id,
        'order_id': order_item.order_id,
        'product_id': order_item.product_id,
        'quantity': order_item.quantity,
        'price' : order_item.price
    } for order_item in order_items])
