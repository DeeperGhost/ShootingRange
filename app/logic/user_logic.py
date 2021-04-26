import json
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db
from app.models.user import USER
from app.models.events import EVENTS
from app.models.events_data import EventsData
from app.models.exercise import Exercise
from app.models.exercise_data import ExerciseData
from app.models.ranktable import RankTable
from app.models.events import RoleEvents


def admin_pg_db():
    # создает все таблицы
    print("Create_ALL")
    # Base.metadata.create_all(engine)
    #дропает все даблицы
    # Base.metadata.drop_all(engine)


def select_events(id_current_user=0, lk=False):
    """селект данных для таблицы игр"""
    # Выбор данных из БД
    if lk:
        table = db.session.query(USER.username, EVENTS.id, EVENTS.event_name, EVENTS.start_date, EVENTS.end_date,
                                 EVENTS.create_date, EVENTS.caption, EVENTS.event_status, EVENTS.id_base_event) \
            .order_by(EVENTS.rank.desc()) \
            .filter(EVENTS.id_user == USER.id) \
            .filter(EVENTS.id_user == id_current_user) \
            .all()
    else:
        table = db.session.query(USER.username, EVENTS.id, EVENTS.event_name, EVENTS.start_date, EVENTS.end_date,
                                 EVENTS.create_date, EVENTS.caption, EVENTS.event_status) \
            .order_by(EVENTS.rank.desc()) \
            .filter(EVENTS.id_user == USER.id) \
            .filter(EVENTS.id == EVENTS.id_base_event) \
            .all()

    list_dict = []
    # вариант для авторизованого пользователя с чек боксом
    if id_current_user != 0:
        for i in table:
            i_dict = i._asdict()  # sqlalchemy.util._collections.result , has a method called _asdict()
            i_dict.update({'selected': select_checked(id_user=id_current_user, id_event=i_dict['id'])})
            list_dict.append(i_dict)
    else:
    #вариант для неавторизрваного пользователя без чек бокса
        for i in table:
            i_dict = i._asdict()  # sqlalchemy.util._collections.result , has a method called _asdict()
            list_dict.append(i_dict)
    return list_dict


def select_event(id_event):
    # print(id_event)
    return db.session.query(EVENTS).order_by(EVENTS.id.desc()).filter_by(id=id_event).first()


def select_event_members(id_event, all=True):
    """Выбирает данные участников соревнования all=True для общей таблицы False для частной"""
    # print(id_event)
    # return db.session.query(EVENTS, USER.login).order_by(EVENTS.rank.desc()).filter(EVENTS.id_user == USER.id)
    # return db.session.query(EventsData).filter_by(id_event=id_event).all()
    # return db.session.query(EventsData, RankTable.name).filter_by(id_event=id_event).all()
    if all:
        t = db.session.query(EventsData, RankTable.name, EVENTS)\
            .join(RankTable) \
            .order_by(EventsData.ExerciseID, EventsData.result_player.desc()) \
            .filter(EVENTS.id_base_event == id_event)\
            .filter(EventsData.id_event == EVENTS.id).all()
    else:
        t = db.session.query(EventsData, RankTable.name) \
            .join(RankTable) \
            .order_by(EventsData.ExerciseID, EventsData.result_player.desc()) \
            .filter(EventsData.id_event == id_event).all()
    return t

def remove_event(id_event):
    """Функция удаляет соревнования вместе с участниками,
     а также результами этих участников, на вход получает ID соревнования"""
    # удаляет роли соревнования в таблице ролей
    db.session.query(RoleEvents).filter_by(id_event=id_event).delete()
    db.session.commit()

    # Удаляет результаты учатников соревнования
    t = db.session.query(EventsData.id).filter_by(id_event=id_event).all()
    [remove_event_data(i) for i in t]

    # удаляет участников в соревновании по ид соревнования
    db.session.query(EventsData).filter_by(id_event=id_event).delete()
    db.session.commit()
    # удаляет само пустое соревнование
    db.session.query(EVENTS).filter_by(id=id_event).delete()
    db.session.commit()


def remove_event_data(id_user):
    """Удаляет участника соревнования вместе с его результатами,
     на вход получает ID участника"""
    db.session.query(ExerciseData).filter_by(EventsDataID=id_user).delete()
    db.session.commit()

    db.session.query(EventsData).filter_by(id=id_user).delete()
    db.session.commit()


