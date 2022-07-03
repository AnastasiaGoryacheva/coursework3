from project.Schemas.director_schema import DirectorSchema
from project.dao.director_dao import DirectorsDAO
from project.dao.models.director_model import Director
from project.exceptions import ItemNotFound


class DirectorsService:
    def __init__(self, dao: DirectorsDAO) -> None:
        self.dao = dao

    def get_by_id(self, director_id: int) -> Director:
        director = self.dao.get_by_id(director_id)
        if not director:
            raise ItemNotFound(f'Director with id={director_id} not exists.')
        return DirectorSchema().dump(director)

    def get_all(self) -> list[Director]:
        directors = self.dao.get_all()
        return DirectorSchema(many=True).dump(directors)
