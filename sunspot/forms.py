from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Regexp, Email, EqualTo

# User registration form:
#   username: 4-20 characters
#   password: at least 8 alphanumeric characters with 1 or more symbols
#   email:
register_username_message = 'Only alphanumeric characters and \'_\' are allowed.'
register_pw_message = 'The passwords must match.'
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Regexp(r'^[\w._]+$', message=register_username_message), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message=register_pw_message)])
    submit = SubmitField('Sign Up')
    
# Login form:
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')