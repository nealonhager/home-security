from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

from .models import db, ma
from .routes import api
from .services import init_services
from .utils.logging_config import setup_logging

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
    
    # Set up logging
    loggers = setup_logging(app)
    
    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    
    # Register blueprints
    app.register_blueprint(api, url_prefix='/api')
    
    # Initialize services (including scheduler)
    init_services(app)
    
    # Create tables
    with app.app_context():
        db.create_all()
        app.logger.info("Database tables created")
    
    return app
