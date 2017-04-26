from flask 			import session
from sqlalchemy.orm import sessionmaker
from tabledef 		import *

import bcrypt

# ======== Helpers =========================================================== #

def getSession():
	return sessionmaker(bind=engine)()

def getUser():
	username = session['username']
	s = getSession()
	user = s.query(User).filter(User.username.in_([username])).first()
	return user

def changeUser():
	username = session['username']
	s = getSession()
	user = s.query(User).filter(User.username.in_([username])).first()	
	return user, s

def hashPassword(password):
	return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

def credentialsValid(username, password):
	s = getSession()
	user = s.query(User).filter(User.username.in_([username])).first()
	if user: return bcrypt.checkpw(password.encode('utf8'), user.password)
	else: return False

def usernameTaken(username):
	s = getSession()
	return s.query(User).filter(User.username.in_([username])).first()