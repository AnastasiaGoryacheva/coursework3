from project.dao.models.base_model import Base
from project.setup_db import db


class Director(Base):
    __tablename__ = 'director'

    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<Director '{self.name.title()}'>"
