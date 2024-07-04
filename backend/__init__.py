from flask import Flask
from .config import DevConfig
from .extensions import db, migrate
from .blueprints import namespaces
from flask_restx import Api
from flask_jwt_extended import JWTManager

def create_app(config_class=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    JWTManager(app)
    
    
    api = Api(app, title='Chapanobi Ecommerce API', version='1.0', description='This is a documentation for the RESTapi we have created for our E-commerce web-app.', doc='/docs')
    
     # Register each namespace
    for namespace in namespaces:
        api.add_namespace(namespace, path='/api')
    
    return app