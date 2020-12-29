from flask import Blueprint, render_template, json, request
from flask import flash, redirect, url_for
# from config import indicatorsPath
from app.views.base_except_view import base_view_except
from app.forms.login_form import LoginForm, SignupForm

from app.logic.user_logic import signup_query

import requests

basic_view = Blueprint('basic_view', __name__, template_folder='templates')


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
def profile():
    username = "Vasya"
    return render_template('profile.html', title='Профиль', username=username)


@basic_view.route('/login', methods=['GET', 'POST'])
@base_view_except
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        return redirect(url_for('basic_view.index'))
    return render_template('login.html', title='Вход', form=form)

@basic_view.route('/logout')
@base_view_except
def logout():
    username = "Vasya"
    return render_template('index.html', title='Новости')


@basic_view.route('/signup', methods=['GET', 'POST'])
@base_view_except
def signup():
    form = SignupForm()

    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    print(username, email, password)

    if form.validate_on_submit():
        if 1 == signup_query(username, email, password):
            return redirect(url_for('basic_view.login'))
        elif 0 == signup_query(username, email, password):
            flash('Email address already exists')
            return render_template('signup.html', title='Регистрация', form=form)

    return render_template('signup.html', title='Регистрация', form=form)


@basic_view.route('/get_len', methods=['GET', 'POST'])
@base_view_except
def get_len():
    name = request.form['name']
    return json.dumps({'len': len(name)})
