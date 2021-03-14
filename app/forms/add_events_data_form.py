import email_validator

from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

# from wtforms import SubmitField, SelectField, DateField
from wtforms.fields.html5 import DateField

from app.logic.admin_logic import sexlist
from app.logic.admin_logic import shortCaptionList
from app.logic.admin_logic import gunList


class AddEventMember(FlaskForm):
    # общее
    # имя игрока
    name_player = StringField('имя участника', validators=[DataRequired()])
    # город участника
    city_player = StringField('город', validators=[DataRequired()])
    # организация участника
    organization_player = StringField('организация', validators=[DataRequired()])
    # пол
    # sex_player = SelectField('пол', choices=[("М", "М"), ("Ж", "Ж")])
    sex_player = SelectField()

    # возраст
    age_player = DateField('возраст', format='%Y-%m-%d')
    # оружие
    # gun_player = StringField('оружие', validators=[DataRequired()])
    gun_player = SelectField()

    # секция стрельбы пределать на exercise
    section_player = SelectField()

    # очки
    # result_player = StringField('упражнение', validators=[DataRequired()])

    submit = SubmitField('Создать')

    def __init__(self):
        super(AddEventMember, self).__init__()
        self.sex_player.choices = [(c.name, c.name_full) for c in sexlist()]
        self.section_player.choices = [(c[0], c[0]) for c in shortCaptionList()]
        self.gun_player.choices = [(c[0], c[1]) for c in gunList()]
