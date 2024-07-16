from flask import Blueprint, request, jsonify
from models import db, Categories
from flask_login import current_user, login_required

category_bp = Blueprint('categories', __name__)

@category_bp.route('/', methods=['POST'])
@login_required
def create_Categories():
    data = request.get_json()
    new_category = Categories(name=data['name'], description=data['description'], user_id=current_user.id)
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'message': 'Categories created successfully'})

@category_bp.route('/', methods=['GET'])
def get_categories():
    categories = Categories.query.all()
    return jsonify([{
        'id': Categories.id,
        'name': Categories.name,
        "description": Categories.description
        } for Categories in categories])

@category_bp.route('/<int:category_id>', methods=['PUT'])
def update_categories(category_id):
    data = request.get_json()
    categories = Categories.query.filter_by(id=category_id, user_id=current_user.id).first()
    if not categories:
        return jsonify({'message': 'Categories not found'}), 404
    if 'name' in data:
        categories.name = data['name']
    if 'description' in data:
        categories.description = data['description']
    db.session.commit
    return jsonify({'message': 'Categories updated successfully'})

@category_bp.route('/<int:category_id>', methods=['DELETE'])
def delete_Categories(category_id):
    category = Categories.query.filter_by(id=category_id, user_id=current_user.id).first()
    if not category:
        return jsonify({'message': 'Categories not found'}), 404
    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully'})
    
    
    