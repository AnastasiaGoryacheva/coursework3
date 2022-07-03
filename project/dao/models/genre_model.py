from project.dao.models.base_model import Base
from project.setup_db import db


class Genre(Base):
    __tablename__ = 'genre'

    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<Genre '{self.name.title()}'>"
