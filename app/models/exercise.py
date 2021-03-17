from flask_login import UserMixin

from app.extensions import db


# структура справочника соревнований
class Exercise(UserMixin, db.Model):
    # структура данных пользователей
    __tablename__ = 'Exercise'

    id = db.Column(db.Integer, primary_key=True)
    # id упражнения
    ExerciseID = db.Column(db.Integer, nullable=False, unique=True)
    # обозначение

    name = db.Column(db.String, nullable=False)
    # количество серий
    series = db.Column(db.Integer, nullable=False)
    # общщее количетсов выстрелов
    total_shoot = db.Column(db.Integer, nullable=False)

    EventsData = db.relationship('EventsData', backref='NameExercise', lazy='dynamic')

    def __init__(self, ExerciseID, name, series, total_shoot):
        self.ExerciseID = ExerciseID
        self.name = name
        self.series = series
        self.total_shoot = total_shoot

    def __repr__(self):
        return '%d, %s, %d, %d' % (self.ExerciseID, self.name, self.series, self.total_shoot)
