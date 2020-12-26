# # setings POSTGRESQL
POSTGRES_URL = "127.0.0.1:5432"
POSTGRES_USER = "postgres"
POSTGRES_PW = "007"
POSTGRES_DB = "ShootingRange"

# # setings flask server
HOST = '192.168.0.100'
PORT = 9999

#
# # setings data Save path
# indicatorsPath = "C:/Users/007/PycharmProjects/FlaskServTest/data/indicators.i"
# pathWork = "E:/FromTelephon/"
# # pathWork = "C:/Users/007/PycharmProjects/FlaskServTest/data/"           #Test space
#
class ConfigObject(object):
    # SERVER_NAME = '192.168.0.100:9999'

    DEBUG = True
    DEVELOPMENT = True

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:007@localhost/ShootingRange'
    SECRET_KEY = "SECRET_KEY"
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = "simple"  # Can be "memcached", "redis", etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

