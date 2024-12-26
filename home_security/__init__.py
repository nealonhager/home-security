from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

from .models import db
from .schemas import ma
from .routes import api

def create_app():
    load_dotenv()
    
    app = Flask(__name__)
    
    # Configure SQLAlchemy for MySQL
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL', 
        'mysql://root:root@localhost/home_security'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
    
    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    
    # Register blueprints
    app.register_blueprint(api, url_prefix='/api')
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app
