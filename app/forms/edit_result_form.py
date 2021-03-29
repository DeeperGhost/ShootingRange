from flask_wtf import FlaskForm

from wtforms.fields.html5 import IntegerField
from wtforms import SubmitField

from wtforms import FieldList, FormField
from wtforms.validators import ValidationError, DataRequired
from wtforms.validators import NumberRange
from wtforms.validators import InputRequired, Length


class ResultForm(FlaskForm):
    """Статическое поля для динамической формы DinamicResultForm"""
    result = IntegerField('результат',
                          validators=[NumberRange(min=0, max=100, message='Неверное значение')], default=0)


def input_res_func_form(entries):
    """Функция обертка для передачи параметра в динамическую форму"""
    class DinamicResultForm(FlaskForm):
        """Динамическая форма ввода результатов"""
        series = FieldList(FormField(ResultForm), min_entries=entries)
        tens_count = IntegerField('количество 10',
                                  validators=[NumberRange(min=0, max=100, message='Неверное количество 10 балов')],
                                  default=0)
        submit = SubmitField('Сохранить')
    form = DinamicResultForm()
    return form
