from flask import session
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from tabledef import *
import bcrypt

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    s = get_session()
    s.expire_on_commit = False
    try:
        yield s
        s.commit()
    except:
        s.rollback()
        raise
    finally:
        s.close()

def get_session():
    return sessionmaker(bind=engine)()

def get_user():
    username = session['username']
    with session_scope() as s:
        user = s.query(User).filter(User.username.in_([username])).first()
        return user

def add_user(username, password, email, c1, c2):
    with session_scope() as s:
        u = User(username=username, password=password, email=email, c1=c1, c2=c2)
        s.add(u)
        s.commit()

def change_user(**kwargs):
    username = session['username']
    with session_scope() as s:
        user = s.query(User).filter(User.username.in_([username])).first()
        for arg, val in kwargs.items():
            if val != "":
                setattr(user, arg, val)
        s.commit()

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

def credentials_valid(username, password):
    with session_scope() as s:
        user = s.query(User).filter(User.username.in_([username])).first()
        if user:
            return bcrypt.checkpw(password.encode('utf8'), user.password)
        else:
            return False

def username_taken(username):
    with session_scope() as s:
        return s.query(User).filter(User.username.in_([username])).first()
