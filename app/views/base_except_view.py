import datetime
from flask import abort
from functools import wraps
from jinja2 import TemplateNotFound


def base_view_except(f):
    # Базовый декоратор, отловщик исключений для views
    @wraps(f)
    def wraped():
        try:
            return f()
        except TemplateNotFound:
            fin = open("data/except_log.csv", 'a')
            fin.write(str(datetime.datetime.now()) + ";" + str(f.__name__) + "; TemplateNotFound\n")
            fin.close()
            abort(404, description="Resource not found")

    return wraped
