from flask import Flask # type: ignore
from .routes import auction_bp # type: ignore
from .config import Config # type: ignore

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register the auction blueprint
    app.register_blueprint(auction_bp)
    
    return app


