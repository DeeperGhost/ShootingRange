from flask_login import UserMixin

from app.extensions import db


# структура таблицы соревнований
class BaseTable(UserMixin, db.Model):
    # имя таблицы
    __tablename__ = 'BaseTable'

    # ид строки
    id = db.Column(db.Integer, primary_key=True)
    # название дисциплины
    name = db.Column(db.String, nullable=False)
    # название оружия
    gun_name = db.Column(db.String, nullable=False)
    # описание дисциплины
    caption = db.Column(db.String, nullable=False)
    # единица измерения
    measure = db.Column(db.String, nullable=False)
    # название разяда
    rank = db.Column(db.String, nullable=False)
    # пол
    id_sex = db.Column(db.Integer,  db.ForeignKey('SexTable.id'), nullable=False)
    # количесво записей (мишеней*2)
    number_shoot = db.Column(db.Integer, nullable=False)
    # необходимое количество балов
    value = db.Column(db.Integer, nullable=False)

    def __init__(self, name, gun_name, caption, measure, rank, id_sex, number_shoot, value):
        # тектовые значения
        self.name = name
        self.gun_name = gun_name
        self.caption = caption
        self.measure = measure
        self.rank = rank
        # численные значения
        self.id_sex = id_sex
        self.number_shoot = number_shoot
        self.value = value

    def __repr__(self):
        return '%s, %s, %s, %s, %s, %d, %d, %d' % (self.name, self.gun_name, self.caption, self.measure, self.rank,
                                                   self.id_sex, self.number_shoot, self.value)
