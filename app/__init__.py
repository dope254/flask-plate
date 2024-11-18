from flask import Flask
from app.config import Config  # Custom configuration class

def create_app():
    """Application factory function."""
    app = Flask(__name__)
    app.config.from_object(Config)
    
    return app
