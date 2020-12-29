from flask_login import UserMixin
from app.extensions import db


class USER(UserMixin, db.Model):
    # структура данных пользователей
    __tablename__ = 'USERS'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)

    date_user_made = db.Column(db.String, nullable=False)

    family = db.Column(db.String, nullable=True)
    name = db.Column(db.String, nullable=True)
    second_name = db.Column(db.String, nullable=True)

    individual_key = db.Column(db.String, nullable=True)
    information = db.Column(db.String, nullable=True)


    rank = db.Column(db.Integer, nullable=True)

    def __init__(self, login, email, password_hash, date_user_made):
        self.login = login
        self.email = email
        self.password_hash = password_hash
        self.date_user_made = date_user_made

    def __repr__(self):
        return '%d, %s, %s, %s' % (self.id, self.login, self.email, self.password_hash)
