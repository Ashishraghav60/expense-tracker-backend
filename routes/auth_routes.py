from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from database.models import User, db
import jwt
import datetime

auth_bp = Blueprint("auth", __name__)

# IMPORTANT — use the SAME SECRET KEY you used in auth_middleware
SECRET_KEY = "your_secret_key_here"  


# ----------------------------- REGISTER ---------------------------------- #
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({"message": "All fields are required"}), 400

    # Check user already exists
    existing = User.query.filter_by(email=email).first()
    if existing:
        return jsonify({"message": "Email already registered"}), 400

    # Hash password securely
    hashed_password = generate_password_hash(password)

    # Save user
    user = User(name=name, email=email, password=hashed_password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 200



# ----------------------------- LOGIN ------------------------------------- #
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    # Find user
    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"message": "Invalid email or password"}), 401

    # Check password hash
    if not check_password_hash(user.password, password):
        return jsonify({"message": "Invalid email or password"}), 401

    # Create JWT token valid for 24 hours
    token = jwt.encode(
        {
            "user_id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        },
        SECRET_KEY,
        algorithm="HS256",
    )

    return jsonify({"token": token}), 200
