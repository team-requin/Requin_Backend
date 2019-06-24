from flask import Blueprint
from flask_restful import Api

def Router(flask_app):
    from app.views.api.api_v1.index import Index

    blueprint_v1 = Blueprint('api_v1',__name__)
    api_v1 = Api(blueprint_v1)

    # Add Api Resource
    api_v1.add_resource(Index, '/')

    # Register blueprint
    flask_app.register_blueprint(blueprint_v1)