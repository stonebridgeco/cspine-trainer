from flask import Flask
from config import Config
from models import db, User
from routes import init_app_routes # We'll define routes in routes.py

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all() # Create database tables if they don't exist

    init_app_routes(app) # Initialize routes

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=False) # debug=True for development, set to False in production
