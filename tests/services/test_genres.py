from unittest.mock import patch

import pytest

from project.dao.models.genre_model import Genre
from project.exceptions import ItemNotFound
from project.services.genres_service import GenresService


class TestGenresService:

    @pytest.fixture()
    @patch('project.dao.GenresDAO')
    def genres_dao_mock(self, dao_mock):
        dao = dao_mock()
        dao.get_by_id.return_value = Genre(id=1, name='test_genre')
        dao.get_all.return_value = [
            Genre(id=1, name='test_genre_1'),
            Genre(id=2, name='test_genre_2'),
        ]
        return dao

    @pytest.fixture()
    def genres_service(self, genres_dao_mock):
        return GenresService(dao=genres_dao_mock)

    @pytest.fixture
    def genre(self, db):
        obj = Genre(name="genre")
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_get_genre(self, genres_service, genre):
        assert genres_service.get_by_id(genre.id)

    def test_genre_not_found(self, genres_dao_mock, genres_service):
        genres_dao_mock.get_by_id.return_value = None

        with pytest.raises(ItemNotFound):
            genres_service.get_by_id(10)
