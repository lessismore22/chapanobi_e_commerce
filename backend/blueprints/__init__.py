# backend/blueprints/__init__.py
from .hello import hello_ns
from .auth import user_ns
from .product import product_ns

namespaces = [hello_ns, product_ns, user_ns]