def show_event(id_event=0, id_base_event=0, id_user=0):
    """Возращает Event по id  или id_base """
    if id_event != 0:
        t = db.session.query(EVENTS).filter_by(id=id_event).first()
    # if id_base_event == 0:
    #     # t = db.session.query(EVENTS).filter_by(id=id_event).first()
    #     t = db.session.query(EVENTS).filter_by(id_base_event=id_base_event, id_user=id_user).first()
    else:
        t = db.session.query(EVENTS).filter_by(id_base_event=id_base_event, id_user=id_user).first()
    return t


def add_events(id_curent_user, event_name, caption, start_date, end_date, id_base_user=0, id_base_event=0):
    """Добавяет соревнование, на вход получает название,
     описание дату старта и дату окоончания"""
    create_date = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
    new_events = EVENTS(id_user=id_curent_user, event_name=event_name, start_date=start_date, end_date=end_date,
                        create_date=create_date, caption=caption, id_base_user=id_base_user,
                        id_base_event=id_base_event)
    db.session.add(new_events)
    db.session.commit()

    if id_base_user != 0 and id_base_event == 0:
        #Добавляем ид в кололку базового ид соревнования
        event = EVENTS.query.filter_by(id=new_events.id).first()
        event.id_base_event = new_events.id
        db.session.commit()
        # добаляем роль содателя соревнования для пользователя
        role_event = RoleEvents(id_event=new_events.id, id_user=id_curent_user, status="creator")
        db.session.add(role_event)
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


def id_reached_rank(EventsDataID):
    """Вычисляет выполненый разряд в состязании"""
    EvData = EventsData.query.filter_by(id=EventsDataID).first()
    ExData = ExerciseData.query.filter_by(EventsDataID=EventsDataID).first()
    # print(EvData.gun_player, EvData.sex_player)
    Ex = Exercise.query.filter_by(ExerciseID=EvData.ExerciseID).first().list_of_value()
    result = ExData.result_player
    if EvData.sex_player == "М":
        s = 0
    else:
        s = 1
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
    # print(db.session.query(Exercise.name_gun).filter_by(name=name).first()[0])
    return db.session.query(Exercise.name_gun).filter_by(name=name).first()[0]


def select_result(id):
    """Выводит результаты участника полные (вместе с данными о соревновании)"""
    t1 = db.session.query(ExerciseData).filter_by(EventsDataID=id).first()
    t2 = db.session.query(EventsData).filter_by(id=id).first()

    return t1, t2


def select_result_test(id_user):
    """Возвращиет json данных участника о соревновании"""
    t = db.session.query(EventsData.id, EventsData.name_player, EventsData.age_player, EventsData.sex_player,
                         EventsData.city_player, EventsData.organization_player, RankTable.name.label("rank_name"),
                         EVENTS.event_name.label("event_name"), EventsData.section_player, EventsData.result_player,
                         EventsData.reached_rank,
                         ExerciseData.ex1, ExerciseData.ex2, ExerciseData.ex3, ExerciseData.ex4, ExerciseData.ex5,
                         ExerciseData.ex6, ExerciseData.ex7, ExerciseData.ex8, ExerciseData.ex9, ExerciseData.ex10,
                         ExerciseData.tens_count)\
        .join(RankTable) \
        .join(EVENTS) \
        .join(ExerciseData) \
        .filter(RankTable.RankID == EventsData.RankID) \
        .filter(EventsData.id == id_user).first()
    # return json.dumps(t._asdict())
    return t


def select_checked(id_user, id_event):
    """Возвращает является ли ползователь редактором или создателем или нет (для активации селектора)"""
    t1 = db.session.query(RoleEvents).filter_by(id_event=id_event, id_user=id_user).first()
    # return t1.status if t1 else False
    if t1:
        return t1.status
    else:
        return False


def set_event_role(id_user, id_event, status):
    """меняет/ присваивает ролью пользователя в соревновании"""
    t = RoleEvents(id_event=id_event, id_user=id_user, status=status)
    t1 = db.session.query(RoleEvents).filter_by(id_event=id_event, id_user=id_user).first()
    if t1:
        t1.status = status
    else:
        db.session.add(t)
    db.session.commit()
    return True


def list_users_event(id_event, id_user):
    """возвращает таблицу пользователей которые причасны к оревнованию"""
    t = db.session.query(RoleEvents.status, USER.username, USER.email, USER.id)\
        .filter(RoleEvents.id_event == id_event) \
        .filter(RoleEvents.id_user == USER.id) \
        .filter(RoleEvents.status != "unregister") \
        .filter(RoleEvents.id_user != id_user) \
        .all()
    return t


def check_user_role_creator(id_user, id_event):
    """Проверяет является ли пользователь создателем соревнования"""
    if db.session.query(RoleEvents).filter_by(id_event=id_event, id_user=id_user).first():
        return True
    else:
        return False
