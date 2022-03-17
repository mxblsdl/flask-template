from flask import Flask


def init_app():
    app = Flask(__name__)

    with app.app_context():
        from . import routes

        # Import and build the Dash application
        from .dash_app.dashboard import init_dash

        # Flask app is passed as the server to Dash
        app = init_dash(server=app)

        # Returns the flask app with embedded dash page
        return app
