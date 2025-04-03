import os

class Config:
    # Get the DATABASE_URL from environment variables or use a default value.
    DATABASE_URL = os.getenv("DATABASE_URL", "db url ***")
    # Example: add other configuration variables here if needed
    DEBUG = os.getenv("DEBUG", True)
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt key ***")  
