from flask_login import UserMixin

from app.extensions import db


# структура таблицы соревнований
class BaseTable(UserMixin, db.Model):
    # имя таблицы
    __tablename__ = 'BaseTable'

    # ид строки
    id = db.Column(db.Integer, primary_key=True)
    # ид строки
    static_id = db.Column(db.Integer, nullable=False)
    # название дисциплины
    short_caption = db.Column(db.String, nullable=False)
    # короткое обозначение оружия
    gun_short = db.Column(db.String, nullable=False)
    # полное название оружия
    gun_name = db.Column(db.String, nullable=False)
    # дистанция стрельбы 1
    distance_1 = db.Column(db.Integer, nullable=False)
    # дистанция стрельбы 2 если имеется
    distance_2 = db.Column(db.Integer, nullable=True)
    # общее количество выстрелов
    total_shoot = db.Column(db.Integer, nullable=False)
    # количество серий
    series = db.Column(db.Integer, nullable=False)
    # полное описание дисциплины
    caption = db.Column(db.String, nullable=False)
    # единица измерения
    measure = db.Column(db.String, nullable=False)
    # название разяда
    rank = db.Column(db.String, nullable=False)
    # пол
    id_sex = db.Column(db.Integer,  db.ForeignKey('SexTable.id'), nullable=False)

    # необходимое количество балов
    value = db.Column(db.Float, nullable=False)

    def __init__(self, static_id, short_caption, gun_short, gun_name, distance_1, total_shoot,
                 series, caption, measure, rank, id_sex, value, distance_2=0):
        # тектовые значения
        self.static_id = static_id
        self.short_caption = short_caption
        self.gun_short = gun_short
        self.gun_name = gun_name
        self.distance_1 = distance_1
        self.distance_2 = distance_2
        self.total_shoot = total_shoot
        self.series = series
        self.caption = caption
        self.measure = measure
        self.rank = rank
        self.id_sex = id_sex
        self.value = value

    def __repr__(self):
        return '%s, %s, %s, %s, %s, %d, %d' % (self.short_caption, self.gun_short, self.caption,
                                               self.measure, self.rank, self.id_sex, self.value)
