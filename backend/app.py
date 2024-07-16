from flask import Flask
from config import Config
from models import db, login_manager, User
from routes import register_routes
from flask_migrate import Migrate
from decouple import config

migrate = Migrate()
app = Flask(__name__)
app.config.from_object(Config)


db.init_app(app)
login_manager.init_app(app)
migrate.init_app(app, db)
register_routes(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

@app.route('/')
def hello():
    return "Welcome to Chapanobi Ecommerce"

if __name__ == '__main__':
    app.run(debug=True)
