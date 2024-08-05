from flask import Flask
from flask_pymongo import PyMongo
from flasgger import Swagger
from flask_cors import CORS
from config import Config
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import os

mongo = PyMongo()
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)

    # Initialize components
    mongo.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    
    CORS(app)  # Enable CORS

    swagger_template_path = os.path.join(os.path.dirname(__file__), '..', 'swagger.yaml')
    swagger = Swagger(app, template_file=swagger_template_path)
    
    # Attach bcrypt to the app context
    app.bcrypt = bcrypt

    from .routes import register_routes
    register_routes(app)

    return app
