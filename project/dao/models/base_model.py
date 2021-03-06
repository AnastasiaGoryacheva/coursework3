from sqlalchemy import Column, Integer

from project.setup_db import db


class Base(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
