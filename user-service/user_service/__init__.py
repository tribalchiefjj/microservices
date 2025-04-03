from flask import Flask # type: ignore
from flask_jwt_extended import JWTManager # type: ignore
from .config import Config # type: ignore
from .routes import user_bp # type: ignore

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize JWTManager with the app
    app.config["JWT_SECRET_KEY"] = "jwt key ****"  
    jwt = JWTManager(app)

    # Register your blueprint(s)
    app.register_blueprint(user_bp)
    
    return app
