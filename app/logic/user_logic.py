from app.extensions import db
from app.models.user import USER
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

def admin_pg_db():
    # создает все таблицы
    print("Create_ALL")
    # Base.metadata.create_all(engine)
    #дропает все даблицы
    # Base.metadata.drop_all(engine)


def select_electro():
    # Выбор данных из БД
    return db.session.query(USER).order_by(USER.rank.desc())


def signup_query(username, email, password):
    user = USER.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database
    create_date = str(datetime.datetime.now())
    if user:# if a user is found, we want to redirect back to signup page so user can try again
        return 0

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    # print("test=",user, email,generate_password_hash(password, method='sha256'))
    new_user = USER(login=username, email=email, password_hash=generate_password_hash(password, method='sha256'), date_user_made=create_date)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return 1

def login(email, password):
    if 0:
        return 0
    else:
        return 1
