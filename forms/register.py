import datetime

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, IntegerField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    email = EmailField('Электронная почта', validators=[DataRequired()])
    login = StringField('Имя пользователя', validators=[DataRequired()])
    # age = IntegerField('Количество лет', validators=[DataRequired()])
    about = 'Не указано'
    created_date = datetime.datetime.now()
    submit = SubmitField('Зарегестрироваться')
