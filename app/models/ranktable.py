from flask_login import UserMixin

from app.extensions import db


# структура таблицы соревнований
class RankTable(UserMixin, db.Model):
    # имя таблицы
    __tablename__ = 'RankTable'

    # ид строки
    id = db.Column(db.Integer, primary_key=True)
    #
    RankID = db.Column(db.Integer, nullable=False, unique=True)
    # сокращенное название
    name = db.Column(db.String, nullable=False)
    # полное название
    name_full = db.Column(db.String, nullable=False)
    # возpаст с которого доступен
    age = db.Column(db.Integer, nullable=False)

    EventsData = db.relationship('EventsData', backref='EventsData', lazy='dynamic')

    def __init__(self, RankID, name, name_full, age):
        self.RankID = RankID
        self.name = name
        self.name_full = name_full
        self.age = age

    def __repr__(self):
        return '%s, %s, %d' % (self.name, self.name_full, self.age)
