from project.Schemas.genre_schema import GenreSchema
from project.dao import GenresDAO
from project.dao.models.genre_model import Genre
from project.exceptions import ItemNotFound


class GenresService:
    def __init__(self, dao: GenresDAO) -> None:
        self.dao = dao

    def get_by_id(self, genre_id: int) -> Genre:
        genre = self.dao.get_by_id(genre_id)
        if not genre:
            raise ItemNotFound(f'Genre with id={genre_id} not exists.')
        return GenreSchema().dump(genre)

    def get_all(self) -> list[Genre]:
        genres = self.dao.get_all()
        return GenreSchema(many=True).dump(genres)
