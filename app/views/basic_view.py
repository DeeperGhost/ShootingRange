import requests

from flask import Blueprint, render_template, json, request
from flask import flash, redirect, url_for

from flask_login import current_user, login_user, login_required
from flask_login import logout_user

from app.views.base_except_view import base_view_except
from app.forms.login_form import LoginForm, RegistrationForm
from app.forms.add_events_form import AddEvent
from app.forms.add_events_data_form import AddEventMember

from app.logic.user_logic import signup_query
from app.logic.user_logic import add_events, select_events, add_event_data, select_event_members
from app.logic.user_logic import select_event

from app.models.user import USER

import os
from flask import send_from_directory

from markupsafe import escape

basic_view = Blueprint('basic_view', __name__, template_folder='templates')


@basic_view.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(basic_view.static, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@basic_view.route('/', methods=['GET', 'POST'])
@basic_view.route('/index', methods=['GET', 'POST'])
@base_view_except
def index():
    stri  = "https://api.openweathermap.org/data/2.5/weather?q=vladivostok&appid=4f700615ae41e5d6e83b562a95e7c16f&lang=ru"
    response = requests.get(stri)
    temp = json.loads(response.text)
    return render_template('index.html', temp=temp, title='Новости')


@basic_view.route('/about')
@base_view_except
def about():
    return render_template('about.html', title='О нас')


@basic_view.route('/rating')
@base_view_except
def rating():
    return render_template('rating.html', title='Рейтинг')


@basic_view.route('/games')
@base_view_except
def games():
    table = select_events("all")
    # print(type(table))
    # for i in table:
    #     print(i[0].caption)
    return render_template('games.html', title='Соревнования', table=table)


@basic_view.route('/profile')
@base_view_except
@login_required
def profile():
    username = current_user.login
    table = select_events(str(current_user.id))
    # add_events(str(current_user.id))
    return render_template('profile.html', title='Профиль', username=username, table=table)


@basic_view.route('/event/<int:idevent>')
# @base_view_except
@login_required
def event(idevent):
    table = select_event_members(idevent)
    event_name = select_event(idevent).event_name
    # print(event_name)
    return render_template('eventmembers.html', title='Участники', event_name=event_name, id_event=idevent, table=table)



@basic_view.route('/addevent', methods=['GET', 'POST'])
@base_view_except
@login_required
def addevent():
    form = AddEvent()
    if form.validate_on_submit():
        add_events(id_curent_user=current_user.id, event_name=form.name.data,
                   caption=form.caption.data, start_date=form.start_date.data)
        return redirect(url_for('basic_view.profile'))

    # print(form.caption.data)

    return render_template('addevent.html', title='Профиль', form=form)


@basic_view.route('/addeventmember/<int:idevent>', methods=['GET', 'POST'])
# @base_view_except
@login_required
def addeventmember(idevent):
    form = AddEventMember()
    if form.validate_on_submit():
        add_event_data(id_event=idevent, name_player=form.name_player.data, sex_player=form.sex_player.data,
                       age_player=form.age_player.data, gun_player=form.gun_player.data,
                       section_player=form.section_player.data)
        # print()
        # add_event_data(id_event=42, name_player="Василий", sex_player="м",
        #                age_player="18", gun_player="пп", section_player="пп40")
        # add_events(id_curent_user=current_user.id, event_name=form.name.data,
        #            caption=form.caption.data, start_date=form.start_date.data)
        return redirect(url_for('basic_view.event', idevent=idevent))

    # print(form.caption.data)

    return render_template('addeventmember.html', title='Профиль', form=form)


@basic_view.route('/login', methods=['GET', 'POST'])
@base_view_except
def login():
    if current_user.is_authenticated:
        return redirect(url_for('basic_view.profile'))
    form = LoginForm()
    if form.validate_on_submit():
        user = USER.query.filter_by(email=form.email.data).first()
        # user = USER.query.filter_by(login=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('basic_view.login'))
        login_user(user)
        # login_user(user, remember=form.remember_me.data)
        return redirect(url_for('basic_view.profile'))
    return render_template('login.html', title='Вход', form=form)


@basic_view.route('/logout')
@base_view_except
def logout():
    logout_user()
    return render_template('index.html', title='Новости')


@basic_view.route('/signup', methods=['GET', 'POST'])
@base_view_except
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('basic_view.login'))
    form = RegistrationForm()
    if form.validate_on_submit():
        signup_query(username=form.username.data, email=form.email.data, password=form.password.data)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('basic_view.login'))
    return render_template('signup.html', title='Регистрация', form=form)
