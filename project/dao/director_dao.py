from project.dao.base_dao import BaseDAO
from project.dao.models.director_model import Director


class DirectorsDAO(BaseDAO):
    def get_by_id(self, director_id: int):
        return self.session.query(Director).filter(Director.id == director_id).one_or_none()

    def get_all(self):
        return self.session.query(Director).all()
