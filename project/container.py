from project.dao import GenresDAO
from project.dao.director_dao import DirectorsDAO
from project.dao.movie_dao import MoviesDAO

from project.services import GenresService
from project.services.directors_service import DirectorsService
from project.services.movies_service import MoviesService
from project.setup_db import db


# DAO
genre_dao = GenresDAO(db.session)
movie_dao = MoviesDAO(db.session)
director_dao = DirectorsDAO(db.session)
# user_dao = UsersDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
movie_service = MoviesService(dao=movie_dao)
director_service = DirectorsService(dao=director_dao)
# user_service = UsersService(dao=user_dao)
