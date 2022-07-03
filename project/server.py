from flask import Flask
from flask_restx import Api

from project.setup_db import db
from project.views.auth_view import auth_ns

from project.views.director_view import directors_ns
from project.views.genre_view import genres_ns
from project.views.movie_view import movies_ns
from project.views.user_view import user_ns


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    app.app_context().push()

    api = Api(
        authorizations={
            "Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}
        },
        title="Flask Course Project 3",
        doc="/docs",
    )
    api.init_app(app)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)

    db.init_app(app)

    return app
