from app.extensions import db


class USER(db.Model):
    # структура данных пользователей
    __tablename__ = 'USERS'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)
    key_pass = db.Column(db.String, nullable=True)

    family = db.Column(db.String, nullable=True)
    name = db.Column(db.String, nullable=True)
    second_name = db.Column(db.String, nullable=True)

    individual_key = db.Column(db.String, nullable=True)
    information = db.Column(db.String, nullable=True)

    rank = db.Column(db.Integer, nullable=True)

    def __init__(self, login, email, password, key_pass):
        self.login = login
        self.email = email
        self.password = password
        self.key_pass = key_pass

    def __repr__(self):
        return '%d, %s, %s, %s, %s' % (self.id, self.login, self.email, self.password, self.key_pass)