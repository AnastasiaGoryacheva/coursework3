from sqlalchemy import desc

from project.config import BaseConfig
from project.dao.base_dao import BaseDAO
from project.dao.models.movie_model import Movie


class MoviesDAO(BaseDAO):
    def get_by_id(self, movie_id: int):
        return self.session.query(Movie).filter(Movie.id == movie_id).one_or_none()

    def get_all(self):
        return self.session.query(Movie).all()

    def get_all_by_status(self):
        return self.session.query(Movie).order_by(desc("year")).all()

    def get_all_by_page(self, page):
        return self.session.query(Movie).limit(
            BaseConfig.ITEMS_PER_PAGE
        ).offset(
            BaseConfig.ITEMS_PER_PAGE * page -
            BaseConfig.ITEMS_PER_PAGE
        )
