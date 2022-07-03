from contextlib import suppress
from typing import Any, Dict, List, Type

from sqlalchemy.exc import IntegrityError

from project.config import DevelopmentConfig
from project.dao.models.base_model import Base
from project.dao.models.genre_model import Genre

from project.server import create_app
from project.setup_db import db

from project.utils import read_json


def load_data(data: List[Dict[str, Any]], model: Type[Base]) -> None:
    for item in data:
        item['id'] = item.pop('pk')
        db.session.add(model(**item))


if __name__ == '__main__':
    fixtures: Dict[str, List[Dict[str, Any]]] = read_json("fixtures.json")

    app = create_app(DevelopmentConfig)

    with app.app_context():
        # TODO: [fixtures] Добавить модели Directors и Movies
        load_data(fixtures['genres'], Genre)

        with suppress(IntegrityError):
            db.session.commit()
