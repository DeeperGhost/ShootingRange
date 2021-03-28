from flask_login import UserMixin

# from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db
# from app.extensions import login_manager

# структура таблицы соревнований
class EVENTS(UserMixin, db.Model):
    # структура данных пользователей
    __tablename__ = 'EVENTS'

    id = db.Column(db.Integer, primary_key=True)
    # ид создателя соревнования
    # id_user = db.Column(db.Integer, nullable=False)
    # название соревнования
    event_name = db.Column(db.String, nullable=False)
    # дата начала соревнования
    start_date = db.Column(db.String, nullable=False)
    # дата окончания соревнования
    end_date = db.Column(db.String, nullable=True)
    # дата создания соревнования
    create_date = db.Column(db.String, nullable=False)
    # статус соревнования (готовится, идет, закочилось)
    event_status = db.Column(db.String, nullable=True)

    # описание соревнования
    caption = db.Column(db.String, nullable=True)
    # оценка соревнования (ранг)
    rank = db.Column(db.Integer, nullable=True)

    # user_id = db.Column(db.Integer, db.ForeignKey('USERS.id'))
    id_user = db.Column(db.Integer, db.ForeignKey('USERS.id'), nullable=False)

    events_data = db.relationship('EventsData', backref='author', lazy='dynamic')


    def __init__(self, id_user, event_name, start_date,end_date, create_date, caption):
        self.id_user = id_user
        self.event_name = event_name
        self.start_date = start_date
        self.end_date = end_date
        self.create_date = create_date
        self.caption = caption

    def __repr__(self):
        return '%d, %s, %s, %s, %s, %s' % (self.id, self.id_user, self.event_name,
                                           self.start_date, self.create_date, self.caption)

    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)
    #
    # def check_password(self, password):
    #     return check_password_hash(self.password_hash, password)