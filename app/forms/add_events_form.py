import email_validator

from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

# from wtforms import SubmitField, SelectField, DateField
from wtforms.fields.html5 import DateField
from app.models.user import USER


class AddEvent(FlaskForm):
    # общее
    # название соревнования
    name = StringField('Название соревнования', validators=[DataRequired()])
    # опсаине соревнования
    caption = StringField('Описание', validators=[DataRequired()])

    # состояния
    # start_date = StringField('Старт соревнования', validators=[DataRequired()])
    start_date = DateField('Start at', format='%Y-%m-%d')
    # end_date = StringField('end_date', validators=[DataRequired()])
    # registration_start = StringField('registration_start', validators=[DataRequired()])
    # registration_end = StringField('registration_end', validators=[DataRequired()])

    # Градации
    # по полам (м, ж , мж, not identification)
    # sex = StringField('Разделение по полу участника', validators=[DataRequired()])
    # по возрастам (группы возрастов или их отсутсвие)
    # age = StringField('age', validators=[DataRequired()])
    # по категориям разрядов (мс, кмс...)
    # category = StringField('category', validators=[DataRequired()])
    # по видам оружия(виды оружия)
    # gun = StringField('Виды оружия', validators=[DataRequired()])
    # по упражнениям (пп40, пп20...)
    # exercise = StringField('exercise', validators=[DataRequired()])

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
