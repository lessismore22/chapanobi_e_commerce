# E-Commerce WebApp API

This project is an API for an E-Commerce WebApp built using Flask. It provides a robust set of features for managing products, users, orders, and shopping carts, making it easy to integrate with any front-end e-commerce platform.

## Features

- **User Authentication and Authorization**: Secure user registration, login, and access control.
- **Product Management**: Add, update, delete, and retrieve products.
- **Shopping Cart**: Add, update, and remove items from the cart.
- **Order Management**: Place orders and track order status.
- **Payment Integration**: Process payments (mock integration provided).

## Getting Started

### Prerequisites

- Python 3.8+
- Flask
- A virtual environment (recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ecommerce-webapp-api.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ecommerce-webapp-api
   ```
3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Set the Flask application and environment variables:
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```
2. Run the Flask application:
   ```bash
   flask run
   ```

## API Endpoints

| Method | Endpoint              | Description                       |
|--------|-----------------------|-----------------------------------|
| POST   | `/api/users/register` | Register a new user.              |
| POST   | `/api/users/login`    | Login a user.                     |
| GET    | `/api/products`       | Retrieve all products.            |
| POST   | `/api/products`       | Add a new product.                |
| PUT    | `/api/cart`           | Update shopping cart.             |
| GET    | `/api/cart`           | Retrieve shopping cart.           |
| POST   | `/api/orders`         | Place a new order.                |
| GET    | `/api/orders`         | Retrieve all orders for a user.   |

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```