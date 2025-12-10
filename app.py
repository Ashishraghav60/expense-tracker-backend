from flask import Flask
from flask_cors import CORS
from config import Config
from database.db import db
from routes.auth_routes import auth_bp
from routes.expense_routes import expense_bp

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

db.init_app(app)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(expense_bp, url_prefix="/api")

@app.route("/")
def home():
    return {"message": "Expense Tracker Backend is running!"}

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000)
