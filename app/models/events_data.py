from flask_login import UserMixin

# from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db


# from app.extensions import login_manager

# структура таблицы соревнований
class EventsData(UserMixin, db.Model):
    # структура данных пользователей
    __tablename__ = 'EventsData'

    id = db.Column(db.Integer, primary_key=True)
    # ид cоревнования
    # id_event = db.Column(db.Integer, nullable=False)
    # название соревнования
    name_player = db.Column(db.String, nullable=False)
    # дата начала соревнования
    sex_player = db.Column(db.String, nullable=False)
    # дата создания соревнования
    age_player = db.Column(db.String, nullable=False)
    # статус соревнования (готовится, идет, закочилось)
    gun_player = db.Column(db.String, nullable=False)
    # номинация участника
    section_player = db.Column(db.String, nullable=False)

    # Город учатника
    city_player = db.Column(db.String, nullable=False)
    # клуб участника
    organization_player = db.Column(db.String, nullable=False)
    # разряд участника


    # количество "10"
    # зачетные серии 1-10
    # сумма
    # выполненый разряд




    result_player = db.Column(db.Integer, nullable=True)

    # ид cоревнования
    id_event = db.Column(db.Integer, db.ForeignKey('EVENTS.id'), nullable=False)

    def __init__(self, id_event, name_player, sex_player, age_player, gun_player,
                 section_player, city_player, organization_player):
        self.id_event = id_event
        self.name_player = name_player
        self.sex_player = sex_player
        self.age_player = age_player
        self.gun_player = gun_player
        self.section_player = section_player
        self.city_player = city_player
        self.organization_player = organization_player

    def __repr__(self):
        return '%d, %d, %s, %s, %s, %s, %s, %s, %s' % (self.id, self.id_event, self.name_player, self.city_player,
                                                       self.organization_player, self.sex_player, self.age_player,
                                                       self.gun_player, self.section_player)
