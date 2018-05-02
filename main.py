"""
It's an API
"""
#app.config_frompyfile('config.py')
from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.one_request = True

@app.before_request
def before_request():
    if 'token' in session and request.endpoint in ['login']:
        return "Ya estas logueado"


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():

    if 'token' in session:
        return

    if app.one_request:
        # Primer usuario
        session['token'] = "sadasda"
        app.one_request = False
    if not app.one_request:
        try:
            text = 'Logged in - token = {}'.format(session['token'])
            return text
        except KeyError:
            return 'Ya existe un usuario loggeado'


@app.route('/logout')
def logout():
    if 'token' in session:
        # remove the username from the session if it's there
        app.one_request = True
        session.pop('token', None)
        return "Ha cerrado sesion"
    else:
        return "No existe un usuario logueado"


if __name__ == '__main__':
    app.run()
