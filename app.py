# app.py

from flask import Flask
from flask_cors import CORS
from config import Config
from database.db import init_db

# Import blueprints
from routes.auth_routes import auth_bp
from routes.user_routes import user_bp  # Only if you have this file

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Enable CORS
    CORS(app)

    # Initialize database
    init_db(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    
    # Register only if file exists
    try:
        app.register_blueprint(user_bp, url_prefix="/user")
    except:
        pass

    @app.route("/")
    def home():
        return {"message": "Backend is running!"}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
