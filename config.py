import os
from dotenv import load_dotenv

# Load .env file (works locally, Render ignores this but keeps variables from Dashboard)
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key")

    # Read database URL from Render or .env
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    # Render sometimes sends URL starting with "postgres://"
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
