from flask import Blueprint, render_template, json, request
# from config import indicatorsPath
from app.views.base_except_view import base_view_except


basic_view = Blueprint('basic_view', __name__, template_folder='templates')


@basic_view.route('/', methods=['GET', 'POST'])
@base_view_except
def index():
    # f = open(indicatorsPath, 'r')
    # indicator = f.readline()
    # f.close()

    hum = 10
    temp = 100
    return render_template('index.html', hum= hum, temp= temp)

@basic_view.route('/about')
@base_view_except
def about():
    return render_template('about.html')


@basic_view.route('/test')
@base_view_except
def test(name=None):
    return render_template('test.html', name=name)


@basic_view.route('/get_len', methods=['GET', 'POST'])
@base_view_except
def get_len():
    name = request.form['name'];
    return json.dumps({'len': len(name)})

