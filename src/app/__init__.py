from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "Simple Secret Key"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Adding routes
    from src.app.routes import routes

    app.register_blueprint(routes, url_prefix="/")

    return app
