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


@api_view.route('/get_json_data', methods=['POST'])
# @base_view_except
@login_required
def get_json_data():
    # print(2+2)
    request_data = request.get_json(force=True)
    # request_data = request.json
    print(request_data)
    # id = request_data['id']
    # value = request_data['value']
    # id_user = request_data['id_user']
    # print(id, value, id_user)


    value = "register" if request_data['value'] else "unregister"
    if set_event_role(id_user=request_data['id_user'], id_event=request_data['id'], status=value):
        return jsonify(status="done")
    else:
        return jsonify(status="denied", category="error")


@api_view.route('/add_role_event', methods=['POST'])
# @base_view_except
@login_required
def add_role_event():
    request_data = request.get_json(force=True)

    print(request_data)
    value = "user" if request_data['value'] else "register"

    if check_user_role_creator(id_user=current_user.id, id_event=request_data['id_event']):
        if set_event_role(id_user=request_data['id_user'],
                          id_event=request_data['id_event'],
                          status=value):
            return jsonify(status="done")
        else:
            return jsonify(status="denied", category="error")
    else:
        return jsonify(status="denied", category="not login")
