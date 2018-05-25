from flask import Flask, session, jsonify
from flask_restplus import Resource, Api, reqparse
from random import randrange
import hashlib
# from wrapperRpi3 import Prototype

app = Flask(__name__)
api = Api(app)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.one_request = True
# app.proto = None

token_arg = reqparse.RequestParser()
token_arg.add_argument('word', type=str, required=True)


def validate(tok):
    if tok == session['token']:
        return True
    else:
        return False


@api.route('/api/v1/login')
class Login(Resource):
    def get(self):
        if app.one_request:
            # Primer usuario
            session['token'] = hashlib.md5(str(randrange(2**15)).encode()).hexdigest()
            app.one_request = False
            # app.proto = Prototype()
        if not app.one_request:
            try:
                return jsonify(code=200, token=session['token'])
            except KeyError:
                return jsonify(message='There\'s already a logged user')


ns_move = api.namespace('api/v1/move', description='Operations to move the motors')


@ns_move.route('/<motor>/<direction>')
@ns_move.route('/<motor>/<direction>/<int:speed>')
@api.response(404, 'This action doesn\'t exist.')
class MovingMotors(Resource):
    @api.response(200, 'Action performed.')
    @api.expect(token_arg, validate=False)
    def get(self, motor, direction, speed=None):
        print(token_arg.parse_args()['word'])
        if validate(token_arg.parse_args()['word']):
            if motor == 'left':
                return execute(dir=direction, sp=speed, mot=motor)
            elif motor == 'right':
                return execute(dir=direction, sp=speed, mot=motor)
            elif motor == 'both':
                return execute(dir=direction, sp=speed, mot=motor)


def execute(dir, sp, mot):
    if dir == 'forward':
        if sp is None:
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
                # app.proto.ForwardMotorAwSpeed(speed)
                return jsonify(message='Moving' + mot + 'motor  - ' + dir + ' with speed ' + str(sp))
            elif mot == 'right':
                # app.proto.ForwardMotorBwSpeed(speed)
                return jsonify(message='Moving' + mot + 'motor  - ' + dir + ' with speed ' + str(sp))
            else:
                # app.proto.ForwardBothwSpeed(speed)
                return jsonify(message='Moving both motors  - ' + dir + ' with speed ' + str(sp))
    elif dir == 'reverse':
        if sp is None:
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
                # app.proto.ReverseMotorAwSpeed(speed)
                return jsonify(message='Moving' + mot + 'motor  - ' + dir + ' with speed ' + str(sp))
            elif mot == 'right':
                # app.proto.ReverseMotorBwSpeed(speed)
                return jsonify(message='Moving' + mot + 'motor  - ' + dir + ' with speed ' + str(sp))
            else:
                # app.proto.ReverseBothwSpeed(speed)
                return jsonify(message='Moving both motors  - ' + dir + ' with speed ' + str(sp))

if __name__ == '__main__':
    app.run()
