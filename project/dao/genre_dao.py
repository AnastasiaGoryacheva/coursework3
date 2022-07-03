from project.dao.base_dao import BaseDAO
from project.dao.models.genre_model import Genre


class GenresDAO(BaseDAO):
    def get_by_id(self, genre_id: int):
        return self.session.query(Genre).filter(Genre.id == genre_id).one_or_none()

    def get_all(self):
        return self.session.query(Genre).all()
