from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from config import Config
from db import Base
from resources.user import UserListResource


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_resources(app)
    return app


def register_resources(app):
    api = Api(app)
    api.add_resource(UserListResource, '/users/')


if __name__ == '__main__':
    app = create_app()
    app.run()
