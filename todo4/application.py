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
    items = db.ListField(db.StringField(max_length=256))

@app.route('/')
def index():
    app.logger.info('index')
    if 'username' in session:
        user = get_user(session['username'])
        return render_template('index.html', user=user)
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

@app.route('/add', methods=['POST'])
def add():
    app.logger.info('add')
    if 'username' in session:
        User.objects(username=session['username']).update_one(push__items=request.form['item'])
        return redirect(url_for('index'))
    else:
        abort(403)

@app.route('/delete/<int:item>')
def delete(item):
    app.logger.info('delete')
    if 'username' in session:
        User.objects(username=session['username']).update_one(unset__items_0)
        User.objects(username=session['username']).update_one(pull__items=None)
        return redirect(url_for('index'))
    else:
        abort(403)    

def validate_credentials(username, password):
    user = get_user(username)
    return user != None and user.password == password
    
def get_user(username):
    return User.objects(username = username).first()

app.secret_key = 'secret'

if __name__ == '__main__':
    handler = RotatingFileHandler('todo.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run()

