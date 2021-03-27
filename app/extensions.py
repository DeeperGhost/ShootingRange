from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# from flask_security import Security, SQLAlchemyUserDatastore
# from app.models.user import USER, Role
# from app.forms.login_form import ExtendedLoginForm, ExtendedRegisterForm

db = SQLAlchemy()
migrate = Migrate()

login_manager = LoginManager()
login_manager.login_view = 'basic_view.login'


# security = Security()
# user_datastore = SQLAlchemyUserDatastore(db, USER, Role)
# security = Security(user_datastore, login_form=ExtendedLoginForm, register_form=ExtendedRegisterForm)