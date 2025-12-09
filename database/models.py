from database.db import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100))
    description = db.Column(db.String(255))
    date = db.Column(db.DateTime, default=datetime.utcnow)
