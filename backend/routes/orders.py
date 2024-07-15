from flask import Blueprint, request, jsonify
from models import db, Order, OrderItem
from flask_login import current_user, login_required

order_bp = Blueprint('orders', __name__)

@order_bp.route('/', methods=['POST'])
@login_required
def create_order():
    data = request.get_json()
    new_order = Order(user_id=current_user.id, quantity=data['quantity'], description=data['description'], total_amount=data['total_amount'], status='Pending')
    db.session.add(new_order) 
    db.session.commit()
    for item in data['items']:
        order_item = OrderItem(order_id=new_order.id, product_id=item['product_id'], quantity=item['quantity'])
        db.session.add(order_item)
    db.session.commit()
    return jsonify({'message': 'Order created successfully'})

@order_bp.route('/<int:order_id>', methods=['GET'])
@login_required
def get_order(order_id):
    order = Order.query.filter_by(id=order_id, user_id=current_user.id).first()
    if not order:
        return jsonify({'message': 'Order not found'}), 404
    order_items = OrderItem.query.filter_by(order_id=order.id).all()
    return jsonify({
        'id': order.id,
        'user_id': order.user_id,
        'total_price': order.total_price,
        'status': order.status,
        'items': [{'product_id': item.product_id, 'quantity': item.quantity} for item in order_items]
    })


@order_bp.route('/<int:order_id>', methods=['POST'])
@login_required
def update_order(order_id):
    data = request.get_json()
    order = Order.query.filter_by(id=order_id, user_id=current_user.id).first()
    if not order:
        return jsonify({'message': 'Order not found'}), 404
    if 'total_price' in data:
        order.total_price = data['total_price']
    if 'status' in data:
        order.status = data['status']
    db.session.commit()
    return jsonify({'message': 'Order updated successfully'})
    

@order_bp.route('/<int:order_id>', methods=['DELETE'])
@login_required
def delete_order(order_id):
     order = Order.query.filter_by(id=order_id, user_id=current_user.id).first()
     if not order:
        return jsonify({'message': 'Order not found'}), 404
     OrderItem.query.filter_by(order_id=order.id).delete()
     db.session.delete(order)
     db.session.commit()
     return jsonify({'message': 'Order deleted successfully'})