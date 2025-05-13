from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from .config import Config

# Initialize extensions
db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # Register additional Blueprints
    from .routes.account_routes import account_bp
    from .routes.transaction_routes import transaction_bp
    app.register_blueprint(account_bp, url_prefix='/api/v1')
    app.register_blueprint(transaction_bp, url_prefix='/api/v1')

    return app