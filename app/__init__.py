from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from config import Config

db = SQLAlchemy()
swagger = Swagger()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    swagger.init_app(app)

    with app.app_context():
        from .routes import bp as api_bp
        app.register_blueprint(api_bp)
        db.create_all()

    return app
