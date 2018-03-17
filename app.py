from flask import Flask, render_template, redirect, url_for, make_response, request
import json
from options import DEFAULTS

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', data=get_saved_data())


def get_saved_data():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data


@app.route('/save', methods=['POST'])
def save_form():
    data = get_saved_data()
    print(data)
    print(request.form.items())
    data.update(dict(request.form.items()))
    print(data)
    
    # we need to use this because of the cookies
    # otherwise return redirect would be enough
    response = make_response(redirect(url_for('builder')))
    response.set_cookie('character', json.dumps(data))
    return response


@app.route('/builder')
def builder():
    return render_template('builder.html', data=get_saved_data(), options=DEFAULTS)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=80)
