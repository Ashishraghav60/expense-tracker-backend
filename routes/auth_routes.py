from flask import Blueprint, request, jsonify
from database.models import User, db
from passlib.hash import pbkdf2_sha256
import jwt, datetime
import config

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json

    if User.query.filter_by(username=data['username']).first():
        return jsonify({"message": "Username already exists"}), 400
        
    hashed_password = pbkdf2_sha256.hash(data['password'])
    user = User(username=data['username'], password=hashed_password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created successfully"})


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()

    if not user or not pbkdf2_sha256.verify(data['password'], user.password):
        return jsonify({"message": "Invalid username or password"}), 401

    token = jwt.encode({
        "user_id": user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    }, config.SECRET_KEY, algorithm="HS256")

    return jsonify({"token": token})
