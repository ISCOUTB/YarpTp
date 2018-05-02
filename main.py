from flask import Flask
app = Flask(__name__)

app.config_frompyfile('config.py')

active = False
token = ''

@app.route('/login')
def login():
    if request.post = 'POST':
        # Verify user ---

    if not 'logged_in' in session:
        session['logged_in'] = 'User'



if __name__ == '__mai__':
    app.run('0.0.0.0', 5001)