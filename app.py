from flask import Flask
from flask_cors import CORS
from config import Config
from database.db import db
from routes.auth_routes import auth_bp
from routes.expense_routes import expense_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enable CORS
    CORS(app)

    # Initialize DB
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(expense_bp, url_prefix="/api")

    # Home route
    @app.route("/")
    def home():
        return {"message": "Expense Tracker Backend is running!"}

    return app


app = create_app()

# Run the app on Render / Local
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(host="0.0.0.0", port=5000)
