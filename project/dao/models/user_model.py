from project.dao.models.base_model import Base
from project.setup_db import db


class User(Base):
    __tablename__ = 'user'

    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String(50), default="user")
    surname = db.Column(db.String(100), default=None)
    favorite_genre = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")

    def __repr__(self):
        return f"<User '{self.name.title()}'>"
