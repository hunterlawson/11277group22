from flask import Flask
from mongoengine import connect
from os import environ
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# Set the Flask secret key, which is used for things like authenticating
# the forms and for user authentication
app.config['SECRET_KEY'] = environ.get('SUNSPOT_SECRET_KEY')
bcrypt = Bcrypt(app)

app.config['MONGO_URI'] = environ.get('SUNSPOT_MONGO_URI')
connect(host=app.config['MONGO_URI'])

from sunspot import views