from flask import Flask
from flask_pymongo import PyMongo
from flasgger import Swagger
from flask_cors import CORS
from config import Config
import os

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)

    mongo.init_app(app)
    
    CORS(app)  # Enable CORS

    swagger_template_path = os.path.join(os.path.dirname(__file__), '..', 'swagger.yaml')
    swagger = Swagger(app, template_file=swagger_template_path)

    from .routes import register_routes
    register_routes(app)

    return app
