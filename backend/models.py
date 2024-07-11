from .extensions import db
from datetime import datetime, timezone

"""
class Product:
	id: int pk
	title: str
	description: str (text)
	date_added: int
"""
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100))  # New field for image filename
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    
    # to return a string representation of the object
    def __repr__(self):
        return f"<Product {self.title} >"
    
    def update(self, title, price, description, image=None):
        self.title = title
        self.price = price
        self.description = description
        if image:
            self.image = image
        db.session.commit()
        
# Step 1: Define the Category Model
class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    products = db.relationship('Product', backref='category', lazy=True)
    
    def __repr__(self):
        return f"<Category {self.name}>"
        
    
    def update(self, name):
        self.name = name 
        db.session.commit()
    
"""
class User:
	id: int pk
	username: str
	email: str
	password: str
"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f"<User {self.username}>"
    

"""For saving, deleting, updating"""
def save(var):
	""" This saves to the database, so we add and commit"""
	db.session.add(var)
	db.session.commit()
	
def delete(var):
	""" Performs delete operations"""
	db.session.delete(var)
	db.session.commit()
