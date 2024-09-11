from flask import Flask
from .routes.upload import upload

# Config file
from .config import Config

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(upload)

    return app
