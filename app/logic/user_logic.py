from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db
from app.models.user import USER
from app.models.events import EVENTS


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
        return db.session.query(EVENTS).order_by(EVENTS.rank.desc()).all()
        # return db.session.query(EVENTS).order_by(EVENTS.rank.desc()).filter_by(id_user=id_user)
    else:
        return db.session.query(EVENTS).order_by(EVENTS.rank.desc()).filter_by(id_user=id_user).all()
    # return t


def add_events(id_curent_user, event_name, caption, start_date):
    create_date = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
    new_events = EVENTS(id_user=id_curent_user, event_name=event_name, start_date=start_date,
                        create_date=create_date, caption=caption)
    db.session.add(new_events)
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
