from project.dao import GenresDAO
from project.dao.auth_dao import AuthDAO
from project.dao.director_dao import DirectorsDAO
from project.dao.movie_dao import MoviesDAO
from project.dao.user_dao import UsersDAO


from project.services.auth_service import AuthService
from project.services.directors_service import DirectorsService
from project.services.genres_service import GenresService
from project.services.movies_service import MoviesService
from project.services.users_service import UsersService
from project.setup_db import db


# DAO
genre_dao = GenresDAO(db.session)
movie_dao = MoviesDAO(db.session)
director_dao = DirectorsDAO(db.session)
user_dao = UsersDAO(db.session)
auth_dao = AuthDAO(session=db.session)

# Services
genre_service = GenresService(dao=genre_dao)
movie_service = MoviesService(dao=movie_dao)
director_service = DirectorsService(dao=director_dao)
user_service = UsersService(user_dao=user_dao)
auth_service = AuthService(auth_dao=auth_dao)
