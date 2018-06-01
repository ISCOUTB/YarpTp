from flask import Flask, session, url_for, request, jsonify, redirect
import hashlib
from random import randrange
# from wrapperRpi3 import Prototype

app = Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.one_request = True


def execute(dir, sp, mot, tm=0):
    if dir == 'forward':
        if sp is None:
            if tm == 0:
                if mot == 'left':
                    # app.proto.ForwardMotorA()
                    return jsonify(code=200, message='Moving ' + mot + ' motor - ' + dir)
                elif mot == 'right':
                    # app.proto.ForwardMotorB()
                    return jsonify(code=200, message='Moving ' + mot + ' motor - ' + dir)
                else:
                    # app.proto.ForwardBoth()
                    return jsonify(code=200, message='Moving both motors  - ' + dir)
            else:
                if mot == 'left':
                    # app.proto.ForwardMotorA(tm)
                    return jsonify(code=200, message='Moving ' + mot + ' motor - ' + dir + ' during ' + str(tm) + ' seconds')
                elif mot == 'right':
                    # app.proto.ForwardMotorB(tm)
                    return jsonify(code=200, message='Moving ' + mot + ' motor - ' + dir + ' during ' + str(tm) + ' seconds')
                else:
                    # app.proto.ForwardBoth(tm)
                    return jsonify(code=200, message='Moving both motors  - ' + dir + ' during ' + str(tm) + ' seconds')
        else:
            if tm == 0:
                if mot == 'left':
                    # app.proto.ForwardMotorAwSpeed(speed)
                    return jsonify(code=200, message='Moving ' + mot + ' motor  - ' + dir + ' with speed ' + str(sp))
                elif mot == 'right':
                    # app.proto.ForwardMotorBwSpeed(speed)
                    return jsonify(code=200, message='Moving ' + mot + ' motor  - ' + dir + ' with speed ' + str(sp))
                else:
                    # app.proto.ForwardBothwSpeed(speed)
                    return jsonify(code=200, message='Moving both motors  - ' + dir + ' with speed ' + str(sp))
            else:
                if mot == 'left':
                    # app.proto.ForwardMotorAwSpeed(speed, tm)
                    return jsonify(code=200, message='Moving ' + mot + ' motor  - ' + dir + ' with speed ' + str(sp) + ' during ' + str(tm) + ' seconds')
                elif mot == 'right':
                    # app.proto.ForwardMotorBwSpeed(speed, tm)
                    return jsonify(code=200, message='Moving ' + mot + ' motor  - ' + dir + ' with speed ' + str(sp) + ' during ' + str(tm) + ' seconds')
                else:
                    # app.proto.ForwardBothwSpeed(speed, tm)
                    return jsonify(message='Moving both motors  - ' + dir + ' with speed ' + str(sp) + ' during ' + str(tm) + ' seconds')
    elif dir == 'reverse':
        if sp is None:
            if tm == 0:
                if mot == 'left':
                    # app.proto.ReverseMotorA()
                    return jsonify(code=200, message='Moving ' + mot + ' motor - ' + dir)
                elif mot == 'right':
                    # app.proto.ReverseMotorB()
                    return jsonify(code=200, message='Moving ' + mot + ' motor - ' + dir)
                else:
                    # app.proto.ReverseBoth()
                    return jsonify(code=200, message='Moving both motors  - ' + dir)
            else:
                if mot == 'left':
                    # app.proto.ReverseMotorA(tm)
                    return jsonify(code=200, message='Moving ' + mot + ' motor - ' + dir + ' during ' + str(tm) + ' seconds')
                elif mot == 'right':
                    # app.proto.ReverseMotorB(tm)
                    return jsonify(code=200, message='Moving ' + mot + ' motor - ' + dir + ' during ' + str(tm) + ' seconds')
                else:
                    # app.proto.ReverseBoth(tm)
                    return jsonify(code=200, message='Moving both motors  - ' + dir + ' during ' + str(tm) + ' seconds')
        else:
            if tm == 0:
                if mot == 'left':
                    # app.proto.ReverseMotorAwSpeed(speed)
                    return jsonify(code=200, message='Moving ' + mot + ' motor  - ' + dir + ' with speed ' + str(sp))
                elif mot == 'right':
                    # app.proto.ReverseMotorBwSpeed(speed)
                    return jsonify(code=200, message='Moving ' + mot + ' motor  - ' + dir + ' with speed ' + str(sp))
                else:
                    # app.proto.ReverseBothwSpeed(speed)
                    return jsonify(code=200, message='Moving both motors  - ' + dir + ' with speed ' + str(sp))
            else:
                if mot == 'left':
                    # app.proto.ReverseMotorAwSpeed(speed, tm)
                    return jsonify(code=200, message='Moving ' + mot + ' motor  - ' + dir + ' with speed ' + str(sp) + ' during ' + str(tm) + ' seconds')
                elif mot == 'right':
                    # app.proto.ReverseMotorBwSpeed(speed, tm)
                    return jsonify(code=200, message='Moving ' + mot + ' motor  - ' + dir + ' with speed ' + str(sp) + ' during ' + str(tm) + ' seconds')
                else:
                    # app.proto.ReverseBothwSpeed(speed, tm)
                    return jsonify(code=200, message='Moving both motors  - ' + dir + ' with speed ' + str(sp) + ' during ' + str(tm) + ' seconds')


