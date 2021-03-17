from flask_login import UserMixin

# from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db


# структура таблицы соревнований
class ExerciseData(UserMixin, db.Model):
    # структура данных пользователей
    __tablename__ = 'ExerciseData'

    # id
    ExerciseDataID = db.Column(db.Integer, primary_key=True)
    # id EventsData
    EventsDataID = db.Column(db.Integer, db.ForeignKey('EventsData.id'), nullable=False)

    # упражнение 1
    ex1 = db.Column(db.Float, nullable=True)
    # упражнение 2
    ex2 = db.Column(db.Float, nullable=True)
    # упражнение 3
    ex3 = db.Column(db.Float, nullable=True)
    # упражнение 4
    ex4 = db.Column(db.Float, nullable=True)
    # упражнение 5
    ex5 = db.Column(db.Float, nullable=True)
    # упражнение 6
    ex6 = db.Column(db.Float, nullable=True)
    # упражнение 7
    ex7 = db.Column(db.Float, nullable=True)
    # упражнение 8
    ex8 = db.Column(db.Float, nullable=True)
    # упражнение 9
    ex9 = db.Column(db.Float, nullable=True)
    # упражнение 10
    ex10 = db.Column(db.Float, nullable=True)

    # количество 10
    tens_count = db.Column(db.Integer, nullable=True)
    # сводный результат
    result_player = db.Column(db.Integer, nullable=True)

    def __init__(self, EventsDataID,
                 ex1=0, ex2=0, ex3=0, ex4=0, ex5=0, ex6=0, ex7=0, ex8=0, ex9=0, ex10=0, tens_count=0):

        self.EventsDataID = EventsDataID
        self.ex1 = ex1
        self.ex2 = ex2
        self.ex3 = ex3
        self.ex4 = ex4
        self.ex5 = ex5
        self.ex6 = ex6
        self.ex7 = ex7
        self.ex8 = ex8
        self.ex9 = ex9
        self.ex10 = ex10
        self.tens_count = tens_count
        self.result_player = ex1 + ex2 + ex3 + ex4 + ex5 + ex6 + ex7 + ex8 + ex9 + ex10

    def __repr__(self):
        return '%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d' % (self.EventsDataID,
                                                                       self.ex1, self.ex2, self.ex3, self.ex4,
                                                                       self.ex5, self.ex6, self.ex7, self.ex8,
                                                                       self.ex9, self.ex10,
                                                                       self.result_player, self.tens_count)
