from project.config import DevelopmentConfig
from project.dao.models.director_model import Director
from project.dao.models.genre_model import Genre
from project.dao.models.movie_model import Movie
from project.dao.models.user_model import User
from project.server import create_app, db

app = create_app(DevelopmentConfig)

app.app_context().push()


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "Movie": Movie,
        "Director": Director,
        "User": User
    }


if __name__ == '__main__':
    app.run(port=25000)