@app.route('/')
def index_first():
    return redirect(url_for('index'))


@app.before_request
def before_request():
    if 'token' in session and request.endpoint in ['login']:
        return jsonify(code=403, message='Ya estas logueado')
    elif 'token' not in session and request.endpoint not in ['login', 'index_first']:
        return jsonify(code=401, message='You\'re unauthorized to perform this action. Please, Log in in the URL',
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
        #app.proto = Prototype()
    if not app.one_request:
        try:
            return jsonify(code=200, token=session['token'])
        except KeyError:
            return jsonify(code=403, message='There\'s already a logged user')


@app.route('/api/v1/move/<string:motor>/<string:direction>')
@app.route('/api/v1/move/<string:motor>/<string:direction>/<float:time>')
@app.route('/api/v1/move/<string:motor>/<string:direction>/<int:speed>')
@app.route('/api/v1/move/<string:motor>/<string:direction>/<int:speed>/<float:time>')
def movement(motor, direction, speed=None, time=0):
    if motor == 'left' and direction == 'forward':
        return execute(mot=motor, dir=direction, sp=speed, tm=time)
    elif motor == 'left' and direction == 'reverse':
        return execute(mot=motor, dir=direction, sp=speed, tm=time)
    elif motor == 'right' and direction == 'forward':
        return execute(mot=motor, dir=direction, sp=speed, tm=time)
    elif motor == 'right' and direction == 'reverse':
        return execute(mot=motor, dir=direction, sp=speed, tm=time)
    elif motor == 'both' and direction == 'forward':
        return execute(mot=motor, dir=direction, sp=speed, tm=time)
    elif motor == 'both' and direction == 'reverse':
        return execute(mot=motor, dir=direction, sp=speed, tm=time)
    else:
        if motor not in ['left', 'right', 'both'] and direction in ['forward', 'reverse']:
            return jsonify(code=400, message='You\'re using a wrong motor instruction. Please, go to the documentation for help')
        elif motor in ['left', 'right', 'both'] and direction not in ['forward', 'reverse']:
            return jsonify(code=400, message='You\'re using a wrong direction instruction. Please, go to the documentation for help')
        else:
            return jsonify(code=404, message='This action doesn\'t exist. Please, go to the documentation for help')


@app.route('/api/v1/stop')
@app.route('/api/v1/stop/<motor>')
def stop(motor=None):
    if motor is None:
        return jsonify(code=200, message='Stopping both motors')
    elif motor == 'left':
        return jsonify(code=200, message='Stopping left motor')
    elif motor == 'right':
        return jsonify(code=200, message='Stopping right motor')
    else:
        return jsonify(code=404, message='This action doesn\'t exist. Please, go to the documentation for help')


@app.route('/api/v1/logout')
def logout():
    if 'token' in session:
        # remove the username from the session if it's there
        app.one_request = True

        session.pop('token', None)
        return jsonify(code=200, message='You\'ve logged out')
    else:
        return jsonify(code=403, message='There\'s no logged user')


if __name__ == '__main__':
    app.run(host='0.0.0.0')