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
    
    # to return a string representation of the object
    def __repr__(self):
        return f"<Product {self.title} >"
    
    def update(self, title, description):
        self.title = title
        self.description = description   
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
