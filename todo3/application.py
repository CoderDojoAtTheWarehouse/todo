from flask import Flask
from flask import make_response
from flask import request
from flask import session
from flask import render_template
from flask import redirect
from flask import url_for
from flask.ext.mongoengine import MongoEngine

import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'todo',
    'host': 'dogen.mongohq.com',
    'port': 10012,
    'username': 'tododbo',
    'password': 'everclear'
}
db = MongoEngine(app)

class User(db.Document):
    username = db.StringField(required=True,max_length=64)
    password = db.StringField(required=True,max_length=64)

@app.route('/')
def index():
    app.logger.info('index')
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    app.logger.info('login')
    if request.method == 'POST':
        if validate_credentials(request.form['username'], request.form['password']):
            session['username'] = request.form['username'] 
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    app.logger.info('logout')
    session.pop('username', None)
    return redirect(url_for('index'))

def validate_credentials(username, password):
    for user in User.objects(username = username):
        if user.password == password:
            return True
    return False

app.secret_key = 'secret'

if __name__ == '__main__':
    handler = RotatingFileHandler('todo.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run()

