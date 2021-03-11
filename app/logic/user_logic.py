from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db
from app.models.user import USER
from app.models.events import EVENTS
from app.models.events_data import EventsData


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
    return db.session.query(EventsData).order_by(EventsData.id.desc()).filter_by(id_event=id_event).all()


def add_events(id_curent_user, event_name, caption, start_date):
    create_date = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
    new_events = EVENTS(id_user=id_curent_user, event_name=event_name, start_date=start_date,
                        create_date=create_date, caption=caption)
    db.session.add(new_events)
    db.session.commit()


def add_event_data(id_event, name_player, sex_player, age_player, gun_player, section_player):
    # create_date = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
    new_events_data = EventsData(id_event=id_event, name_player=name_player, sex_player=sex_player,
                                 age_player=age_player, gun_player=gun_player, section_player=section_player)
    db.session.add(new_events_data)
    db.session.commit()


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
