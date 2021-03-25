from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db
from app.models.user import USER
from app.models.events import EVENTS
from app.models.events_data import EventsData
from app.models.exercise import Exercise
from app.models.exercise_data import ExerciseData
from app.models.ranktable import RankTable


def admin_pg_db():
    # создает все таблицы
    print("Create_ALL")
    # Base.metadata.create_all(engine)
    #дропает все даблицы
    # Base.metadata.drop_all(engine)


def select_electro():
    # Выбор данных из БД
    return db.session.query(USER).order_by(USER.rank.desc())


def select_events(id_user):
    # Выбор данных из БД
    # t = db.session.query(EVENTS).order_by(EVENTS.rank.desc())
    # t = db.session.query(EVENTS.event_name, EVENTS.create_date ).all()
    if id_user == "all":
        return db.session.query(EVENTS, USER.login).order_by(EVENTS.rank.desc()).filter(EVENTS.id_user == USER.id)
        # return db.session.query(EVENTS).order_by(EVENTS.rank.desc()).filter_by(id_user=id_user)
    else:
        return db.session.query(EVENTS).order_by(EVENTS.rank.desc()).filter_by(id_user=id_user).all()
        # return db.session.query(EVENTS, USER.login).order_by(EVENTS.rank.desc()).filter(EVENTS.id_user == USER.id).\
        #     filter_by(id_user=id_user).all()
    # return t


def select_event(id_event):
    # print(id_event)
    return db.session.query(EVENTS).order_by(EVENTS.id.desc()).filter_by(id=id_event).first()


def select_event_members(id_event):
    # print(id_event)
    # return db.session.query(EVENTS, USER.login).order_by(EVENTS.rank.desc()).filter(EVENTS.id_user == USER.id)
    # return db.session.query(EventsData).filter_by(id_event=id_event).all()
    # return db.session.query(EventsData, RankTable.name).filter_by(id_event=id_event).all()

    return db.session.query(EventsData, RankTable.name) \
        .join(RankTable) \
        .order_by(EventsData.ExerciseID, EventsData.result_player.desc()) \
        .filter(EventsData.id_event == id_event).all()

# удаление соревнования вместе с его участниками
def remove_event(id_event):
    # удаляет участников в соревновании по ид соревнования
    db.session.query(EventsData).filter_by(id_event=id_event).delete()
    db.session.commit()
    # удаляет само пустое соревнование
    db.session.query(EVENTS).filter_by(id=id_event).delete()
    db.session.commit()


# удаляет строку игрока из таблицы даных игроков
def remove_event_data(id_user):
    db.session.query(ExerciseData).filter_by(EventsDataID=id_user).delete()
    db.session.commit()

    db.session.query(EventsData).filter_by(id=id_user).delete()
    db.session.commit()


# добавляет соревнование
def add_events(id_curent_user, event_name, caption, start_date):
    create_date = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
    new_events = EVENTS(id_user=id_curent_user, event_name=event_name, start_date=start_date,
                        create_date=create_date, caption=caption)
    db.session.add(new_events)
    db.session.commit()


# добавляет игрока в соревнование
def add_event_data(id_event,ExerciseID, RankID,  name_player, sex_player, age_player, gun_player, section_player,
                   city_player, organization_player):
    # create_date = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
    new_events_data = EventsData(id_event=id_event, ExerciseID=ExerciseID, RankID=RankID, name_player=name_player,
                                 sex_player=sex_player, age_player=age_player, gun_player=gun_player,
                                 section_player=section_player, city_player=city_player,
                                 organization_player=organization_player)
    db.session.add(new_events_data)
    db.session.commit()


# добавляет игрока в соревнование
def set_exercise_data(EventsDataID, ex1=0, ex2=0, ex3=0, ex4=0, ex5=0, ex6=0, ex7=0, ex8=0, ex9=0, ex10=0, tens_count=0):
    # create_date = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
    ExerciseData.query.filter_by(EventsDataID=EventsDataID).delete()
    db.session.commit()
    new_exercise_data = ExerciseData(EventsDataID=EventsDataID, ex1=ex1, ex2=ex2, ex3=ex3, ex4=ex4, ex5=ex5, ex6=ex6,
                                     ex7=ex7, ex8=ex8, ex9=ex9, ex10=ex10, tens_count=tens_count)
    db.session.add(new_exercise_data)
    db.session.commit()

    # переприсваевывает значения результатов из таблицы результатов в таблицу данных соревнования (костыль)
    EvData = EventsData.query.filter_by(id=EventsDataID).first()
    ExData = ExerciseData.query.filter_by(EventsDataID=EventsDataID).first()
    EvData.result_player = ExData.result_player
    EvData.reached_rank = id_reached_rank(EventsDataID)
    db.session.commit()


# вычисляет ид достигнутого разряда
def id_reached_rank(EventsDataID):
    EvData = EventsData.query.filter_by(id=EventsDataID).first()
    ExData = ExerciseData.query.filter_by(EventsDataID=EventsDataID).first()
    # print(EvData.gun_player, EvData.sex_player)
    Ex = Exercise.query.filter_by(ExerciseID=EvData.ExerciseID).first().list_of_value()
    result = ExData.result_player
    if EvData.sex_player == "М":
        s = 0
    else:
        s = 1
    # print(s)
    for i in range(s, len(Ex), 2):
        if result >= Ex[i] and Ex[i] != 0:
            if i == 10 or i == 11:
                return "III"
            if i == 8 or i == 9:
                return "II"
            if i == 6 or i == 7:
                return "I"
            if i == 4 or i == 5:
                return "КМС"
            if i == 2 or i == 3:
                return "МС"
            if i == 0 or i == 1:
                return "МСМК"
    return "Б/Р"


# запрос на регистрацию пользователя
def signup_query(username, email, password):
    user = USER.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database
    create_date = str(datetime.now())
    # if user:# if a user is found, we want to redirect back to signup page so user can try again
    #     return 0

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    # print("test=",user, email,generate_password_hash(password, method='sha256'))
    new_user = USER(login=username, email=email, password_hash=generate_password_hash(password, method='sha256'), date_user_made=create_date)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    # return 1

# def login(email, password):
#     if 0:
#         return 0
#     else:
#         email = USER.query.filter_by(email=email).first()
#         password = USER.query.filter_by(password=password).first()
#         if email and password:
#             return 1


# переименовать функции 1 выдает количество выстрелов а также серии по ид упражнения для формы заполения результатов
def parametr_exercise(id):
    param = db.session.query(EventsData.ExerciseID).filter_by(id=id).first()
    param2 = db.session.query(Exercise.total_shoot, Exercise.series).filter_by(ExerciseID=param).first()
    return param2
# возвращвет ид упражнение по имени
def _id_exercise_by_name(name):
    # print(db.session.query(Exercise.ExerciseID, Exercise.name_gun).filter_by(name=name).first()[1])
    return db.session.query(Exercise.ExerciseID).filter_by(name=name).first()[0]

# возвращвет название оружия по имени
def _gun_exercise_by_name(name):
    print(db.session.query(Exercise.name_gun).filter_by(name=name).first()[0])
    return db.session.query(Exercise.name_gun).filter_by(name=name).first()[0]


def select_result(id):
    t1 = db.session.query(ExerciseData).filter_by(EventsDataID=id).first()
    t2 = db.session.query(EventsData).filter_by(id=id).first()
    return t1,t2