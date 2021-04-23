import requests


from flask import jsonify
from datetime import date

from flask import Blueprint, render_template, json, request
from flask import flash, redirect, url_for

from flask_security import login_required, roles_required, roles_accepted
from flask_login import current_user, login_user


from app.views.base_except_view import base_view_except
from app.forms.login_form import LoginForm, RegistrationForm
from app.forms.login_form import ExtendedLoginForm
from app.forms.add_events_form import AddEvent
from app.forms.add_events_data_form import AddEventMember
# from app.forms.edit_result_form import EditResult
from app.forms.edit_result_form import input_res_func_form

from app.logic.admin_logic import rankList, sexlist, shortCaptionList, gunList, exercise_list
from app.logic.admin_logic import create_exercise_table
from app.logic.admin_logic import create_sextable
from app.logic.admin_logic import create_basetable
from app.logic.admin_logic import create_rank_table
from app.logic.admin_logic import add_roles
from app.logic.admin_logic import lst_users_roles
from app.logic.admin_logic import delete_user


from app.logic.user_logic import add_events, select_events, add_event_data, select_event_members
from app.logic.user_logic import select_event, remove_event, remove_event_data
from app.logic.user_logic import parametr_exercise, _id_exercise_by_name, _gun_exercise_by_name
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
    """стартовая страница с новостями"""
    # прогноз погоды владивосток
    # stri  = "https://api.openweathermap.org/data/2.5/weather?q=vladivostok&appid=4f700615ae41e5d6e83b562a95e7c16f&lang=ru"
    # response = requests.get(stri)
    # temp = json.loads(response.text)
    # print(temp)
    posts=[{"title":"Title1", "Text":"Text1"}, {"title":"Title2", "Text":"Text2"}]

    return render_template('index.html', posts=posts, title='Новости')


# вкладка about на данный момент пустая
@basic_view.route('/about')
# @base_view_except
def about():
    return render_template('about.html', title='О нас')


# вкладка рейтинг на данный момент пустая (неясна надобность ее)
@basic_view.route('/rating')
@roles_required('admin')
# @base_view_except
def rating():
    return render_template('rating.html', title='Рейтинг')


@basic_view.route('/games')
@base_view_except
def games():
    """Вкладка игры-соревнования отображает видимые для всех списки соревнований а, также результаты"""
    if current_user.is_authenticated:
        table = select_events(id_current_user=current_user.id)
    else:
        table = select_events()
    return render_template('games.html', title='Соревнования', table=table)


# вкладка профиль позволяет добавлять соревновани и дает ссылку на редактироване непосредственно сами соревнования
@basic_view.route('/profile')
@base_view_except
@login_required
def profile():
    # username = current_user.login
    username = current_user.username
    table = select_events(id_current_user=current_user.id, lk=True)
    # add_events(str(current_user.id))
    return render_template('profile.html', title='Профиль', username=username, table=table)


# редактируем непосредственно соревнование из доступна профиля
@basic_view.route('/event/<int:idevent>', methods=['GET', 'POST'])
# @base_view_except
@login_required
def event(idevent):
    table = select_event_members(idevent, all=False)
    event_name = select_event(idevent).event_name

    # print(current_user.get_id(), 'id')
    # print(idevent, 'id')
    # print(event_name)

    form = AddEventMember()
    if form.validate_on_submit():
        exercise_id = _id_exercise_by_name(form.section_player.data)
        gun_name = _gun_exercise_by_name(form.section_player.data)
        add_event_data(id_event=idevent, ExerciseID=exercise_id, RankID=form.rank_player.data,
                       name_player=form.name_player.data, sex_player=form.sex_player.data,
                       age_player=form.age_player.data, gun_player=gun_name,
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

        exercise_id = _id_exercise_by_name(form.section_player.data)
        gun_name = _gun_exercise_by_name(form.section_player.data)

        add_event_data(id_event=idevent, ExerciseID=exercise_id, RankID=form.rank_player.data,
                       name_player=form.name_player.data, sex_player=form.sex_player.data,
                       age_player=form.age_player.data, gun_player=gun_name,
                       section_player=form.section_player.data, city_player=form.city_player.data,
                       organization_player=form.organization_player.data)
        return redirect(url_for('basic_view.event', idevent=idevent))

    return render_template('eventmembers.html', title='Участники', event_name=event_name, id_event=idevent,
                           table=table, form=form)


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
                   caption=form.caption.data, start_date=form.start_date.data, end_date=form.end_date.data,
                   id_base_user=current_user.id)
        return redirect(url_for('basic_view.profile'))

    # print(form.caption.data)

    return render_template('addevent.html', title='Профиль', form=form)


