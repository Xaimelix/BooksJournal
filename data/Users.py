import datetime
from typing import Any

import sqlalchemy
from sqlalchemy import orm, Column
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from .db_session import SqlAlchemyBase


class Users(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    login = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    about = sqlalchemy.Column(sqlalchemy.String, nullable=True, default='Не указано')
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
