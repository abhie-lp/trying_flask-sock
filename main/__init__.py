"""Main file to run the app"""

from flask import Flask
from flask_sock import Sock

sock = Sock()


def create_app() -> Flask:
    """Create flask app using the factory pattern"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="hands_on_flask-sock_package",
    )

    @app.route("/test")
    def test():
        return "Flask server running."

    # Import the module containing websocket routes
    import main.ws
    sock.init_app(app)

    return app
