from .auth_view import auth_ns
from .director_view import directors_ns
from .genre_view import genres_ns
from .movie_view import movies_ns
from .user_view import user_ns

__all__ = [
    "genres_ns",
    "directors_ns",
    "movies_ns",
    "auth_ns",
    "user_ns"
]
