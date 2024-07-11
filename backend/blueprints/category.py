# backend/blueprints/category.py
from flask import Blueprint, request
from flask_restx import Namespace, Resource, fields
from backend.models import Category, save, delete  # Assuming similar functions for Category
from flask_jwt_extended import jwt_required

category_ns = Namespace('categories', description='Category operations')

category_model = category_ns.model(
    "Category",
    {
        "id": fields.Integer(readOnly=True, description='The unique identifier of a category'),
        "name": fields.String(required=True, description='Category name'),
    }
)

@category_ns.route('/')
class CategoryList(Resource):
    @category_ns.doc('list_categories')
    @category_ns.marshal_list_with(category_model)
    def get(self):
        """List all categories"""
        return Category.query.all()

    @jwt_required()
    @category_ns.expect(category_model)
    @category_ns.marshal_with(category_model, code=201)
    def post(self):
        """Create a new category"""
        data = request.json
        category = Category(name=data['name'])
        save(category)
        return category, 201

@category_ns.route('/<int:id>')
@category_ns.response(404, 'Category not found')
class CategoryResource(Resource):
    @category_ns.doc('get_category')
    @category_ns.marshal_with(category_model)
    def get(self, id):
        """Fetch a category given its identifier"""
        return Category.query.get_or_404(id)

    @jwt_required()
    @category_ns.expect(category_model)
    @category_ns.marshal_with(category_model)
    def put(self, id):
        """Update a category given its identifier"""
        category = Category.query.get_or_404(id)
        data = request.json
        category.name = data.get('name', category.name)
        save(category)
        return category

    @jwt_required()
    @category_ns.doc('delete_category')
    @category_ns.response(204, 'Category deleted')
    def delete(self, id):
        """Delete a category given its identifier"""
        category = Category.query.get_or_404(id)
        delete(category)
        return '', 204