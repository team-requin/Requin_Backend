from flask import Flask

from views import Router

def create_app(*config_cls):
    flask_app = Flask(__name__)

    for config in config_cls:
        flask_app.config.from_object(config)

    Router(flask_app)

    return flask_app