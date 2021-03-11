import email_validator

from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

# from wtforms import SubmitField, SelectField, DateField
from wtforms.fields.html5 import DateField


class AddEventMember(FlaskForm):
    # общее
    # имя игрока
    name_player = StringField('имя участника', validators=[DataRequired()])
    # пол
    sex_player = StringField('пол', validators=[DataRequired()])
    # возраст
    age_player = StringField('возраст', validators=[DataRequired()])
    # оружие
    gun_player = StringField('оружие', validators=[DataRequired()])
    # секция стрельбы пределать на exercise
    section_player = StringField('упражнение', validators=[DataRequired()])
    # очки
    # result_player = StringField('упражнение', validators=[DataRequired()])

    submit = SubmitField('Создать')

    # def validate_username(self, username):
    #     user = USER.query.filter_by(login=username.data).first()
    #     if user is not None:
    #         raise ValidationError('Please use a different username.')
    #
    # def validate_email(self, email):
    #     user = USER.query.filter_by(email=email.data).first()
    #     if user is not None:
    #         raise ValidationError('Please use a different email address.')
