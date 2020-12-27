from flask import Blueprint, render_template, json, request
from flask import flash, redirect, url_for
# from config import indicatorsPath
from app.views.base_except_view import base_view_except
from app.forms.login_form import LoginForm
import requests

basic_view = Blueprint('basic_view', __name__, template_folder='templates')


@basic_view.route('/', methods=['GET', 'POST'])
@basic_view.route('/index', methods=['GET', 'POST'])
@base_view_except
def index():
    hum = 10
    stri  = "https://api.openweathermap.org/data/2.5/weather?q=vladivostok&appid=4f700615ae41e5d6e83b562a95e7c16f&lang=ru"
    response = requests.get(stri)
    temp = json.loads(response.text)
    return render_template('index.html', hum= hum, temp=temp)


@basic_view.route('/about')
@base_view_except
def about():
    return render_template('about.html')


@basic_view.route('/login', methods=['GET', 'POST'])
@base_view_except
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))

        return redirect(url_for('basic_view.index'))
    return render_template('login.html', title='Sign In', form=form)


@basic_view.route('/signup')
@base_view_except
def signup():
    message = ''

    return render_template('signup.html')


@basic_view.route('/get_len', methods=['GET', 'POST'])
@base_view_except
def get_len():
    name = request.form['name']
    return json.dumps({'len': len(name)})



