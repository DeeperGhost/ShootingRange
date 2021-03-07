from flask import Flask

from app.extensions import db, migrate, login_manager
from app.models.user import USER
# from app.models.events import EVENTS

from config import ConfigObject

# from app.views.indicators import indicators
# from app.views.upload import upload
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


def register_blueprints(app):
#     app.register_blueprint(indicators)
#     app.register_blueprint(upload)
    app.register_blueprint(basic_view)

