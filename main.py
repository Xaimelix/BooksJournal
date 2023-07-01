from flask import Flask, render_template

from data import db_session

app = Flask(__name__)
from config import SECRET_KEY

app.config['SECRET_KEY'] = SECRET_KEY
db_session.global_init("db/geometry.db")


@app.route('/index')
@app.route('/')
def base():
    """Основная старница"""
    return render_template('base.html')


if __name__ == '__main__':
    app.run()
