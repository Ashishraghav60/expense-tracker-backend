from flask_cors import CORS
from flask import Flask
from database.models import db
import config

from routes.auth_routes import auth_bp
from routes.expense_routes import expense_bp

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = config.DATABASE_URI
app.config["SECRET_KEY"] = config.SECRET_KEY

db.init_app(app)

# Register routes
app.register_blueprint(auth_bp)
app.register_blueprint(expense_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    if __name__ == "__main__":
     app.run(host="0.0.0.0")
