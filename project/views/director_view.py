from flask_restx import Namespace, Resource, abort

from project.container import director_service
from project.exceptions import ItemNotFound

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        """
        Get all directors.
        """
        try:
            return director_service.get_all()
        except ItemNotFound:
            abort(404, 'Directors not found')


@directors_ns.route('/<int:director_id>/')
class DirectorView(Resource):
    def get(self, director_id: int):
        """
        Get director by id.
        """
        try:
            return director_service.get_by_id(director_id)
        except ItemNotFound:
            abort(404, 'Director not found')