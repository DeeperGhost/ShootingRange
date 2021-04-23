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

    print(request_data)
    value = "user" if request_data['value'] else "register"
    print(value)
    # проверка на то что пользователь является создателем соревнования
    if check_user_role_creator(id_user=current_user.id, id_event=request_data['id_event']):
        if set_event_role(id_user=request_data['id_user'],
                          id_event=request_data['id_event'],
                          status=value):
            # убираем соревнование
            if value == "user":
                t = show_event(id_event=request_data['id_event'])
                # print(t.id, t.event_name, t.caption, t.start_date, t.end_date)
                # pass

                add_events(id_curent_user=request_data['id_user'],
                           event_name=t.event_name, caption=t.caption, start_date=t.start_date, end_date=t.end_date,
                           id_base_user=current_user.id, id_base_event=request_data['id_event'])
            # добавляем соревнвоание
            else:

                t = show_event(id_base_event=request_data['id_event'], id_user=request_data['id_user'])
                # t = show_event(id_base_event=request_data['id_event'], id_user=33)
                print(t.id)
                remove_event(id_event=t.id)

            return jsonify(status="done")
        else:
            return jsonify(status="denied", category="error")
    else:
        return jsonify(status="denied", category="not login")


@api_view.route('/show_result/<int:id_user>', methods=['GET', 'POST'])
def show_result(id_user):
    """возвращает результаты участника для всплывающего окна"""
    from app.logic.user_logic import select_result_test
    t = select_result_test(id_user)

    return jsonify(t._asdict())

