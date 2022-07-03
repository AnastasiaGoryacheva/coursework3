from flask_restx import Namespace, Resource, abort

from project.container import genre_service
from project.exceptions import ItemNotFound

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        """
        Get all genres.
        """
        try:
            return genre_service.get_all()
        except ItemNotFound:
            abort(404, 'Genres not found')


@genres_ns.route('/<int:genre_id>/')
class GenreView(Resource):
    def get(self, genre_id: int):
        """
        Get genre by id.
        """
        try:
            return genre_service.get_by_id(genre_id)
        except ItemNotFound:
            abort(404, 'Genre not found')
