from flask import Flask
from flask import make_response
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

@app.route('/')
def index():
    app.logger.info('index.html')
    username = request.cookies.get('username')
    if (username == None):
        return redirect(url_for('login'))
    else:
        return render_template('index.html', username=username)

@app.route('/login', methods=['GET','POST'])
def login():
    app.logger.info('login.html')
    if request.method == 'POST':
        if validate_credentials(request.form['username'], request.form['password']):
            resp = make_response(redirect(url_for('index')))
            resp.set_cookie('username', request.form['username']) 
            return resp
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

def validate_credentials(username, password):
    return True

if __name__ == '__main__':
    handler = RotatingFileHandler('todo.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run()

