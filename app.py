from flask import Flask, redirect, url_for, render_template, request, session
from forms import LoginForm
from tabledef import *
import helpers
import json
import os

engine = db_connect()
app = Flask(__name__)

# ======== Routing =========================================================== #
# -------- Login ------------------------------------------------------------- #
@app.route('/', methods=['GET', 'POST'])
def login():
    if not session.get('logged_in'):
        form = LoginForm(request.form)
        if request.method == 'POST':
            username = request.form['username'].lower()
            password = request.form['password']
            if form.validate():
                if helpers.credentials_valid(username, password):
                    session['logged_in'] = True
                    session['username'] = username
                    return json.dumps({'status': 'Login successful'})
                return json.dumps({'status': 'Invalid user/pass'})
            return json.dumps({'status': 'Both fields required'})
        return render_template('login.html', form=form)
    user = helpers.get_user()
    return render_template('index.html', user=user)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))

# -------- Register ---------------------------------------------------------- #
@app.route('/register', methods=['GET', 'POST'])
def register():
    if not session.get('logged_in'):
        form = LoginForm(request.form)
        if request.method == 'POST':
            username = request.form['username'].lower()
            password = helpers.hash_password(request.form['password'])
            email = request.form['email']
            c1 = "#360033"
            c2 = "#0b8793"
            if form.validate():
                if not helpers.username_taken(username):
                    helpers.add_user(username, password, email, c1, c2)
                    session['logged_in'] = True
                    session['username'] = username
                    return json.dumps({'status': 'Register successful'})
                return json.dumps({'status': 'Username taken'})
            return json.dumps({'status': 'Both fields required'})
        return render_template('login.html', form=form)
    return redirect(url_for('login'))

# -------- Settings ---------------------------------------------------------- #
@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if session.get('logged_in'):
        if request.method == 'POST':
            password = request.form['password']
            if password != "":
                password = helpers.hash_password(password)
            email = request.form['email']
            c1 = request.form['c1']
            c2 = request.form['c2']
            helpers.change_user(password=password, email=email, c1=c1, c2=c2)
            return json.dumps({'status': 'Saved'})
        user = helpers.get_user()
        return render_template('settings.html', user=user)
    return redirect(url_for('login'))

# ======== Main ============================================================== #
if __name__ == "__main__":
    app.secret_key = os.urandom(12) # Generic key for dev purposes only
    app.run(host='127.0.0.1', port='4200')
