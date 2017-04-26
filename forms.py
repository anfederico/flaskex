from wtforms import Form, TextField, validators

class LoginForm(Form):
    username = TextField('Username:', validators=[validators.required(), validators.Length(min=1, max=30)])
    password = TextField('Password:', validators=[validators.required(), validators.Length(min=1, max=30)])
    email    = TextField('Email:', validators=[validators.optional(), validators.Length(min=0, max=50)])
