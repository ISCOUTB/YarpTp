from flask import Flask, session, url_for, request, jsonify
import hashlib
from random import randrange
from wYarpTp import Prototype

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
    if 'token' not in session and request.endpoint not in ['login']:
        return jsonify(code=200, message='You\'re unauthorized to perform this action. Please, Log in in the URL',
                       url=url_for('login'))


@app.route('/api/v1')
def index():
    if 'token' not in session:
        return jsonify(code=200, message='Welcome to the API. Please go to the URL to Log in', url=url_for('login'))
    else:
        return jsonify(code=200, message='Welcome to the API. Go to the documentation for help')


@app.route('/api/v1/login')
def login():
    if app.one_request:
        # Primer usuario
        session['token'] = hashlib.md5(str(randrange(2**15)).encode()).hexdigest()
        app.one_request = False
        app.proto = Prototype()
    if not app.one_request:
        try:
            return jsonify(code=200, token=session['token'])
        except KeyError:
            return jsonify(message='There\'s already a logged user')


@app.route('/api/v1/move/<string:motor>/<string:direction>')
@app.route('/api/v1/move/<string:motor>/<string:direction>/<float:time>')
@app.route('/api/v1/move/<string:motor>/<string:direction>/<int:speed>')
@app.route('/api/v1/move/<string:motor>/<string:direction>/<int:speed>/<float:time>')
def movement(motor, direction, speed, time):
    if motor == 'left' and direction == 'forward':
        pass
    elif motor == 'left' and direction == 'reverse':
        pass
    elif motor == 'right' and direction == 'forward':
        pass
    elif motor == 'right' and direction == 'reverse':
        pass
    elif motor == 'both' and direction == 'forward':
        pass
    elif motor == 'both' and direction == 'reverse':
        pass
    else:
        if motor not in ['left', 'right', 'both'] and direction in ['forward', 'reverse']:
            pass
        elif motor in ['left', 'right', 'both'] and direction not in ['forward', 'reverse']:
            pass
        else:
            pass


@app.route('/api/v1/stop')
@app.route('/api/v1/stop/<motor>')
def stop(motor=None):
    if motor is None:
        app.proto.StopAll()
        return jsonify(code=200, message='Stopping both motors')
    elif motor == 'w_left':
        app.proto.StopMotorA()
        return jsonify(code=200, message='Stopping left motor')
    elif motor == 'w_right':
        app.proto.StopMotorB()
        return jsonify(code=200, message='Stopping right motor')
    else:
        return jsonify(message='This action doesn\'t exist. Please, go to the documentation for help')


@app.route('/api/v1/logout')
def logout():
    if 'token' in session:
        # remove the username from the session if it's there
        app.one_request = True
        app.proto = None
        session.pop('token', None)
        return jsonify(code=200, message='You\'ve logged out')
    else:
        return jsonify(message='There\'s no logged user')


if __name__ == '__main__':
    app.run(host='0.0.0.0')


def execute(dir, sp, mot, tm=0):
    if dir == 'forward':
        if sp is None:
            if tm == 0:
                if mot == 'left':
                    # app.proto.ForwardMotorA()
                    return jsonify(message='Moving ' + mot + ' motor - ' + dir)
                elif mot == 'right':
                    # app.proto.ForwardMotorB()
                    return jsonify(message='Moving ' + mot + ' motor - ' + dir)
                else:
                    # app.proto.ForwardBoth()
                    return jsonify(message='Moving both motors  - ' + dir)
            else:
                if mot == 'left':
                    # app.proto.ForwardMotorA(tm)
                    return jsonify(message='Moving ' + mot + ' motor - ' + dir)
                elif mot == 'right':
                    # app.proto.ForwardMotorB(tm)
                    return jsonify(message='Moving ' + mot + ' motor - ' + dir)
                else:
                    # app.proto.ForwardBoth(tm)
                    return jsonify(message='Moving both motors  - ' + dir)
        else:
            if tm == 0:
                if mot == 'left':
                    # app.proto.ForwardMotorAwSpeed(speed)
                    return jsonify(message='Moving' + mot + 'motor  - ' + dir + ' with speed ' + str(sp))
                elif mot == 'right':
                    # app.proto.ForwardMotorBwSpeed(speed)
                    return jsonify(message='Moving' + mot + 'motor  - ' + dir + ' with speed ' + str(sp))
                else:
                    # app.proto.ForwardBothwSpeed(speed)
                    return jsonify(message='Moving both motors  - ' + dir + ' with speed ' + str(sp))
            else:
                if mot == 'left':
                    # app.proto.ForwardMotorAwSpeed(speed, tm)
                    return jsonify(message='Moving' + mot + 'motor  - ' + dir + ' with speed ' + str(sp))
                elif mot == 'right':
                    # app.proto.ForwardMotorBwSpeed(speed, tm)
                    return jsonify(message='Moving' + mot + 'motor  - ' + dir + ' with speed ' + str(sp))
                else:
                    # app.proto.ForwardBothwSpeed(speed, tm)
                    return jsonify(message='Moving both motors  - ' + dir + ' with speed ' + str(sp))
    elif dir == 'reverse':
        if sp is None:
            if tm == 0:
                if mot == 'left':
                    # app.proto.ReverseMotorA()
                    return jsonify(message='Moving ' + mot + ' motor - ' + dir)
                elif mot == 'right':
                    # app.proto.ReverseMotorB()
                    return jsonify(message='Moving ' + mot + ' motor - ' + dir)
                else:
                    # app.proto.ReverseBoth()
                    return jsonify(message='Moving both motors  - ' + dir)
            else:
                if mot == 'left':
                    # app.proto.ReverseMotorA(tm)
                    return jsonify(message='Moving ' + mot + ' motor - ' + dir)
                elif mot == 'right':
                    # app.proto.ReverseMotorB(tm)
                    return jsonify(message='Moving ' + mot + ' motor - ' + dir)
                else:
                    # app.proto.ReverseBoth(tm)
                    return jsonify(message='Moving both motors  - ' + dir)
        else:
            if tm == 0:
                if mot == 'left':
                    # app.proto.ReverseMotorAwSpeed(speed)
                    return jsonify(message='Moving' + mot + 'motor  - ' + dir + ' with speed ' + str(sp))
                elif mot == 'right':
                    # app.proto.ReverseMotorBwSpeed(speed)
                    return jsonify(message='Moving' + mot + 'motor  - ' + dir + ' with speed ' + str(sp))
                else:
                    # app.proto.ReverseBothwSpeed(speed)
                    return jsonify(message='Moving both motors  - ' + dir + ' with speed ' + str(sp))
            else:
                if mot == 'left':
                    # app.proto.ReverseMotorAwSpeed(speed, tm)
                    return jsonify(message='Moving' + mot + 'motor  - ' + dir + ' with speed ' + str(sp))
                elif mot == 'right':
                    # app.proto.ReverseMotorBwSpeed(speed, tm)
                    return jsonify(message='Moving' + mot + 'motor  - ' + dir + ' with speed ' + str(sp))
                else:
                    # app.proto.ReverseBothwSpeed(speed, tm)
                    return jsonify(message='Moving both motors  - ' + dir + ' with speed ' + str(sp))






