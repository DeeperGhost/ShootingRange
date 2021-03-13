import email_validator

from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

# from wtforms import SubmitField, SelectField, DateField
from wtforms.fields.html5 import DateField

from app.logic.admin_logic import sexlist


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

    def __init__(self):
        super(AddEventMember, self).__init__()
        self.sex_player.choices = [(c.name, c.name_full) for c in sexlist()]


    # возраст
    age_player = DateField('возраст', format='%Y-%m-%d')
    # оружие
    # gun_player = StringField('оружие', validators=[DataRequired()])
    gun_player = SelectField('оружие', choices=[("ПП", "пневматический пистолет"),
                                                      ("МП", "стандартный малокалиберный пистолет"),
                                                      ("ППП", "скорострельный пневматический пистолет"),
                                                      ("МПП","произвольный малокалиберный пистолет"),
                                                      ("КП","крупнокалиберный пистолет или револьвер"),
                                                      ("ВП","пневматическая винтовка"),
                                                      ("ВП/ДМ","пневматическая винтовка (по движущейся мишени)"),
                                                      ("МВ","малокалиберная винтовка"),
                                                      ("КВ","крупнокалиберная винтовка"),
                                                      ("КВС","крупнокалиберная винтовка (скоростная стрельба)"),
                                                      ("КВП","произвольная крупнокалиберная винтовка")])


    # секция стрельбы пределать на exercise
    # section_player = StringField('упражнение', validators=[DataRequired()])
    section_player = SelectField('упражнение', choices=[("20", "20-выстрелов"),
                                                        ("30", "30-выстрелов"),
                                                        ("40", "40-выстрелов"),
                                                        ("50", "50-выстрелов"),
                                                        ("60", "60-выстрелов"),
                                                        ("5", "5 выстрелов"),
                                                        ("3*20", "3*20-выстрелов"),
                                                        ("2*40", "2*40-выстрелов")])

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
