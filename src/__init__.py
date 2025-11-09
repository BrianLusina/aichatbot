from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Task xyz: write the code for creating an object of SQLAlchemy here

def create_app():
    # Creating a new App
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Simple Secret Key"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Task xyz: Write the code for adding your database to the application here

    # Task xyz: Call your database here

    # Adding routes
    from .routes import routes
    app.register_blueprint(routes, url_prefix="/")

    return app

# Task xyz: Write the code for your database method here