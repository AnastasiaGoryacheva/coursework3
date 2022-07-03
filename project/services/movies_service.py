from project.Schemas.movie_schema import MovieSchema
from project.dao.models.movie_model import Movie
from project.dao.movie_dao import MoviesDAO
from project.exceptions import ItemNotFound


class MoviesService:
    def __init__(self, dao: MoviesDAO) -> None:
        self.dao = dao

    def get_by_id(self, movie_id: int) -> Movie:
        movie = self.dao.get_by_id(movie_id)
        if not movie:
            raise ItemNotFound(f'Director with id={movie_id} not exists.')
        return MovieSchema().dump(movie)

    def get_all_movies(self, filters):
        if filters.get("page"):
            movies = self.dao.get_all_by_page(filters["page"])
        elif filters.get("status") == "new":
            movies = self.dao.get_all_by_status()
        else:
            movies = self.dao.get_all()
        return MovieSchema(many=True).dump(movies)
