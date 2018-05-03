from flask import Flask, session, redirect, url_for, escape, request, jsonify
import hashlib
from random import randrange

app = Flask(__name__)

app.one_request = True

@app.before_request
def before_request():
    if 'token' in session and request.endpoint in ['login']:
        return jsonify(message='Ya estas logueado')

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    if app.one_request:
        # Primer usuario
        session['token'] = hashlib.md5(str(randrange(2**15)).encode()).hexdigest()
        app.one_request = False
    if not app.one_request:
        try:
            return jsonify(token = session['token'])
        except KeyError:
            return jsonify(message='Ya existe un usuario loggeado')

@app.route('/logout')
def logout():
    if 'token' in session:
        # remove the username from the session if it's there
        app.one_request = True
        session.pop('token', None)
        return jsonify(message='Ha cerrado sesion')
    else:
        return jsonify(message='No existe un usuario logueado')

if __name__ == '__main__':
    app.run()
