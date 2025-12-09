import jwt
from flask import request, jsonify
from functools import wraps
from config import Config

def auth_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"error": "Missing token"}), 401

        try:
            token = token.replace("Bearer ", "")
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
            request.user_id = data["user_id"]

        except Exception as e:
            return jsonify({"error": "Invalid token", "detail": str(e)}), 401

        return f(*args, **kwargs)

    return wrapper
