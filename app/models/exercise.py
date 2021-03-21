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
    # название оружия
    name_gun = db.Column(db.String, nullable=False)
    # дистанция 1
    distance1 = db.Column(db.Integer, nullable=False)
    # дистанция 2
    distance2 = db.Column(db.Integer, nullable=False)
    # количество серий
    series = db.Column(db.Integer, nullable=False)
    # общщее количетсов выстрелов
    total_shoot = db.Column(db.Integer, nullable=False)
    # полное описание
    caption = db.Column(db.String, nullable=False)
    # мера очков
    measure = db.Column(db.String, nullable=False)

    #значения очков необходимые набрать для получения звания
    msmk_m = db.Column(db.Float, nullable=False)
    msmk_f = db.Column(db.Float, nullable=False)
    ms_m = db.Column(db.Float, nullable=False)
    ms_f = db.Column(db.Float, nullable=False)
    kms_m = db.Column(db.Float, nullable=False)
    kms_f = db.Column(db.Float, nullable=False)
    first_m = db.Column(db.Float, nullable=False)
    first_f = db.Column(db.Float, nullable=False)
    second_m = db.Column(db.Float, nullable=False)
    second_f = db.Column(db.Float, nullable=False)
    third_m = db.Column(db.Float, nullable=False)
    third_f = db.Column(db.Float, nullable=False)

    EventsData = db.relationship('EventsData', backref='NameExercise', lazy='dynamic')

    def __init__(self, ExerciseID, name, name_gun, dist, series, total_shoot, caption, measure, rank_values):
        self.ExerciseID = ExerciseID
        self.name = name
        self.name_gun = name_gun
        self.distance1 = dist[0]
        self.distance2 = dist[1]
        self.series = series
        self.total_shoot = total_shoot
        self.caption = caption
        self.measure = measure
        self.msmk_m = rank_values[0]
        self.msmk_f = rank_values[1]
        self.ms_m = rank_values[2]
        self.ms_f = rank_values[3]
        self.kms_m = rank_values[4]
        self.kms_f = rank_values[5]
        self.first_m = rank_values[6]
        self.first_f = rank_values[7]
        self.second_m = rank_values[8]
        self.second_f = rank_values[9]
        self.third_m = rank_values[10]
        self.third_f = rank_values[11]


    def __repr__(self):
        return '%d, %s, %d, %d' % (self.ExerciseID, self.name, self.series, self.total_shoot)
