from flask_login import UserMixin

from app.extensions import db


# структура таблицы соревнований
class SexTable(UserMixin, db.Model):
    # имя таблицы
    __tablename__ = 'SexTable'

    # ид строки
    id = db.Column(db.Integer, primary_key=True)
    # сокращенное название
    name = db.Column(db.String, nullable=False)
    # полное название
    name_full = db.Column(db.String, nullable=False)

    basetable = db.relationship('BaseTable', backref='author', lazy='dynamic')

    def __init__(self, name, name_full):
        self.name = name
        self.name_full = name_full

    def __repr__(self):
        return '%d, %s, %s' % (self.id, self.name, self.name_full)
