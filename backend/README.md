# E-commerce site

Creating a virtual environment
- pip install --upgrade pipenv
- pipenv install -> ``` To activate the environment ```
- pipenv install flask flask_restx flask_sqlalchemy flask_jwt_extended ``` flask_restx is for creating the rest api for frontend, flask_sqlalchemy will help us write models for our database, and flask_jwt_extended will help us create jwt's and also help in our backend. ```

- pipenv install python_decouple -> ``` Used to locate the secret key within an env file ```

###### Using python secrets module to generate a secret key in hex
```
python
import secrets
secrets.token_hex(12)
```

##### Database
- Using sqlite and sqlalchemy for models
- pipenv install flask_sqlalchemy
- Create a models.py file to define our models
- Create a database.py file to create our database
- Create a schema.sql file to create our database schema
- Create a seed.py file to seed our database with data
- Create a config.py file to configure our database
- Create a .env file to store our secret key and database url
- Create a app.py file to create our flask app and routes
- Create a routes.py file to define our routes
- Create a auth.py file to handle authentication
- Create a users.py file to handle user related operations
- Create a products.py file to handle product related operations
- Create a orders.py file to handle order related operations
- Create a payments.py file to handle payment related operations
- Create a utils.py file to handle utility functions
- Create a tests.py file to write unit tests for our application
- Create a requirements.txt file to store our dependencies
- Create a Dockerfile to containerize our application
- Create a docker-compose.yml file to define our services
- Create a .gitignore file to ignore files that should not be tracked by git
- Create a README.md file to provide information about our application
- Create a LICENSE file to provide licensing information about our application
- Create a .env.example file to provide an example of our .env file
- Create a config.example.py file to provide an example of our config.py file
- Create a schema.example.sql file to provide an example of our schema.sql files
- Create a seed.example.py file to provide an example of our seed.py file
- Create a tests.example.py file to provide an example of our tests.py file

- Migrate our data using the flask_migrate dependency.
--- 
pipenv install flask_migrate

Then create a migrate repository, you can run ```flask db``` to see all the commands to run on the migrate

```flask db init``` to create repository for database
```flask db migrate -m "Added user table"``` to migrate database
```flask db upgrade``` to create all table


---
###### When creating methods for put and post, add this decorator ```@api.expect(product_model)``` so that there will be interaction in swaggerui


##### For creating security in our app, ```from werkzeug.security import generate_password_hash, check_password_hash```, so we can hash our passwords




# from flask import Flask, request, jsonify
# from flask_restx import Api, Resource, fields
# from flask_migrate import Migrate


# # importing our config
# from config import DevConfig
# from models import Product, db, save, delete, User

# # we use werkzeug to add security, hash passwords
# from werkzeug.security import generate_password_hash, check_password_hash

# # create the flask instance
# app = Flask(__name__)

# # we are using from_object since it's a class
# app.config.from_object(DevConfig)
# # register the databse to connect with our app
# db.init_app(app)

# # instantiate our migrate class
# migrate = Migrate(app, db)

# api = Api(app, doc="/docs")

# # serializing our product data
# product_model = api.model(
#     "Product",
#     {
#         "id": fields.Integer(),
#         "title": fields.String(),
#         "description": fields.String()
#     }
# )

# # serializing our signup data
# signup_model = api.model(
#     "SignUp",
#     {
#         "id": fields.Integer(),
#         "username": fields.String(),
#         "email": fields.String(),
#         "password": fields.String()
#     }
# )


# @api.route("/hello")
# # this class will contain all the routes we will carry out in this route
# class HelloResource(Resource):
#     def get(self):
#         return {"message": "Hello world"}
    
# # creating routes for logging and signing up a user
# @api.route('/user/signup')
# class SignUp(Resource):
#     @api.marshal_with(signup_model)
#     @api.expect(signup_model)
#     def post(self):
#         data = request.get_json()
#         username = data.get('username')
#         email = data.get('email')
#         # filtering or getting out only one user
#         db_user = User.query.filter_by(username=username).first()
#         db_mail = User.query.filter_by(email=email).first()
        
#         if db_user is not None:
#             return jsonify({"message": f"User {username} already exists"})
#         elif db_mail is not None:
#             return jsonify({"message": "This email is already in use"})

#         new_user = User(
# 			username = username,
# 			email = email,
# 			password = generate_password_hash(data.get('password')),
# 		)
#         save(new_user)
#         return new_user, 201


# @api.route('/user/login')
# class LogIn(Resource):
#     def post(self):
#         """Log in a new user"""
#         pass


    

# # creating route for our product app
# @api.route('/products')
# class ProductsResource(Resource):
#     # using our serialized object to decorate
#     # the method so it gives response in json
#     @api.marshal_list_with(product_model)
#     def get(self):
#         """Get all products from database"""
        
#         all_products = Product.query.all()
#         return all_products
    
#     @api.marshal_with(product_model)
#     @api.expect(product_model)
#     def post(self):
#         """For creating a new product"""
#         data = request.get_json()
#         new_product = Product(
# 			title = data.get('title'),
# 			description = data.get('description')
# 		)
#         save(new_product)
#         return new_product, 201
    

# # A class for updating and deleting
# @api.route('/product/<int:id>')
# class ProductResource(Resource):
#     @api.marshal_with(product_model)
#     def get(self, id):
#         """Get a single product"""
#         single_product = Product.query.get_or_404(id)
#         return single_product
    
#     @api.marshal_with(product_model)
#     @api.expect(product_model)
#     def put(self, id):
#         """Update a product"""
#         product_to_update = Product.query.get_or_404(id)
#         data = request.get_json()
        
#         product_to_update.update(data['title'], data['description'])
#         return product_to_update
        
#     @api.marshal_with(product_model)
#     def delete(self, id):
#         """Deletes a product"""
#         product_to_delete = Product.query.get_or_404(id)
#         delete(product_to_delete)
#         return product_to_delete


# # exporting our databse to a terminal so we can interact with it
# @app.shell_context_processor
# def make_shell_context():
#     return {"db": db, "Product": Product}


# if __name__ == "__main__":
#     app.run()
