from functools import wraps
from flask import request, jsonify
import jwt

SECRET_KEY = "mysecret"  # use your own

def auth_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"message": "Token missing"}), 401

        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            request.user_id = decoded["user_id"]
        except Exception as e:
            return jsonify({"message": "Invalid token"}), 401

        return f(*args, **kwargs)
    return wrapper
