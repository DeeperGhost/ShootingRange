import requests
from datetime import date

from flask import Blueprint, render_template, json, request
from flask import flash, redirect, url_for

from flask_login import current_user, login_user, login_required
from flask_login import logout_user

from app.views.base_except_view import base_view_except
from app.forms.login_form import LoginForm, RegistrationForm
from app.forms.add_events_form import AddEvent
from app.forms.add_events_data_form import AddEventMember
# from app.forms.edit_result_form import EditResult
from app.forms.edit_result_form import cont_f

from app.logic.admin_logic import rankList, sexlist, shortCaptionList, gunList, exercise_list
from app.logic.admin_logic import create_exercise_table
from app.logic.admin_logic import create_sextable
from app.logic.admin_logic import create_basetable
from app.logic.admin_logic import create_rank_table

from app.logic.user_logic import signup_query
from app.logic.user_logic import add_events, select_events, add_event_data, select_event_members
from app.logic.user_logic import select_event, remove_event, remove_event_data
from app.logic.user_logic import parametr_exercise, parametr_exercise2
from app.logic.user_logic import set_exercise_data
from app.logic.user_logic import select_result

from app.models.user import USER

import os
from flask import send_from_directory

from markupsafe import escape

basic_view = Blueprint('basic_view', __name__, template_folder='templates')

