from flask import Blueprint, request, jsonify
from models import db, Product

product_bp = Blueprint('products', __name__)

@product_bp.route('/', methods=['POST'])
def create_product():
# @login_required
    data = request.get_json()
    new_product = Product(name=data['name'], description=data['description'], price=data['price'], category_id=data['category_id'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully'})

@product_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'category_id': product.category_id
    } for product in products])