# Форма внесения результатов соревнования участника
@basic_view.route('/editresult/<int:iduser>/<int:idevent>', methods=['GET', 'POST'])
# @base_view_except
@login_required
def editresult(iduser, idevent):
    """View внесения результатов участника"""
    entries, series = parametr_exercise(iduser)

    # Функция обертка для передачи параметра в динамическую форму
    form = input_res_func_form(entries=entries/10)
    if form.validate_on_submit():
        lst_ex = []
        for i in form.series.entries:
            pass
            lst_ex.append(i.data['result'])
        while len(lst_ex) < 10:
            lst_ex.append(0)

        set_exercise_data(EventsDataID=iduser, ex1=lst_ex[0], ex2=lst_ex[1], ex3=lst_ex[2], ex4=lst_ex[3],
                          ex5=lst_ex[4], ex6=lst_ex[5], ex7=lst_ex[6], ex8=lst_ex[7], ex9=lst_ex[8], ex10=lst_ex[9],
                          tens_count=form.tens_count.data)

        return redirect(url_for('basic_view.event', idevent=idevent))
    return render_template('editresult.html', title='внести данные', form=form, series=series)


# @basic_view.route('/result/<int:id>')
# # @base_view_except
# def result(id):
#     """View вывода результатов участника
#     -требуются доработки"""
#     t1, t2 = select_result(id)
#     entries, series = parametr_exercise(id)
#     # t3 = str(t1).split(',')
#     # # for i in t3:
#     # #     print(i)
#     # print(entries,series)
#     return render_template('result.html', title='резултат', t1=t1,t2=t2)


@basic_view.route('/eventedit/<int:id>')
def event_edit(id):
    """View редактироваиня соревнвание"""
    from app.logic.user_logic import list_users_event
    table_users = list_users_event(id_event=id, id_user=current_user.id)

    return render_template('eventedit.html', title='редактирование', table=table_users, id_event=id)


@basic_view.route('/admin')
# @base_view_except
@roles_accepted('admin')
def admin():
    """View админской панели"""
    # список зарегестрированых пользователей с ролями
    lst_users = lst_users_roles()

    return render_template('admin.html', title='Admin panel', lst_users=lst_users)


@basic_view.route('/do_any')
# @base_view_except
@roles_accepted('admin')
def do_any():
    """функция для тестирвоания промежуточных функций админ панели"""
    # заполнить справочник с полами
    # create_sextable()
    # заролнить справочник базовой таблицы из министерства
    # create_basetable()
    # rankList()
    # create_exercise_table()
    # create_rank_table()
    add_roles()
    # remove_event(64)

    return render_template('admin.html', title='Admin panel2')


@basic_view.route('/del_user/<int:id>')
# @base_view_except
@roles_accepted('admin')
def del_user(id):
    """удалить пользователя"""
    delete_user(id)
    lst_users = lst_users_roles()
    return render_template('admin.html', title='Admin panel', lst_users=lst_users)


# ссылки с административными действиями
@basic_view.route('/test')
@base_view_except
def test():
    # заполнить справочник с полами
    # create_sextable()
    # заролнить справочник базовой таблицы из министерства
    # create_basetable()
    # rankList()
    # create_exercise_table()
    # create_rank_table()

    return jsonify(    {
        "username": "admin",
        "email": "admin@localhost",
        "id": 42
    })
