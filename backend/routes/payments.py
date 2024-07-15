from flask import Blueprint, request, jsonify
from models import db, Payment

payment_bp = Blueprint('payments', __name__)

@payment_bp.route('/', methods=['POST'])
def create_payment():
    data = request.get_json()
    new_payment = Payment(order_id=data['order_id'], amount=data['amount'], method=data['method'], status='Pending')
    db.session.add(new_payment)
    db.session.commit()
    return jsonify({'message': 'Payment created successfully'})

@payment_bp.route('/', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    return jsonify([{
        'id': payment.id,
        'order_id': payment.order_id,
        'amount': payment.amount,
        'method': payment.method,
        'status': payment.status
    } for payment in payments])
