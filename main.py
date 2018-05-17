from flask import Flask, session, url_for, request, jsonify
import hashlib
from random import randrange
from wrapperRpi3 import Prototype

app = Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.one_request = True
app.proto = None

@app.errorhandler(404)
def page_not_found():
    return jsonify(code_error=404, message='This action doesn\'t exist. Please, go to the documentation for help')

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


@app.route('/api/v1/move/w_left/<string:direction>')
@app.route('/api/v1/move/w_left/<string:direction>/<int:speed>')
def move_wLeft(direction='', speed=None):
    if direction == 'forward':
        if speed is None:
            app.proto.ForwardMotorA()
            return jsonify(message='Moving left motor - ' + direction)
        else:
            app.proto.ForwardMotorAwSpeed(speed)
            return jsonify(message='Moving left motor  - ' + direction + ' with speed ' + str(speed))
    elif direction == 'reverse':
        if speed is None:
            app.proto.ReverseMotorA()
            return jsonify(message='Moving left motor - ' + direction)
        else:
            app.proto.ReverseMotorAwSpeed(speed)
            return jsonify(message='Moving left motor  - ' + direction + ' with speed ' + str(speed))
    else:
        return jsonify(message='This action doesn\'t exist. Please, go to the documentation for help')


@app.route('/api/v1/move/w_right/<string:direction>')
@app.route('/api/v1/move/w_right/<string:direction>/<int:speed>')
def move_wRight(direction='', speed=None):
    if direction == 'forward':
        if speed is None:
            app.proto.ForwardMotorB()
            return jsonify(message='Moving right motor  - ' + direction)
        else:
            app.proto.ForwardMotorBwSpeed(speed)
            return jsonify(message='Moving right motor  - ' + direction + ' with speed ' + str(speed))
    elif direction == 'reverse':
        if speed is None:
            app.proto.ReverseMotorB()
            return jsonify(message='Moving right motor  - ' + direction)
        else:
            app.proto.ReverseMotorBwSpeed(speed)
            return jsonify(message='Moving right motor  - ' + direction + ' with speed ' + str(speed))
    else:
        return jsonify(message='This action doesn\'t exist. Please, go to the documentation for help')


@app.route('/api/v1/move/both/<string:direction>')
@app.route('/api/v1/move/both/<string:direction>/<int:speed>')
def move_wLeft(direction='', speed=None):
    if direction == 'forward':
        if speed is None:
            app.proto.ForwardBoth()
            return jsonify(message='Moving both motors  - ' + direction)
        else:
            app.proto.ForwardBothwSpeed(speed)
            return jsonify(message='Moving both motors  - ' + direction + ' with speed ' + str(speed))
    elif direction == 'reverse':
        if speed is None:
            app.proto.ReverseBoth()
            return jsonify(message='Moving both motors  - ' + direction)
        else:
            app.proto.ReverseBothwSpeed(speed)
            return jsonify(message='Moving both motors  - ' + direction + ' with speed ' + str(speed))
    else:
        return jsonify(message='This action doesn\'t exist. Please, go to the documentation for help')


@app.route('/api/v1/stop')
@app.route('/api/v1/stop/<motor>')
def stop(motor=None):
    if motor is None:
        app.proto.StopAll()
        return jsonify(message='Stopping both motors')
    elif motor == 'w_left':
        app.proto.StopMotorA()
        return jsonify(message='Stopping left motor')
    elif motor == 'w_right':
        app.proto.StopMotorB()
        return jsonify(message='Stopping right motor')
    else:
        return jsonify(message='This action doesn\'t exist. Please, go to the documentation for help')


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
