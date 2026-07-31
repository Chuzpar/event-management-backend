from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from .models import User
from . import db

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"message": "Email already exists"}), 400

    user = User(
        full_name=data["full_name"],
        email=data["email"]
    )

    user.set_password(data["password"])

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

@auth.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    user = User.query.filter_by(email=data["email"]).first()

    if not user or not user.check_password(data["password"]):
        return jsonify({"message": "Invalid credentials"}), 401

    token = create_access_token(identity=str(user.id))
    return jsonify({
        "access_token": token,
        "user": {
            "id": user.id,
            "name": user.full_name,
            "email": user.email
        }
    })