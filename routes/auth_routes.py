from flask import Blueprint, request, jsonify
from database.models import User, db
from passlib.hash import pbkdf2_sha256
import jwt
import datetime
from config import Config

auth_bp = Blueprint("auth", __name__)

# -------- REGISTER --------
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "User already exists"}), 400

    hashed_pw = pbkdf2_sha256.hash(password)

    user = User(username=username, password=hashed_pw)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201


# -------- LOGIN --------
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not pbkdf2_sha256.verify(password, user.password):
        return jsonify({"error": "Invalid username or password"}), 401

    token = jwt.encode({
        "user_id": user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=3)
    }, Config.SECRET_KEY, algorithm="HS256")

    return jsonify({"token": token})
