class Config:
    """Configuration settings for the Flask app."""
    SECRET_KEY = "your-secret-key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
