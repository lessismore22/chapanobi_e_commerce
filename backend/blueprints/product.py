# backend/blueprints/product.py
from flask import Blueprint, request
from flask_restx import Namespace, Resource, fields
from backend.models import Product, save, delete
from flask_jwt_extended import jwt_required

product_ns = Namespace('products', description='Making requests for the products')

product_model = product_ns.model(
    "Product",
    {
        "id": fields.Integer(),
        "title": fields.String(),
        "price": fields.Float(),
        "description": fields.String()
    }
)

@product_ns.route('/products')
class ProductsResource(Resource):
    @product_ns.marshal_list_with(product_model)
    @product_ns.doc('get_products')
    def get(self):
        """Gets all products"""
        all_products = Product.query.all()
        return all_products
    
    @product_ns.marshal_with(product_model)
    @product_ns.expect(product_model)
    @product_ns.doc('create_products')
    @jwt_required()
    def post(self):
        """Creates a new product"""
        data = request.get_json()
        new_product = Product(
            title=data.get('title'),
            price=data.get('price'),
            description=data.get('description')
        )
        save(new_product)
        return new_product, 201
    

# A class for updating and deleting
@product_ns.route('/product/<int:id>')
class ProductResource(Resource):
    @product_ns.marshal_with(product_model)
    @product_ns.doc('get_product')
    def get(self, id):
        """Get a single product"""
        single_product = Product.query.get_or_404(id)
        return single_product
    
    @product_ns.marshal_with(product_model)
    @product_ns.expect(product_model)
    @product_ns.doc('update_product')
    @jwt_required()
    def put(self, id):
        """Update a product"""
        product_to_update = Product.query.get_or_404(id)
        data = request.get_json()
        
        product_to_update.update(data['title'], data['price'], data['description'])
        return product_to_update
        
    @product_ns.marshal_with(product_model)
    @product_ns.doc('delete_product')
    @jwt_required()
    def delete(self, id):
        """Deletes a product"""
        product_to_delete = Product.query.get_or_404(id)
        delete(product_to_delete)
        return product_to_delete

