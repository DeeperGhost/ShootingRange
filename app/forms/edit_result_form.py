from flask_wtf import FlaskForm

from wtforms.fields.html5 import IntegerField
from wtforms import SubmitField

from wtforms import FieldList, FormField
from wtforms.validators import ValidationError, DataRequired

# class EditResult(FlaskForm):
#     tens_count = IntegerField(label="Количество 10")
#     submit = SubmitField('Создать')


class LocationForm(FlaskForm):
    result = IntegerField('results', validators=[DataRequired()])


class CompanyForm(FlaskForm):
    series = FieldList(FormField(LocationForm), min_entries=5)
    tens_count = IntegerField('количество 10', validators=[DataRequired()])

    submit2 = SubmitField('Сохранить1')


def cont_f(entries):

    class DinamicResultForm(FlaskForm):
        series = FieldList(FormField(LocationForm), min_entries=entries)
        tens_count = IntegerField('количество 10')

        submit2 = SubmitField('Сохранить')

    form = DinamicResultForm()
    return form
