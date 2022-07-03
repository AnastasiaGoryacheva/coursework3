from flask import request
from flask_restx import Namespace, Resource, abort

from project.container import movie_service
from project.exceptions import ItemNotFound

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """
        Get all movies.
        """
        try:
            page = request.args.get('page', type=int)
            status = request.args.get('status')
            filters = {
                'status': status,
                'page': page
            }
            return movie_service.get_all_movies(filters)
        except ItemNotFound:
            abort(404, 'Movies not found')


@movies_ns.route('/<int:movie_id>/')
class MovieView(Resource):
    def get(self, movie_id: int):
        """
        Get movie by id.
        """
        try:
            return movie_service.get_by_id(movie_id)
        except ItemNotFound:
            abort(404, 'Movie not found')
