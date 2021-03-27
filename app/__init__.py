from flask import Flask
from flask_mail import Mail
from flask_security import Security, SQLAlchemyUserDatastore

from app.extensions import db, migrate, login_manager

from app.forms.login_form import ExtendedLoginForm, ExtendedRegisterForm

from app.models.user import USER, Role
from app.models.events import EVENTS
from app.models.basetable import BaseTable
from app.models.sextable import SexTable
from app.models.exercise import Exercise
from app.models.exercise_data import ExerciseData

from config import ConfigObject

from app.views.basic_view import basic_view


def create_app(config_object=ConfigObject):
    app = Flask(__name__)
    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)

    # app.run(host=HOST, port=PORT)
    app.run(host='192.168.0.100', port='9999', debug=True)
    # return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    Mail(app)

    user_datastore = SQLAlchemyUserDatastore(db, USER, Role)
    security = Security(app, user_datastore, login_form=ExtendedLoginForm, register_form=ExtendedRegisterForm)

    @security.context_processor
    def security_context_processor():
        return dict(title="Вход")

    @security.register_context_processor
    def security_register_processor():
        return dict(title="Регистрация")


def register_blueprints(app):
#     app.register_blueprint(indicators)
#     app.register_blueprint(upload)
    app.register_blueprint(basic_view)

