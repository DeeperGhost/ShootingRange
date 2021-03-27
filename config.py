from paswords import mail_pass
from paswords import security_password_salt
from paswords import postress_pw
from paswords import secret_key

# # setings POSTGRESQL
POSTGRES_URL = "127.0.0.1:5432"
POSTGRES_USER = "postgres"
POSTGRES_PW = postress_pw
POSTGRES_DB = "ShootingRange"

# # setings flask server
HOST = '192.168.0.100'
PORT = 9999


class ConfigObject(object):
    DEBUG = False
    DEVELOPMENT = True

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:007@localhost/ShootingRange'
    SECRET_KEY = secret_key
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = "simple"  # Can be "memcached", "redis", etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    SECURITY_REGISTERABLE = True
    SECURITY_REGISTER_URL = '/create_account'
    SECURITY_PASSWORD_SALT = security_password_salt

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'VShootingRange@gmail.com'
    MAIL_PASSWORD = mail_pass
