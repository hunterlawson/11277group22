from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Regexp, Email, EqualTo

# User registration form:
#   username: 4-20 characters
#   password: at least 8 alphanumeric characters with 1 or more symbols
#   email:
username_message = 'Only alphanumeric characters and \'_\' are allowed.'
email_message = 'Must be a valid email.'
pw_message = 'The passwords must match.'
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Regexp(r'\w', message=username_message), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(message=email_message)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message=pw_message)])
    submit = SubmitField('Sign Up')
    
# Login form:    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message=email_message)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')