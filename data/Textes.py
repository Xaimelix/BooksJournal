import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Books(SqlAlchemyBase):
    __tablename__ = 'textes'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    id_book = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    text = sqlalchemy.Column(sqlalchemy.Text, nullable=True)

    id_chapter = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("books.id"))

    user = orm.relationship('Books')
