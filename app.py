from flask            import Flask, redirect, url_for, render_template, request, session
from forms            import LoginForm
from sqlalchemy.orm   import sessionmaker
from tabledef         import *

import helpers, time, json, requests, os

engine = create_engine('sqlite:///accounts.db', echo=True)
app = Flask(__name__)
app.config.from_object(__name__)

# ======== Routing ============================================================ #

# -------- Login -------------------------------------------------------------- #   
@app.route('/', methods=['GET', 'POST'])
def login():
	if not session.get('logged_in'):
		form = LoginForm(request.form)
		if request.method == 'POST':
			username = request.form['username'].lower()
			password = request.form['password']
			if form.validate():  
				if helpers.credentialsValid(username, password):
					session['logged_in'] = True
					session['username'] = username
					return json.dumps({'status': 'Login successful'})
				return json.dumps({'status': 'Invalid user/pass'})
			return json.dumps({'status': 'Both fields required'})	
		return render_template('login.html', form=form)
	
	user = helpers.getUser()
	return render_template('index.html', user=user)

@app.route("/logout")
def logout():
	session['logged_in'] = False
	return redirect(url_for('login'))

# -------- Register ----------------------------------------------------------- #   
@app.route('/register', methods=['GET', 'POST'])
def register():
	if not session.get('logged_in'):
		form = LoginForm(request.form)
		if request.method == 'POST':
			username = request.form['username'].lower()
			password = helpers.hashPassword(request.form['password'])
			email    = request.form['email']
			if form.validate():
				if not helpers.usernameTaken(username):
					s = helpers.getSession()
					u = User(username=username, password=password, email=email, c1="#360033", c2="#0b8793")
					s.add(u)
					s.commit()
					session['logged_in'] = True
					session['username'] = username										
					return json.dumps({'status': 'Register successful'})
				return json.dumps({'status': 'Username taken'})
			return json.dumps({'status': 'Both fields required'})
		return render_template('login.html', form=form)
	return redirect(url_for('login'))

# -------- Settings ----------------------------------------------------------- #   
@app.route('/settings', methods=['GET', 'POST'])
def settings():
	if session.get('logged_in'):
		if request.method == 'POST':	
			user, s = helpers.changeUser()
			if request.form['password'] != "": user.password = helpers.hashPassword(request.form['password'])
			if request.form['email'] != "": user.email = request.form['email']
			if request.form['c1'] != "": user.c1 = request.form['c1']
			if request.form['c2'] != "": user.c2 = request.form['c2']	
			s.commit()
			return json.dumps({'status': 'Saved'})
		user = helpers.getUser()
		return render_template('settings.html', user=user)
	return redirect(url_for('login'))

# ======== Main =============================================================== #
if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(host='127.0.0.1', port='4201')