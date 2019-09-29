# -*- coding: utf-8 -*-

'''
Flask seems to have it's own Form from flask_wtf... should we replace the Form
from wtforms with Flask's?
'''
from wtforms import Form, StringField, validators, SelectField, IntegerField, SubmitField


class LoginForm(Form):
    username = StringField('Username:', validators=[validators.required(), validators.Length(min=1, max=30)])
    password = StringField('Password:', validators=[validators.required(), validators.Length(min=1, max=30)])
    email = StringField('Email:', validators=[validators.optional(), validators.Length(min=0, max=50)])

class PredictionForm(Form):
    name = StringField('Full Name', validators=[validators.required(), validators.Length(min=1, max=30)])

    COUNTRY_CHOICES = [('United-States','United States'), ('Mexico', 'Mexico'),
     ('Greece', 'Greece')]
    native_country = SelectField(label='Country of Origin', choices=COUNTRY_CHOICES)

    sex = SelectField(label='Sex', choices = [('Female', 'Female'), ('Male', 'Male')])

    race = SelectField(label='Race', choices = [('White', 'White'), ('Black', 'Black')])

    education_level = SelectField(label='Education Level', choices = [
        ('HS-grad', 'HS-grad'), ('Some-college', 'Some-College')])

    work_class = SelectField(label='Work Class', choices = [
        ('?','?'), ('Private', 'Privete')])

    weekly_hours = IntegerField('Hours Worked per Week')

    years_employed = IntegerField('Years in Employment')

    income = IntegerField('Annual Income (USD)')

    submit = SubmitField("Submit")
