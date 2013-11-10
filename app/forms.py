from flask import current_app
from flask.ext.wtf import (Form, TextField, PasswordField, Required, Email,
                           Length, Regexp, ValidationError, EqualTo)
from wtforms import Form, BooleanField, TextField, PasswordField, TextAreaField, validators
from wtforms.validators import Required, Length


# class UniqueUser(object):
#     def __init__(self, message="User exists"):
#         self.message = message

#     def __call__(self, form, field):
#         if current_app.security.datastore.find_user(email=field.data):
#             raise ValidationError(self.message)

validators = {
    'email': [
        Required(),
        Email(),
        # UniqueUser(message='Email address is associated with '
        #                    'an existing account')
    ],
    'password': [
        Required(),
        Length(min=1, max=50),
        EqualTo('confirm', message='Passwords must match'),
        Regexp(r'[A-Za-z0-9@#$%^&+=]',
               message='Password contains invalid characters')
    ],
    'username': [
        Required(),
        Length(min=1, max = 30),
        Regexp(r'[A-Za-z0-9]',
               message='Username contains invalid characters')

    ]
}

class RegistrationForm(Form):
    username = TextField('Username', validators['username'])
    email = TextField('Email', validators['email'])
    password = PasswordField('New Password', validators=[Required()])
    confirm = PasswordField('Confirm Password', validators=[EqualTo('password', message='Passwords must match')])
    tos = BooleanField('I accept the TOS', validators=[Required()])

class LoginForm(Form):
    username = TextField('Username', validators = [Required()])
    password = TextField('Password', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

class EditForm(Form):
    username = TextField('nickname', validators = [Required()])
    about_me = TextAreaField('about_me', validators = [Length(min = 0, max = 140)])




