import requests

from flask import Blueprint, render_template, json, request
from flask import flash, redirect, url_for

from flask_login import current_user, login_user, login_required
from flask_login import logout_user

from app.views.base_except_view import base_view_except
from app.forms.login_form import LoginForm, RegistrationForm
from app.logic.user_logic import signup_query
from app.models.user import USER

import os
from flask import send_from_directory

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
    return render_template('games.html', title='Соревнования')


@basic_view.route('/profile')
@base_view_except
@login_required
def profile():
    username = str(current_user.id) + current_user.login
    return render_template('profile.html', title='Профиль', username=username)


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
