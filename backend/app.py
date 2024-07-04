# backend/app.py
from backend import create_app
from .extensions import db
from .models import Product

app = create_app()

# exporting our databse to a terminal so we can interact with it
@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Product": Product}


if __name__ == "__main__":
    app.run(debug=True)

