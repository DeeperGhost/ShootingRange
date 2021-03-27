# from flask_login import UserMixin
from flask_security import RoleMixin, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db
from app.extensions import login_manager


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return USER.query.get(int(user_id))

# Define models
# roles_users = db.Table('roles_users',
#                        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
#                        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class USER(UserMixin, db.Model):
    # структура данных пользователей
    __tablename__ = 'USERS'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())

    login = db.Column(db.String, nullable=True, unique=True)
    password_hash = db.Column(db.String, nullable=True)

    date_user_made = db.Column(db.String, nullable=True)

    family = db.Column(db.String, nullable=True)
    name = db.Column(db.String, nullable=True)
    second_name = db.Column(db.String, nullable=True)

    individual_key = db.Column(db.String, nullable=True)
    information = db.Column(db.String, nullable=True)

    rank = db.Column(db.Integer, nullable=True)

    events = db.relationship('EVENTS', backref='author', lazy='dynamic')

    roles = db.relationship('Role', secondary='roles_users',
                            backref=db.backref('users', lazy='dynamic'))

    # def __init__(self, login, email, password, date_user_made):
    #     self.login = login
    #     self.email = email
    #     self.password = password
    #     self.date_user_made = date_user_made

    def __repr__(self):
        return '%d, %s, %s, %s' % (self.id, self.login, self.email, self.password_hash)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('USERS.id'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id'))