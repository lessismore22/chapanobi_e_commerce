from flask import Blueprint, request, jsonify
from models import db, Reviews
from flask_login import current_user, login_required

review_bp = Blueprint('reviews', __name__)

@review_bp.route('/', methods=['POST'])
@login_required
def create_review():
    data = request.get_json()
    new_review = Reviews(product_id=data['product_id'], user_id=current_user.id, rating=data['rating'], comment=data['comment'])
    db.session.add(new_review)
    db.session.commit()
    return jsonify({'message': 'Review created successfully'})

@review_bp.route('/', methods=['GET'])
def get_reviews():
    reviews = Reviews.query.all()
    return jsonify([{
        'id': review.id,
        'product_id': review.product_id,
        'user_id': review.user_id,
        'rating': review.rating,
        'comment': review.comment
    } for review in reviews])
