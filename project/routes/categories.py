from flask import Blueprint, request, jsonify
from models import db, Categories
from flask_login import current_user, login_required

category_bp = Blueprint('categories', __name__)

@category_bp.route('/', methods=['POST'])
@login_required
def create_Categories():
    data = request.get_json()
    new_category = Categories(name=data['name'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'message': 'Categories created successfully'})

@category_bp.route('/', methods=['GET'])
def get_categories():
    categories = Categories.query.all()
    return jsonify([{'id': Categories.id, 'name': Categories.name} for Categories in categories])

@category_bp.route('/<int:Categories_id>', methods=['PUT'])
def update_categories():
    data = request.get_json()
    Categories = Categories.query.filter_by(id=Categories.id, user_id=current_user.id).first()
    if not Categories:
        return jsonify({'message': 'Categories not found'}), 404
    if 'name' in data:
        Categories.name = data['name']
    if 'description' in data:
        Categories.description = data['description']
    db.session.commit
    return jsonify({'message': 'Categories updated successfully'})

@category_bp.route('/<int:Categories_id>', methods=['DELETE'])
def delete_Categories():
    Categories = Categories.query.filter_by(id=Categories.id, user_id=current_user.id).first()
    if not Categories:
        return jsonify({'message': 'Categories not found'}), 404
    Categories.query.filter_by(id=Categories.id).delete()
    db.session.delete(Categories)
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully'})
    
    
    