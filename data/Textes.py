import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Texts(SqlAlchemyBase):
    __tablename__ = 'texts'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    id_book = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('books.id'))
    text = sqlalchemy.Column(sqlalchemy.Text)

    id_chapter = sqlalchemy.Column(sqlalchemy.Integer)

    Book = orm.relationship('Books', backref='texts')


