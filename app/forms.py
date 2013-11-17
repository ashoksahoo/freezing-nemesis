from flask import current_app
#from flask.ext.wtf import (Form, TextField, PasswordField, Required, Email, Length, Regexp, ValidationError, EqualTo)
from wtforms import Form, BooleanField, TextField, PasswordField, TextAreaField, validators
from wtforms.validators import Required, Length


 
from flask import *
from flask.ext.sqlalchemy import *
from werkzeug import generate_password_hash, check_password_hash
# class UniqueUser(object):
#     def __init__(self, message="User exists"):
#         self.message = message

#     def __call__(self, form, field):
#         if current_app.security.datastore.find_user(email=field.data):
#             raise ValidationError(self.message)

# validators = {
#     'email': [
#         Required(),
#         Email(),
#         # UniqueUser(message='Email address is associated with '
#         #                    'an existing account')
#     ],
#     'password': [
#         Required(),
#         Length(min=1, max=50),
#         EqualTo('confirm', message='Passwords must match'),
#         Regexp(r'[A-Za-z0-9@#$%^&+=]',
#                message='Password contains invalid characters')
#     ],
#     'username': [
#         Required(),
#         Length(min=1, max = 30),
#         Regexp(r'[A-Za-z0-9]',
#                message='Username contains invalid characters')

#     ]
# }


class LoginForm(Form):
    username = TextField('Username', [validators.Required()])
    password = TextField('Password', [validators.Required()])

class EditForm(Form):
    username = TextField('nickname', validators = [Required()])
    about_me = TextAreaField('about_me', validators = [Length(min = 0, max = 140)])


class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=3, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])


