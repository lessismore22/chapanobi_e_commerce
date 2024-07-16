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

@product_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = Product.query.filter_by(id=product_id).first()
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    if 'name' in data:
        product.name = data['name']
    if 'description' in data:
        product.description = data['description']
    if 'price' in data:
        product.price = data['price']
    if 'category_id' in data:
        product.category_id = data['category_id']
    db.session.commit()
    return jsonify({'message': 'Product updated successfully'})

@product_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
	product = Product.query.filter_by(id=product_id).first()
	if not product:
		return jsonify({'message': 'Product not found'}), 404
	db.session.delete(product)
	db.session.commit()
	return jsonify({'message': 'Product deleted successfully'})