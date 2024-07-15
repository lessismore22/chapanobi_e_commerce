from flask import Flask
from config import Config
from models import db, login_manager
from routes import register_routes
from flask_migrate import Migrate

migrate = Migrate()
app = Flask(__name__)
app.config.from_object(Config)


db.init_app(app)
login_manager.init_app(app)
migrate.init_app(app, db)
register_routes(app)

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
