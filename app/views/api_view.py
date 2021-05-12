import json

from flask import jsonify
from flask import Blueprint
from flask import request
from flask_security import login_required, current_user

from app.logic.user_logic import set_event_role
from app.logic.user_logic import check_user_role_creator

api_view = Blueprint('api_view', __name__, template_folder='templates')


@api_view.route('/add_red')
# @base_view_except
@login_required
def add_red():
    # print(2+2)
    return jsonify(status="yes", category="error")


@api_view.route('/reg_role_user_event', methods=['POST'])
# @base_view_except
@login_required
def reg_role_user_event():
    request_data = request.get_json(force=True)
    value = "register" if request_data['value'] else "unregister"
    if set_event_role(id_user=request_data['id_user'], id_event=request_data['id'], status=value):
        return jsonify(status="done")
    else:
        return jsonify(status="denied", category="error")


@api_view.route('/add_role_event', methods=['POST'])
# @base_view_except
@login_required
def add_role_event():
    """Добавляет роль пользователя в соревновании
    дополнительно( удаляет соревнование личное если роль убирают или созадет если роль добавляется)"""
    from app.logic.user_logic import show_event, add_events, remove_event

    request_data = request.get_json(force=True)

    value = "user" if request_data['value'] else "register"
    # проверка на то что пользователь является создателем соревнования
    if check_user_role_creator(id_user=current_user.id, id_event=request_data['id_event']):
        if set_event_role(id_user=request_data['id_user'],
                          id_event=request_data['id_event'],
                          status=value):
            # убираем соревнование
            if value == "user":
                t = show_event(id_event=request_data['id_event'])
                add_events(id_curent_user=request_data['id_user'],
                           event_name=t.event_name, caption=t.caption, start_date=t.start_date, end_date=t.end_date,
                           id_base_user=current_user.id, id_base_event=request_data['id_event'])
            # добавляем соревнвоание
            else:
                t = show_event(id_base_event=request_data['id_event'], id_user=request_data['id_user'])
                remove_event(id_event=t.id)
            return jsonify(status="done")
        else:
            return jsonify(status="denied", category="error")
    else:
        return jsonify(status="denied", category="not login")


@api_view.route('/show_result/<int:id_user>', methods=['GET', 'POST'])
def show_result(id_user):
    """возвращает результаты участника для всплывающего окна"""
    from app.logic.user_logic import select_result_test, parametr_exercise
    t = select_result_test(id_user)

    entries, series = parametr_exercise(id_user)
    if t:
        t1 = t._asdict()
        t1['entries'] = entries/10
        t1['id_user'] = id_user
        return jsonify(t1)
    else:
        return jsonify(name_player=None, entries=entries/10, id_user=id_user)


@api_view.route('/edit_result/<int:id_user>', methods=['GET', 'POST'])
@login_required
def edit_result(id_user):
    """Ввоод и редактирование результатов участника в соревновании"""
    from app.logic.user_logic import set_exercise_data

    # t = select_result_test(id_user)
    #
    # entries, series = parametr_exercise(id_user)

    # request_data = request.get_json(force=True)
    rd = request.get_json(force=True)
    # set_exercise_data(request_data)
    print(rd['idUser'])
    print(rd)
    set_exercise_data(EventsDataID=rd['idUser'], ex1=rd['ex1'], ex2=rd['ex2'], ex3=rd['ex3'], ex4=rd['ex4'],
                      ex5=rd['ex5'], ex6=rd['ex6'], ex7=rd['ex7'], ex8=rd['ex8'], ex9=rd['ex9'], ex10=rd['ex10'],
                      tens_count=rd['tens'])
    # for i in request_data:
    #     print(request_data[i])
    return jsonify(status="done")