# картинка листика клевера в закладке
@basic_view.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(basic_view.static, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


# index view на данный отображает json прогноза погоды (поменять на ленту новостей)
@basic_view.route('/', methods=['GET', 'POST'])
@basic_view.route('/index', methods=['GET', 'POST'])
@base_view_except
def index():
    stri  = "https://api.openweathermap.org/data/2.5/weather?q=vladivostok&appid=4f700615ae41e5d6e83b562a95e7c16f&lang=ru"
    response = requests.get(stri)
    temp = json.loads(response.text)
    return render_template('index.html', temp=temp, title='Новости')


# вкладка about на данный момент пустая
@basic_view.route('/about')
@base_view_except
def about():
    return render_template('about.html', title='О нас')


# вкладка рейтинг на данный момент пустая (неясна надобность ее)
@basic_view.route('/rating')
@base_view_except
def rating():
    return render_template('rating.html', title='Рейтинг')


# Вкладка игры-соревнования отображает видимые для всех списки соревнований а, также результаты
@basic_view.route('/games')
@base_view_except
def games():
    table = select_events("all")
    # print(type(table))
    # for i in table:
    #     print(i[0].caption)
    return render_template('games.html', title='Соревнования', table=table)


# вкладка профиль позволяет добавлять соревновани и дает ссылку на редактироване непосредственно сами соревнования
@basic_view.route('/profile')
@base_view_except
@login_required
def profile():
    username = current_user.login
    table = select_events(str(current_user.id))
    # add_events(str(current_user.id))
    return render_template('profile.html', title='Профиль', username=username, table=table)


# редактируем непосредственно соревнование из доступна профиля
@basic_view.route('/event/<int:idevent>', methods=['GET', 'POST'])
# @base_view_except
@login_required
def event(idevent):
    table = select_event_members(idevent)
    event_name = select_event(idevent).event_name
    # print(event_name)

    form = AddEventMember()
    if form.validate_on_submit():
        exID = parametr_exercise2(form.section_player.data)
        add_event_data(id_event=idevent, ExerciseID=exID, RankID=form.rank_player.data,
                       name_player=form.name_player.data, sex_player=form.sex_player.data,
                       age_player=form.age_player.data, gun_player="GUN",
                       section_player=form.section_player.data, city_player=form.city_player.data,
                       organization_player=form.organization_player.data)
        return redirect(url_for('basic_view.event', idevent=idevent))

    return render_template('eventmembers.html', title='Участники', event_name=event_name, id_event=idevent, table=table, form=form)


# вью для просмотра незалогинеными пользователями соревнований (исправить после добавления уровней доступа пользователей)
@basic_view.route('/eventforall/<int:idevent>', methods=['GET', 'POST'])
# @base_view_except
# @login_required
def eventforall(idevent):
    table = select_event_members(idevent)

    event_name = select_event(idevent).event_name
    # print(event_name)
    return render_template('eventmembersall.html', title='Участники', event_name=event_name, table=table)


# вью удаление соревнования вместе с его участниками
@basic_view.route('/eventremove/<int:idevent>', methods=['GET', 'POST'])
# @base_view_except
@login_required
def eventremove(idevent):
    # функция из юзер логик удаление соревнования вместе с его участниками по ид соревнования
    remove_event(id_event=idevent)
    username = current_user.login
    table = select_events(str(current_user.id))
    return render_template('profile.html', title='Профиль', username=username, table=table)


#вью для редактирования участников соревнования
@basic_view.route('/eventdataremove/<int:iduser>/<int:idevent>', methods=['GET', 'POST'])
# @base_view_except
@login_required
# передаем из шаблона id пользователя и id соревнования
def eventdataremove(iduser, idevent):
    remove_event_data(id_user=iduser)

    table = select_event_members(idevent)
    event_name = select_event(idevent).event_name
    # username = current_user.login
    # table = select_events(str(current_user.id))
    form = AddEventMember()
    if form.validate_on_submit():
        exID = parametr_exercise2(form.section_player.data)
        add_event_data(id_event=idevent, ExerciseID=exID, RankID=form.rank_player.data,
                       name_player=form.name_player.data, sex_player=form.sex_player.data,
                       age_player=form.age_player.data, gun_player="GUN",
                       section_player=form.section_player.data, city_player=form.city_player.data,
                       organization_player=form.organization_player.data)
        return redirect(url_for('basic_view.event', idevent=idevent))

    return render_template('eventmembers.html', title='Участники', event_name=event_name, id_event=idevent, table=table, form=form)


# вью длля добавления соревнования из профиля
@basic_view.route('/addevent', methods=['GET', 'POST'])
@base_view_except
@login_required
def addevent():
    form = AddEvent()
    if form.validate_on_submit():
        # d = date.fromisoformat(form.start_date.data)
        # print(form.start_date.data.strftime('%d.%m.%Y'))
        add_events(id_curent_user=current_user.id, event_name=form.name.data,
                   caption=form.caption.data, start_date=form.start_date.data)
        return redirect(url_for('basic_view.profile'))

    # print(form.caption.data)

    return render_template('addevent.html', title='Профиль', form=form)


# вью для логина
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


# вью выход из пользователя
@basic_view.route('/logout')
@base_view_except
def logout():
    logout_user()
    return render_template('index.html', title='Новости')


# регистрация пользователя
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


# Форма внесения результатов соревнования участника
@basic_view.route('/editresult/<int:iduser>/<int:idevent>', methods=['GET', 'POST'])
# @base_view_except
@login_required
def editresult(iduser, idevent):

    entries, series = parametr_exercise(iduser)
    # print(entries, series)
    form = cont_f(entries=entries/10)
    if form.validate_on_submit():
        lst_ex = []
        for i in form.series.entries:
            pass
            lst_ex.append(i.data['result'])
            # print(i.data['result'])
        while len(lst_ex) < 10:
            lst_ex.append(0)
        # print(lst_ex)
        # print(len(lst_ex))

        set_exercise_data(EventsDataID=iduser, ex1=lst_ex[0], ex2=lst_ex[1], ex3=lst_ex[2], ex4=lst_ex[3],
                          ex5=lst_ex[4], ex6=lst_ex[5], ex7=lst_ex[6], ex8=lst_ex[7], ex9=lst_ex[8], ex10=lst_ex[9],
                          tens_count=form.tens_count.data)

        # return redirect(url_for('basic_view.event', idevent=idevent))
        return redirect(url_for('basic_view.event', idevent=idevent))

    return render_template('editresult.html', title='внести данные', form=form, series=series)

# показывает результаты участника
@basic_view.route('/result/<int:id>')
# @base_view_except
def result(id):
    t1, t2 = select_result(id)
    entries, series = parametr_exercise(id)
    # t3 = str(t1).split(',')
    # # for i in t3:
    # #     print(i)
    # print(entries,series)
    return render_template('result.html', title='резултат', t1=t1,t2=t2)


# ссылки с административными действиями
@basic_view.route('/addsextable')
@base_view_except
def admin():
    # заполнить справочник с полами
    # create_sextable()
    # заролнить справочник базовой таблицы из министерства
    # create_basetable()
    # rankList()
    # create_exercise_table()
    # create_rank_table()

    return render_template('about.html', title='О нас')
