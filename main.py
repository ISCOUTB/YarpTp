from flask import Flask, session, url_for, request, jsonify
import hashlib
from random import randrange
from wrapperRpi3 import Prototype

app = Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.one_request = True
app.proto = None


@app.before_request
def before_request():
    if 'token' in session and request.endpoint in ['login']:
        return jsonify(message='Ya estas logueado')
    if not 'token' in session and not request.endpoint in ['login']:
        return jsonify(message='You\'re unauthorized to perform this action. Please, Log in in the URL',
                url=url_for('login'))


@app.route('/api/v1')
def index():
    if 'token' not in session:
        return jsonify(message='Welcome to the API. Please go to the URL to Log in', url=url_for('login'))
    else:
        return jsonify(message='Welcome to the API. Go to the documentation for help')


@app.route('/api/v1/login')
def login():
    if app.one_request:
        # Primer usuario
        session['token'] = hashlib.md5(str(randrange(2**15)).encode()).hexdigest()
        app.one_request = False
        app.proto = Prototype()
    if not app.one_request:
        try:
            return jsonify(token=session['token'])
        except KeyError:
            return jsonify(message='Ya existe un usuario loggeado')


@app.route('/api/v1/random/<int:valor>')
def la_random(valor=0):
    if 'token' in session:
        return jsonify(val=valor)
    else:
        return jsonify(message='You\'re unauthorized to perform this action. Please, Log in in the URL',
                url=url_for('login'))


@app.route('/api/v1/move/w_left/<direction>')
@app.route('/api/v1/move/w_left/<direction>/<int:speed>')
def move_wLeft(direction='', speed=None):
    if direction == 'forward':
        if speed is None:
            app.proto.ForwardMotorA()
        else:
            app.proto.ForwardMotorAwSpeed(speed)
    elif direction == 'reverse':
        if speed is None:
            app.proto.ReverseMotorA()
        else:
            app.proto.ReverseMotorAwSpeed(speed)
    else:
        pass   # error


@app.route('/api/v1/move/w_right/<direction>')
@app.route('/api/v1/move/w_right/<direction>/<int:speed>')
def move_wRight(direction='', speed=None):
    if direction == 'forward':
        if speed is None:
            app.proto.ForwardMotorB()
        else:
            app.proto.ForwardMotorBwSpeed(speed)
    elif direction == 'reverse':
        if speed is None:
            app.proto.ReverseMotorB()
        else:
            app.proto.ReverseMotorBwSpeed(speed)
    else:
        pass  # error


@app.route('/api/v1/move/both/<direction>')
@app.route('/api/v1/move/both/<direction>/<int:speed>')
def move_wLeft(direction='', speed=None):
    if direction == 'forward':
        if speed is None:
            app.proto.ForwardBoth()
        else:
            app.proto.ForwardBothwSpeed(speed)
    elif direction == 'reverse':
        if speed is None:
            app.proto.ReverseBoth()
        else:
            app.proto.ReverseBothwSpeed(speed)
    else:
        pass  # error


@app.route('/api/v1/stop')
@app.route('/api/v1/stop/<motor>')
def stop(motor=None):
    if motor is None:
        app.proto.StopAll()
    elif motor == 'w_left':
        app.proto.StopMotorA()
    elif motor == 'w_right':
        app.proto.StopMotorB()
    else:
        pass  # error

@app.route('/api/v1/logout')
def logout():
    if 'token' in session:
        # remove the username from the session if it's there
        app.one_request = True
        session.pop('token', None)
        return jsonify(message='Ha cerrado sesion')
    else:
        return jsonify(message='No existe un usuario logueado')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
