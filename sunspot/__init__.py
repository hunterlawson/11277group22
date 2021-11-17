from flask import Flask
from mongoengine import connect
from os import environ
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

# Set the Flask secret key, which is used for things like authenticating
# the forms and for user authentication
app.config['SECRET_KEY'] = environ.get('SUNSPOT_SECRET_KEY')
app.config['SOLAR_API_KEY'] = environ.get('SUNSPOT_SOLAR_API_KEY')

app.config['MONGO_URI'] = environ.get('SUNSPOT_MONGO_URI')
connect(host=app.config['MONGO_URI'])

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "danger"

from sunspot import views