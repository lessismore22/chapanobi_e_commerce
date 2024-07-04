# backend/blueprints/user.py
from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from backend.models import User, save, delete
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token

user_ns = Namespace("users", description="Users related operations")

signup_model = user_ns.model(
    "SignUp",
    {
        "id": fields.Integer(),
        "username": fields.String(),
        "email": fields.String(),
        "password": fields.String(),
        "first_name": fields.String(),
        "last_name": fields.String(),
        "address": fields.String(),
        "phone": fields.String(),
        "created_at": fields.DateTime(),
        "updated_at": fields.DateTime()
    },
)
login_model = user_ns.model(
    "Login", {"username": fields.String(), "password": fields.String()}
)


@user_ns.route("/users/signup")
class SignUp(Resource):
    # @user_ns.marshal_with(signup_model)
    @user_ns.expect(signup_model)
    @user_ns.doc("signup_user")
    def post(self):
        """Creates a new user."""
        data = request.get_json()
        username = data.get("username")
        email = data.get("email")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        address = data.get("address")
        phone = data.get("phone")
        # filtering or getting out only one user and email
        db_user = User.query.filter_by(username=username).first()
        db_mail = User.query.filter_by(email=email).first()

        if db_user is not None:
            return jsonify({"message": f"User {username} already exists"})
        elif db_mail is not None:
            return jsonify({"message": "This email is already in use"})

        new_user = User(
            username=username,
            email=email,
            password=generate_password_hash(data.get("password")),
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone=phone,
        )
        save(new_user)
        return jsonify({"message": "User created successfully"})


@user_ns.route("/user/login")
class LoginResource(Resource):
    @user_ns.expect(login_model)
    @user_ns.doc("login_user")
    def post(self):
        """Logs in a user"""
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        db_user = User.query.filter_by(username=username).first()

        if db_user and check_password_hash(db_user.password, password):
            access_token = create_access_token(identity=db_user.username)
            refresh_token = create_refresh_token(identity=db_user.username)
            return jsonify(
                {"access_token": access_token, "refresh_token": refresh_token}
            )
