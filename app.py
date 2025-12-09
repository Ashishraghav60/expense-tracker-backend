from flask import Flask
from flask_cors import CORS
from config import Config
from database.models import db
from routes.auth_routes import auth_bp
from routes.expense_routes import expense_bp

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# Initialize DB
db.init_app(app)

with app.app_context():
    db.create_all()

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(expense_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
