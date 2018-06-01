@app.route('/api/v1/move/w_left/<string:direction>')
@app.route('/api/v1/move/w_left/<string:direction>/<float:time>')
@app.route('/api/v1/move/w_left/<string:direction>/<int:speed>')
def move_wLeft(direction='', speed=None):
    if direction == 'forward':
        if speed is None:
            app.proto.ForwardMotorA()
            return jsonify(code=200, message='Moving left motor - ' + direction)
        else:
            app.proto.ForwardMotorAwSpeed(speed)
            return jsonify(code=200, message='Moving left motor  - ' + direction + ' with speed ' + str(speed))
    elif direction == 'reverse':
        if speed is None:
            app.proto.ReverseMotorA()
            return jsonify(code=200, message='Moving left motor - ' + direction)
        else:
            app.proto.ReverseMotorAwSpeed(speed)
            return jsonify(code=200, message='Moving left motor  - ' + direction + ' with speed ' + str(speed))
    else:
        return jsonify(message='This action doesn\'t exist. Please, go to the documentation for help')


@app.route('/api/v1/move/w_right/<string:direction>')
@app.route('/api/v1/move/w_right/<string:direction>/<int:speed>')
def move_wRight(direction='', speed=None):
    if direction == 'forward':
        if speed is None:
            app.proto.ForwardMotorB()
            return jsonify(code=200, message='Moving right motor  - ' + direction)
        else:
            app.proto.ForwardMotorBwSpeed(speed)
            return jsonify(code=200, message='Moving right motor  - ' + direction + ' with speed ' + str(speed))
    elif direction == 'reverse':
        if speed is None:
            app.proto.ReverseMotorB()
            return jsonify(code=200, message='Moving right motor  - ' + direction)
        else:
            app.proto.ReverseMotorBwSpeed(speed)
            return jsonify(code=200, message='Moving right motor  - ' + direction + ' with speed ' + str(speed))
    else:
        return jsonify(message='This action doesn\'t exist. Please, go to the documentation for help')


@app.route('/api/v1/move/both/<string:direction>')
@app.route('/api/v1/move/both/<string:direction>/<int:speed>')
def move_wLeft(direction='', speed=None):
    if direction == 'forward':
        if speed is None:
            app.proto.ForwardBoth()
            return jsonify(code=200, message='Moving both motors  - ' + direction)
        else:
            app.proto.ForwardBothwSpeed(speed)
            return jsonify(code=200, message='Moving both motors  - ' + direction + ' with speed ' + str(speed))
    elif direction == 'reverse':
        if speed is None:
            app.proto.ReverseBoth()
            return jsonify(code=200, message='Moving both motors  - ' + direction)
        else:
            app.proto.ReverseBothwSpeed(speed)
            return jsonify(code=200, message='Moving both motors  - ' + direction + ' with speed ' + str(speed))
    else:
        return jsonify(message='This action doesn\'t exist. Please, go to the documentation for help')
