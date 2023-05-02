
from flask import Flask
from .routes import index, api

def create_app() -> Flask :
    app = Flask(__name__, static_url_path="/", static_folder="./static")
    app.register_blueprint(index)
    app.register_blueprint(api)
    return app